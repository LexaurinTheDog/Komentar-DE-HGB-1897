#!/usr/bin/env python3
"""Reproducible HGB XML extraction. No historical text reconstruction or commentary generation."""
import json,re,hashlib,shutil,unicodedata
from pathlib import Path
from collections import Counter
from xml.etree import ElementTree as E
W=Path(__file__).resolve().parent
RAW=W/'sources/hgb-2026-10-19.xml'
ORIGINAL=Path('/Volumes/LaCie/law-intake/eu/de/gesetze/gii-hgb.md')
OUT=Path('/Volumes/LaCie/open-commentary/de/Komentar-DE-HGB-1897')
def write(name,obj): (W/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def render(e):
    if e is None:return ''
    s=e.text or ''
    for c in e:
        t=render(c)
        if c.tag=='BR':s+='\n'
        elif c.tag=='DT':s+='\n'+t+' '
        elif c.tag in ('DL','DD'):s+='\n'+t+'\n'
        elif c.tag=='P':s+=t+'\n\n'
        elif c.tag=='LA':s+='\n'+t+'\n'
        else:s+=t
        s+=c.tail or ''
    return s

def clean(s):
    s=s.replace('\u00a0',' ')
    s='\n'.join(re.sub(r'[\t \r]+',' ',x).strip() for x in s.splitlines())
    return re.sub(r'\n{3,}','\n\n',s).strip()
def tx(e):return clean(render(e))
def uid(label):
    label=re.sub(r'^\(XXXX\)\s*','',label)
    if label.startswith('§§'):
        return 'p'+re.sub(r'\s*(?:bis|u\.)\s*','-',label.replace('§','').strip()).replace(' ','')
    return 'p'+label.replace('§','').replace(' ','')
def norm(t):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',t)).strip()
root=E.parse(RAW).getroot()
assert root.tag=='dokumente' and root.get('doknr')=='BJNR002190897'
assert root.find('norm/metadaten/jurabk').text=='HGB'
units=[];structure={};structs=[];global_notes=[]
for n in root.findall('norm'):
    m=n.find('metadaten');g=m.find('gliederungseinheit');en=m.findtext('enbez')
    if g is not None:
        code=g.findtext('gliederungskennzahl');level=len(code)//3
        structure={k:v for k,v in structure.items() if k<level}
        st=re.sub(r'\s+',' ',tx(g.find('gliederungsbez'))+' — '+tx(g.find('gliederungstitel')))
        structure[level]=st
        structs.append(dict(doknr=n.get('doknr'),code=code,label=st));continue
    if not en:
        global_notes.extend([tx(x) for x in n.findall('textdaten/fussnoten/Content') if tx(x)]);continue
    title=re.sub(r'\s+',' ',tx(m.find('titel')));body=tx(n.find('textdaten/text/Content'))
    notes=[tx(x) for x in n.findall('textdaten/fussnoten/Content') if tx(x)]
    label=en  # Preserve the exact official designation, including (XXXX) on grouped repealed slots.
    units.append(dict(id=uid(en),label=label,title=title,chapter=0,structure=[v for k,v in sorted(structure.items())],text=body,notes=notes,official_enbez=en,official_doknr=n.get('doknr'),empty_slot=not bool(body),grouped_slot=bool(re.match(r'^(?:\(XXXX\)\s*)?§§',label))))
ids=[u['id'] for u in units];assert len(ids)==len(set(ids))
# Separate chapters at Book/Abschnitt boundaries and every 25 units.
chapters=[];prev=None;count=0
for u in units:
    key=tuple(u['structure'][:2])
    if key!=prev or count>=25:
        chapters.append(dict(n=len(chapters)+1,slug='hgb-'+str(len(chapters)+1).zfill(2),title=' / '.join(u['structure'][:2])))
        count=0;prev=key
    u['chapter']=len(chapters);count+=1
for c in chapters:
    us=[u for u in units if u['chapter']==c['n']]
    c['title']+=' ('+(us[0]['label'] if us[0]['label']==us[-1]['label'] else us[0]['label']+'–'+us[-1]['label'])+')'
canonical=['# Handelsgesetzbuch — mechanische XML-Transkription','\nQuelle: https://www.gesetze-im-internet.de/hgb/xml.zip','\nAbruf: 2026-10-19; XML-builddate: '+root.get('builddate')]
for u in units:
    canonical+=['\n## '+u['label']+(' — '+u['title'] if u['title'] else ''),'\n'+u['text']]
    for note in u['notes']:canonical+=['\nRedaktioneller Hinweis:\n'+note]
(W/'sources/hgb-canonical.md').write_text('\n'.join(canonical)+'\n')
with (W/'units.jsonl').open('w') as f:
    for u in units:f.write(json.dumps(u,ensure_ascii=False)+'\n')
meta=dict(cc='de',lang='de',repo='Komentar-DE-HGB-1897',repo_dir=str(OUT),title='Kommentar zum Handelsgesetzbuch',source_path=str(W/'sources/hgb-canonical.md'),intro_file='00-einleitung.md',intro_desc='Geltungsstand, Systematik und Arbeitsmethode',labels=dict(text='Wortlaut der Vorschrift',chapter='Kommentarkapitel',notes='Redaktioneller Quellenhinweis'),chapters=chapters,decisive_date='2026-10-19',source_xml_sha256=hashlib.sha256(RAW.read_bytes()).hexdigest(),status='authoring')
write('meta.json',meta);write('sources/structure.json',structs);write('sources/global-notes.json',global_notes)
# Derive official inventory directly from the raw XML, independently of generated JSONL.
expected=[]
for n in E.parse(RAW).getroot().findall('norm'):
    label=n.findtext('metadaten/enbez')
    if label:expected.append(dict(official_identifier=n.attrib['doknr'],enbez=label,id=uid(label)))
expected_ids=[x['id'] for x in expected]
parsed=[json.loads(l) for l in (W/'units.jsonl').read_text().splitlines()]
parsed_ids=[x['id'] for x in parsed]
annex=[n.get('doknr') for n in root.findall('norm') if 'Anlage' in (n.findtext('metadaten/enbez') or '')]
assert not annex
report=dict(source_xml=str(RAW.relative_to(W)),source_sha256=meta['source_xml_sha256'],official_inventory=expected,expected_ids=expected_ids,parsed_ids=parsed_ids,official_norm_nodes=len(root.findall('norm')),metadata_nodes=1,structural_nodes=len(structs),expected_count=len(expected_ids),parsed_count=len(parsed_ids),missing=sorted(set(expected_ids)-set(parsed_ids)),unexpected=sorted(set(parsed_ids)-set(expected_ids)),duplicates=[k for k,v in Counter(parsed_ids).items() if v>1],empty_slots=[dict(id=u['id'],label=u['label'],title=u['title'],notes=u['notes']) for u in parsed if u['empty_slot']],grouped_slots=[dict(id=u['id'],label=u['label'],disposition='Amtliche Sammelbezeichnung für weggefallene Vorschriften bleibt als eine XML-Einheit erhalten; keine historische Fassung ergänzt.') for u in parsed if u['grouped_slot']],annex_disposition='Keine Anlage als eigene HGB-Norm im amtlichen XML. Fremdgesetzliche Anwendungs- und Übergangsverweise bleiben in den Quellenhinweisen; das EGHGB ist ein gesondertes Gesetz und nicht Teil des HGB-Manuskripts.',limitations=['Die Zählung folgt amtlichen Normknoten, einschließlich zusammengefasster Leerstellen; sie ist keine Anzahl aller historisch einmal vergebenen Paragraphennummern.'])
report['repealed_slots']=[dict(id=u['id'],label=u['label'],title=u['title'],body=u['text'],disposition='Amtliche Leerstelle einschließlich vorhandener Strich-/Titelmarkierung bewahrt; kein historischer Wortlaut ergänzt.') for u in parsed if u['empty_slot'] or 'weggefallen' in u['title']]
report['internal_repealed_paragraphs']=[dict(id=u['id'],markers=re.findall(r'\([0-9a-z]+\) \(weggefallen\)',u['text'])) for u in parsed if re.search(r'\([0-9a-z]+\) \(weggefallen\)',u['text'])]
report['ok']=not(report['missing'] or report['unexpected'] or report['duplicates'])
write('completeness-report.json',report)
shutil.copyfile(ORIGINAL,W/'sources/intake-2026-10-01.md')
original=norm(ORIGINAL.read_text())
changes=[]
for u in units:
    paragraphs=[p for p in re.split(r'\n\s*\n',u['text']) if len(p.strip())>10]
    unmatched=[p for p in paragraphs if norm(p) not in original]
    if unmatched:changes.append(dict(id=u['id'],unmatched_paragraphs=unmatched,disposition='Text-/Formatdifferenz zur lokalen Markdown-Transkription; nicht automatisch eine Gesetzesänderung.'))
write('sources/change-map.json',dict(original_path=str(ORIGINAL),original_sha256=hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),official_xml_sha256=meta['source_xml_sha256'],old_stand='Zuletzt geändert durch Art. 4 G v. 4.2.2026 I Nr. 33',new_stand=[x.text for x in root.findall('norm/metadaten/standangabe/standkommentar')],unmatched_units=changes,unit_count_explanation='813 Intake-Einheiten = 696 Normeinheiten + 117 Gliederungsknoten. Die zusätzliche XML-Kopfnorm führt zu insgesamt 814 XML-norm-Knoten.'))
print(json.dumps(dict(units=len(units),chapters=len(chapters),structure=len(structs),unmatched_intake_units=len(changes),completeness_ok=report['ok']),ensure_ascii=False))
