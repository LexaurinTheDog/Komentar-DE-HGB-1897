"""Copy evidence and normalize relative export links without editing reviewed prose."""
from pathlib import Path
import json,shutil,re,hashlib
W=Path(__file__).resolve().parent;O=Path(json.loads((W/'meta.json').read_text())['repo_dir'])
for base in [W,O]:
 d=base/'sources/assembly-history'
 for p in d.glob('*.md'):p.rename(p.with_suffix('.md.txt'))
for d in ['sources','cases']:shutil.copytree(W/d,O/d,dirs_exist_ok=True)
changes=[]
for p in O.rglob('*.md'):
 if '.git' in p.parts:continue
 def fix(m):
  target=m[1]
  if re.match(r'^(https?://|mailto:|#|data:)',target):return m[0]
  if (p.parent/target.split('#')[0]).exists():return m[0]
  clean=target
  while clean.startswith('../'):clean=clean[3:]
  dest=O/clean.split('#')[0]
  if dest.exists():
   import os
   corrected=os.path.relpath(dest,p.parent)+('#'+clean.split('#',1)[1] if '#' in clean else '')
   changes.append(dict(file=str(p.relative_to(O)),old=target,new=corrected));return ']('+corrected+')'
  return m[0]
 text=p.read_text();new=re.sub(r'\]\(([^\n]+?)\)',fix,text)
 if new!=text:p.write_text(new)
(W/'export-link-normalization.json').write_text(json.dumps({'scope':'Relative local export paths only; ledger-reviewed commentary bodies unchanged in WORK.','changes':changes},ensure_ascii=False,indent=2)+'\n')
shutil.copy2(W/'export-link-normalization.json',O/'export-link-normalization.json')
manifest={'description':'Source snapshots, derived evidence and case cards; URL/HTTP metadata in verification records.','files':[]}
for d in ['sources','cases']:
 for p in sorted((W/d).rglob('*')):
  if p.is_file():manifest['files'].append(dict(path=str(p.relative_to(W)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(W/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');shutil.copy2(W/'source-manifest.json',O/'source-manifest.json')
print('Normalized export links:',len(changes))
