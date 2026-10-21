# Autorenkontrolle — kein unabhängiges Zweitgutachten

Stand: 19. Oktober 2026. Dieser Bericht dokumentiert die eigene Arbeitskontrolle des Entwurfs. Eine unabhängige zweite Prüfung durch einen frischen Prozess hat nicht stattgefunden. Es liegt keine externe anwaltliche Freigabe vor.

## Gesicherte technische Befunde

- Amtliches HGB-XML und HTML-Inhaltsverzeichnis enthalten dieselben 696 Normkennungen; kein fehlender oder doppelter Eintrag im Parsergebnis.
- 117 Gliederungsknoten sind von Vorschriften getrennt; amtliche Sammelleerstellen und interne Wegfallmarker bleiben erhalten. Keine eigene Anlage im amtlichen HGB-XML.
- Sämtlicher extrahierter Gesetzestext stimmt ohne Leerraum mit dem XML überein. Die strenge Wortlautprüfung gegen die kanonische Quelle ergibt 100 Prozent. Gegenüber dem erhaltenen Intake besteht nach Leerraumnormalisierung keine Textabweichung.
- 233 Kommentare mit 290.696 Zeichen sind vorhanden. Es gibt keine doppelte Kommentarzuordnung, keinen unbekannten Einheitenbezeichner, keinen zu kurzen vorhandenen Kommentar nach den technischen Mindestgrenzen und keinen exakt identischen wiederholten längeren Prosaabsatz.

Die Berichte [audit-report.json](audit-report.json) und [completeness-report.json](completeness-report.json) enthalten Einzelkennungen und Quellenhashes. Die Längen- und Wiederholungsprüfung beweist keine rechtliche Qualität und erkennt nicht jede semantische Ähnlichkeit.

## Sachliche Kontrollpunkte

Zeitliche Fassungen wurden anhand des Standortfördergesetzes getrennt. Die aktuelle OHG-Nummerierung ist zugrunde gelegt; alte Nummern werden nicht unbesehen fortgeschrieben. Die amtlich noch abgedruckte Regel des § 75 Absatz 3 wird im Kommentar anhand des vollständig gelesenen BAG-Urteils als nicht anwendbar erläutert. Firmen- und Etablissementbezeichnung sowie interne Geschäftsführung und Außenvertretung werden getrennt behandelt. Die drei aufgenommenen Fallkarten begrenzen ihre Aussagen auf tatsächlich gelesene Entscheidungsinhalte.

## Offene Arbeit

463 Kommentare ab § 264 fehlen. Der gemeinsame Builder lehnt das Gesamtmanuskript deshalb ab; die strenge Gesamtvalidierung ist negativ. Ein lesbarer Export der 15 bereits vollständig kommentierten Kapitel ist ein ausdrücklich gekennzeichneter Teilstand und keine Verengung der Gesamtzuweisung. [Build-Ergebnis](build-result.json), [Validierung](validation.json) und [Status](status.json) bleiben zugänglich.

Die rechtliche Qualität jedes später hinzukommenden Abschnitts, zusätzliche einschlägige Rechtsprechung, externe Querverweise und eine unabhängige Durchsicht des gesamten fertigen Manuskripts stehen weiter aus. Es wird kein Abschlussstatus `drafted_technical_validation` vergeben.

## Begrenzte Quellen-/Parsernachprüfung vom 21. Oktober 2026

Alle 814 amtlichen XML-Knoten wurden zugeordnet (696 Normen, 117 Strukturknoten, eine Kopfnorm). Keine unzugeordnete Eingangsformel oder operative Anlage wurde festgestellt. Die Bezeichnungen der sieben Sammelleerstellen wurden repariert, ohne die stabilen Kommentar-IDs oder Kommentartexte zu ändern. [preflight-result.json](preflight-result.json) dokumentiert den abgeschlossenen Teilauftrag. Dies ist keine inhaltliche Zweitprüfung der Kommentare.

## Unabhängiger begrenzter zweiter Durchgang am 21. Oktober 2026

Ein frischer Prüfprozess hat ausschließlich die 20 Einheiten `p1`–`p13` einschließlich `p8a`, `p8b`, `p9a`–`p9d` und `p10a` vollständig gegen den amtlichen XML-Text gelesen. Die früheren Aussagen über eine noch nicht erfolgte Zweitprüfung beschreiben den damaligen Gesamtstand; eine Prüfung aller 696 Einheiten wird auch jetzt nicht behauptet. Einzelbefunde und genaue Kennungen dieses früheren Durchgangs bleiben im [Prüfledger](batch-review-ledger.json) erhalten.

Sieben Kommentare wurden ergänzt oder präzisiert: § 3 (allgemeiner Löschungsweg), § 8a (Weiterübertragung), § 8b (Datenkategorien, Hinterlegung und Zweckbindung), § 9 (Authentifizierung und Bestätigung), § 9a (Soll-Mindestdauer), § 12 (Rechtsnachfolge) und § 13 (Anmeldepflichtige und Gericht). Die übrigen 13 Kommentare bleiben nach sachlicher Prüfung erhalten. Keine fremden Kommentarabschnitte wurden ersetzt.

Der erneute amtliche Abruf lieferte HTTP 200 und denselben XML-Hash wie am 19. Oktober. Die zeitliche Trennung des § 9d wurde anhand der verkündeten Artikel 3, 4 und 64 erneut geprüft. Die Kontrolle aller XML-Knoten bestätigt weiterhin 696 Vorschriften, 117 Gliederungsknoten und eine Kopfnorm ohne unzugeordneten operativen Text; keine fehlende Eingangsformel oder eigene Gesetzesanlage. Die technischen Kontrollen ersetzen die hier protokollierte Einzelprüfung nicht.

Der Teilprüfauftrag ist abgeschlossen. Das Buch bleibt ein unvollständiger Entwurf mit 463 fehlenden Kommentaren außerhalb des Prüfauftrags. Neue Rechtsprechung wurde in diesem Durchgang nicht aufgenommen; die geprüften Kommentare enthalten keine konkrete Entscheidungszitation. Eine externe anwaltliche Freigabe liegt nicht vor.

## Begrenzter zweiter Durchgang: §§ 13a–25, 21. Oktober 2026

Die exakt 20 zugewiesenen Einheiten wurden jeweils vollständig mit dem amtlichen Text verglichen; die Kennungen und Einzelbefunde stehen in [review-result.json](review-result.json) und dauerhaft in [review-p13a-p25.json](review-p13a-p25.json). Vier Kommentare wurden berichtigt oder vertieft: § 13e (Insolvenzanmeldepflichtige), § 13f (Anmeldezeitpunkt, Anlagen und EU-/EWR-Ausnahmen), § 13g (Zweijahresbezug und Ausnahmen) und § 14 (gebundene Durchsetzung). Die übrigen 16 Kommentare wurden nach Einzelprüfung erhalten.

Die amtlichen Volltexte zu BGH II ZR 220/22 und II ZR 140/13 wurden vollständig gelesen und die zitierten Randnummern mit Aussagen, Verfahrenskontext und Fallkarten verglichen. Keine neue Entscheidung wurde aufgenommen. Die Kenntnisregel des § 15 Absatz 1 wird nicht auf dessen geänderten Absatz 3 übertragen; der Hotelbeschluss belegt keine allgemeine Ausnahme für Hotelbetriebe.

Der erneute amtliche ZIP-Abruf ergab HTTP 200 und denselben XML-Hash wie der maßgebliche Ausgangstext vom 19. Oktober. Die vorhandene Inkrafttretensprüfung und vollständige Knotenzuordnung wurden gegengeprüft. Keine historische Doppelfassung, eigenständige Anlage oder fehlende Eingangsformel wurde festgestellt. Die technischen Prüfungen ergeben vollständige Normabdeckung und 100 Prozent Wortlautübereinstimmung; sie ersetzen keine inhaltliche Prüfung. Der Teilauftrag ist abgeschlossen; 463 nicht ausgearbeitete Kommentare außerhalb dieses Auftrags verhindern weiterhin den Gesamtbuild.

## Begrenzter zweiter Durchgang: §§ 26–53, 21. Oktober 2026

Exakt 20 zugewiesene Einheiten einschließlich § 37a und der Sammelleerstelle §§ 38 bis 47b wurden vollständig am erneut abgerufenen amtlichen XML gelesen. Einzelbefunde und genaue Kennungen stehen dauerhaft in [review-p26-p53.json](review-p26-p53.json). Vier Kommentare wurden korrigiert oder vertieft: § 32 (Aufhebungsereignisse), § 33 (Eintragungskatalog und Urkundenform), § 34 (Zeitpunkt des Zuständigkeitswechsels), § 37 (gebundene Durchsetzung samt Beispiel). Die übrigen 16 Kommentare wurden nach inhaltlicher Einzelprüfung erhalten. Die Kommentare enthalten keine Entscheidungszitate; neue Rechtsprechung wurde nicht aufgenommen.

HTTP 200, ZIP-/XML-Formatprüfung und identischer Quellhash bestätigen den gesicherten Quellenstand. Inkrafttretensregeln wurden anhand des erhaltenen Verkündungstexts erneut abgeglichen; spätere Fassungen werden nicht vorgezogen. Alle amtlichen Normknoten sind zugeordnet, ohne historische Dubletten, eigenständige Anlage oder fehlende Eingangsformel. Der Teilprüfauftrag ist abgeschlossen, das Gesamtbuch mit 463 fehlenden Kommentaren bleibt unvollständig. Keine externe anwaltliche Freigabe.

## Begrenzter zweiter Durchgang: §§ 54–75a, 21. Oktober 2026

Exakt 20 zugewiesene Einheiten einschließlich § 74a–c und der Sammelleerstelle §§ 66 bis 72 wurden vollständig gegen den amtlichen XML-Text gelesen. Kennungen und Einzelbefunde: [review-p54-p75a.json](review-p54-p75a.json). Fünf Kommentare wurden präzisiert oder korrigiert: §§ 60, 62, 64, 75 und 75a. Die übrigen 15 wurden nach inhaltlicher Einzelprüfung erhalten.

Wesentlicher Befund: Der bisherige §-75-Kommentar und die BAG-Fallkarte übertrugen die Nichtigkeitsaussage zum früheren Absatz 3 fälschlich auf den heutigen ausdrücklichen Verweis auf Absatz 1. Der aktuelle Wortlaut wurde erneut amtlich abgerufen und das Urteil 10 AZR 260/14 vollständig gelesen. Kommentar und Fallkarte sind berichtigt; historische Entscheidungsgründe und heutige Gesetzesfassung bleiben getrennt. § 75 Absatz 2 erläutert jetzt ausdrücklich die Monatsfrist und schriftliche Lossagung. Die Aussagen zu § 74a bleiben durch die tatsächlichen Entscheidungsgründe gedeckt.

Erneuter amtlicher Abruf: HTTP 200, gültiges ZIP und XML, identischer Quellhash. Quellenstand und Inkrafttretensregeln sowie alle amtlichen Kennungen, Gliederungsknoten, leeren Stellen und das Fehlen einer separaten Anlage oder Eingangsformel wurden gegengeprüft. Kein neuer operativer Text fehlt. Das Gesamtbuch bleibt mit 463 fehlenden Kommentaren unvollständig. Die abgeschlossene Teilprüfung und der partielle Export sind keine Gesamtfreigabe oder externe anwaltliche Prüfung.

## Begrenzter zweiter Durchgang: §§ 75b–87d, 21. Oktober 2026

Genau die 20 beauftragten Einheiten wurden einzeln am erneut abgerufenen amtlichen XML gelesen, einschließlich §§ 75b, 75e und der Sammelleerstelle §§ 76 bis 82. [Einzelbefunde und exakte Kennungen](review-p75b-p87d.json). §§ 75c, 75f, 75h, 87, 87a und 87c wurden präzisiert; die übrigen 14 Kommentare sind nach Prüfung erhalten. Wesentlich sind die Trennung der Alternativen in § 87 Absatz 3 Nummer 1 und die Verteilung der Personenwahl bei der Bucheinsicht nach § 87c Absatz 4. § 87a nennt jetzt ausdrücklich die späteste Vorschussfälligkeit; § 75c erklärt die Rechtsfolgen des §-340-Verweises.

Amtlicher ZIP-Abruf: HTTP 200, Format gültig, XML-Hash unverändert. Wirksamkeitsregeln und Quellenvergleich wurden erneut gelesen; alle 696 amtlichen Kennungen sind ohne Dubletten abgedeckt, keine zusätzliche operative Eingangsformel oder Anlage wurde gefunden. Der zunächst fehlgeschlagene BGH-PDF-Abruf wurde protokolliert. Danach wurde das vollständige Urteil I ZR 245/12 im lokalen Justizkorpus gefunden und über den amtlichen ZIP/XML-Endpunkt von Rechtsprechung im Internet mit HTTP 200 verifiziert. Alle Absätze wurden mit dem Intake abgeglichen. Kommentar und Fallkarte erklären die grundsätzliche Einbeziehung von Abwerbeverboten, die enge Nebenabredenausnahme und die zeitliche Begrenzung im entschiedenen Fall. Nur diese selektive Rechtsprechungsprüfung ist abgeschlossen. Das Gesamtbuch bleibt unvollständig; dieser Teilcheckpoint ist keine Gesamtfreigabe und keine externe anwaltliche Prüfung.

## Begrenzter zweiter Durchgang: §§ 88–99, 21. Oktober 2026

Genau 20 Einheiten wurden einzeln am erneut abgerufenen amtlichen XML geprüft: §§ 88, 88a, 89, 89a, 89b, 90, 90a, 91, 91a, 92, 92a, 92b, 92c, 93, 94, 95, 96, 97, 98 und 99. [Einzelbefunde und exakte reviewed_ids](review-p88-p99.json). Vier Kommentare wurden präzisiert: § 89 nennt alle Monatsfristen; § 89b erklärt die Ausschlüsse und besondere Dreijahresvergütungsgrenze; § 90a benennt die Unternehmerunterschrift; § 92c benennt die EG-/EWR-Gebietsgrenze ausdrücklich. Die übrigen 16 Kommentare bleiben nach inhaltlicher Prüfung erhalten.

Zu § 89b wurde BGH VII ZR 328/12 vom 6. Oktober 2016 aus dem lokalen nationalen Justizkorpus ermittelt und als amtlicher XML-Volltext erneut abgerufen und vollständig gelesen. Die ergänzte Erklärung betrifft ausschließlich den Neukundenbegriff bei getrennten Produktlinien. Parteivortrag, Vorinstanz und BGH-Begründung sind getrennt; der historische Gesetzesstand und die Zurückverweisung werden erläutert. Die Fallkarte enthält präzise Randnummern und Quellenbelege. Eine erschöpfende Rechtsprechungsrecherche ist damit nicht behauptet.

Der amtliche HGB-Abruf ergab HTTP 200 und gültiges ZIP/XML; der XML-Hash ist unverändert. Die geltungsbezogenen Nachweise und Inkrafttretensregeln wurden erneut gelesen. Alle 696 Normkennungen und ihre Texte stimmen mit units.jsonl überein; alle 814 XML-Knoten sind zugeordnet. Es gibt keine gesonderte operative Anlage oder ausgelassene Eingangsformel. Der leere § 88 bleibt erhalten. Keine exakte Wiederholung längerer Kommentarabsätze in der geprüften Gruppe. Die Prüfung der Mindestlänge ist keine Aussage über juristische Qualität.

Das Gesamtbuch enthält weiterhin 463 fehlende Kommentare außerhalb dieses Auftrags. Der vollständige Build und die strenge Gesamtvalidierung bleiben deshalb gesperrt; die betroffenen Kapitel werden als nachvollziehbarer Teilcheckpoint neu aus den vorhandenen Einheiten und Kommentaren erzeugt. Dies ist keine Gesamtfreigabe oder externe anwaltliche Prüfung.

## Begrenzter zweiter Durchgang: §§ 100–118, 21. Oktober 2026

Genau 20 beauftragte Einheiten, einschließlich § 104a, wurden vollständig gegen das erneut abgerufene amtliche XML gelesen. [Einzelbefunde mit exakten reviewed_ids](review-p100-p118.json). Vier Kommentare sind korrigiert oder vertieft: § 100 erklärt die qualifizierte elektronische Signatur; § 103 unterscheidet die Fahrlässigkeitsandrohung in Nummer 1 vom Vorsatzerfordernis bei vorzeitiger Vernichtung nach Nummer 2; § 106 nennt die Anmeldedaten und Versicherung vollständig; § 116 erläutert Entziehungsgründe und die entsprechende Anwendung von § 671 Absätzen 2 und 3 BGB. Die übrigen 16 Kommentare bleiben nach Einzelprüfung erhalten. Die drei externen Gesetzesverweise wurden unmittelbar am amtlichen Text geprüft und gesichert.

Der neue HGB-Abruf ergab HTTP 200, ein gültiges ZIP und HGB-XML mit unverändertem SHA-256. Die Inkrafttretensregel des Artikel 64 BGBl. 2026 I Nr. 33 und der Quellenvergleich zum Intake wurden erneut geprüft. Alle 696 Normkennungen und Texte stimmen mit units.jsonl überein; alle 814 XML-Knoten sind erfasst. Keine historische Dublette, separate operative Anlage oder fehlende Eingangsformel festgestellt. Selektive Suche im amtlichen Webangebot und lokalen Justizmanifest führte zu keiner zusätzlich übernommenen verifizierten Entscheidung. Ältere Aussagen zum Beschlussmängelrecht werden nicht ungeprüft auf das heutige Regime übertragen. Dies behauptet keine erschöpfende Rechtsprechungsabdeckung.

Die zugewiesenen Kommentare sind vollständig; längere Absätze wiederholen sich innerhalb dieser Gruppe nicht exakt. Die Mindestlängenprüfung ersetzt keine inhaltliche Prüfung. Der vollständige Builder und die strenge Gesamtvalidierung scheitern weiterhin ausschließlich an 463 fehlenden Kommentaren außerhalb des Auftrags. Die drei betroffenen Kapitel werden nach den unveränderten Darstellungsregeln des Builders als Teilcheckpoint neu erzeugt. Keine Gesamtfertigstellung, unabhängige Gesamtfreigabe oder externe anwaltliche Prüfung wird behauptet.

## Begrenzter zweiter Durchgang: §§ 119–138, 21. Oktober 2026

Genau die 20 beauftragten Einheiten wurden vollständig mit dem erneut abgerufenen amtlichen XML verglichen und inhaltlich geprüft. [Einzelbefunde und exakte reviewed_ids](review-p119-p138.json). Sechs Kommentare wurden vertieft: § 119 nennt Zinssatz und Erstattungsgrundlage; § 120 erklärt die Rangfolge der Gewinnverteilung nach § 709 Absatz 3 BGB; § 124 erläutert Niederlassungsgrenze, gerichtlichen Entzug und Erklärungsempfang bei Gesamtvertretung; § 131 erklärt die besondere Ablaufhemmung; § 132 benennt die Ausnahmen des Volljährigkeitsrechts; § 137 unterscheidet die Sicherungsalternativen und den Registerstichtag beim Wechsel zum Kommanditisten. Die übrigen 14 Kommentare bleiben nach Einzelprüfung erhalten. Alle Beispiele und internen Verweise wurden auf ihren Bezug zum geltenden Tatbestand geprüft.

Amtlicher ZIP-Abruf: HTTP 200, gültiges ZIP/XML und identischer SHA-256. Die Inkrafttretensregel des Artikels 64 BGBl. 2026 I Nr. 33 sowie der Quellenvergleich zum Intake wurden erneut gelesen. Sämtliche 696 Normkennungen und Texte stimmen mit units.jsonl überein; alle 814 XML-Knoten sind zugeordnet. Keine historische Dublette, operative Anlage oder ausgelassene Eingangsformel festgestellt. Die externen BGB-Verweise zu Beitragsverhältnissen, Aufwendungen und Ablaufhemmung wurden amtlich nachgeprüft und gesichert.

Eine selektive amtliche Websuche und Suche im lokalen Justizmanifest wurden protokolliert. Ein älterer Nachhaftungstreffer wurde ohne Volltext- und Fassungsprüfung nicht als aktueller Entscheidungsbeleg verwendet. Kein neues Urteil wird zitiert; eine erschöpfende Rechtsprechungsrecherche wird nicht behauptet. Die längeren Absätze der geprüften Kommentare wiederholen sich nicht exakt. Die technische Mindestlänge beweist keine juristische Qualität.

Der Teilprüfauftrag ist abgeschlossen. Der vollständige Builder und die strenge Gesamtvalidierung bleiben wegen 463 fehlender Kommentare außerhalb dieses Auftrags gesperrt. Der nachvollziehbare Teilcheckpoint umfasst die vollständig vorhandenen Kapitel. Keine Gesamtfertigstellung oder externe anwaltliche Freigabe.

## Begrenzter zweiter Durchgang: §§ 139–165, 21. Oktober 2026

Genau die 20 beauftragten Einheiten einschließlich der leeren Sammelstelle §§ 153 bis 160 wurden vollständig am erneut abgerufenen amtlichen XML gelesen. [Exakte reviewed_ids und Einzelbefunde](review-p139-p165.json). Fünf Kommentare wurden präzisiert: § 139 nennt Vorsatz und grobe Fahrlässigkeit; § 143 konkretisiert die Zustimmung bei alternativer Abwicklung; § 144 erklärt die KG-Ausnahme des § 178; § 148 benennt Einbringungswert und Verteilungsmaßstab; § 151 verdeutlicht den alternativen Fristbeginn ohne Jahresendregel und die ausdrücklich begrenzte Hemmungsverweisung. Die anderen 15 Kommentare bleiben nach inhaltlicher Einzelprüfung erhalten.

Der amtliche Abruf ergab HTTP 200, gültiges ZIP/XML und denselben SHA-256 wie die wirksamkeitsgeprüfte Fassung vom 19. Oktober. Inkrafttretensnachweise und Intake-Vergleich wurden erneut gelesen. Alle 696 Kennungen und Texte stimmen mit units.jsonl überein, alle 814 XML-Knoten sind zugeordnet. Keine historische Dublette, separate operative Anlage oder fehlende Eingangsformel. Alle Beispiele und Verweise wurden im Kontext geprüft; keine exakten Wiederholungen längerer Absätze innerhalb dieser Gruppe. Mindestlängen sind kein Beweis juristischer Qualität.

Die selektive amtliche Websuche und lokale Justizmanifest-Suche sind protokolliert. Kein neuer Entscheidungsbeleg wird übernommen; ältere Treffer wurden ohne Volltext- und Fassungsprüfung nicht als Autorität verwendet. Keine erschöpfende Rechtsprechungsabdeckung wird behauptet. Der vollständige Builder und die strenge Gesamtvalidierung bleiben wegen 463 fehlender Kommentare außerhalb dieser Gruppe gesperrt. Die betroffenen vollständigen Kapitel werden als Teilcheckpoint aufgebaut. Dies ist keine Gesamtfertigstellung oder externe anwaltliche Freigabe.


## Begrenzter zweiter Durchgang: §§ 166–232, 21. Oktober 2026

Genau die 20 zugewiesenen Einheiten einschließlich § 172a und der Sammelleerstelle §§ 180 bis 229 wurden vollständig am erneut abgerufenen amtlichen XML gelesen. [Exakte reviewed_ids und Einzelbefunde](review-p166-p232.json). § 172 wurde zu Haftsumme, Kapitalanteil, bilanziellen Verweisen und genauer Beteiligungskettenausnahme präzisiert. § 177a erläutert zusätzlich die verwiesene Ausnahme bei Personengesellschaften sowie Vordrucke, Bestellscheine und Zwangsgeld. Die anderen 18 Kommentare bleiben nach inhaltlicher Prüfung erhalten. Beispiele, Absatzunterschiede und Querverweise wurden im jeweiligen Kontext geprüft.

Amtlicher Abruf: HTTP 200, gültiges ZIP/XML und identischer SHA-256 zur wirksamkeitsgeprüften Fassung vom 19. Oktober. Inkrafttretensnachweis und Intake-Vergleich wurden erneut gelesen. Alle 696 amtlichen Kennungen und Texte stimmen mit dem Parsergebnis überein; alle 814 XML-Knoten sind zugeordnet. Keine historische Dublette, operative Anlage oder ausgelassene Eingangsformel. Längere Prosaabsätze dieser Gruppe wiederholen sich nicht exakt; Mindestlängen beweisen keine rechtliche Qualität.

Die selektive amtliche Websuche und lokale Manifest-Suche stehen im [Suchprotokoll](sources/research/case-search-p166-p232.json). Es wird keine zusätzliche Entscheidung zitiert; ältere Suchtreffer ohne vollständige Volltext- und Fassungsprüfung werden nicht als Belege verwendet. Keine erschöpfende Rechtsprechungsabdeckung. Der vollständige Builder und die strenge Gesamtvalidierung bleiben wegen 463 fehlender Kommentare außerhalb des Auftrags gesperrt. Die Kapitel 12 und 13 werden als überprüfbarer Teilcheckpoint neu erzeugt. Keine Gesamtfertigstellung oder externe anwaltliche Freigabe.


## Begrenzter zweiter Durchgang: §§ 233–251, 21. Oktober 2026

Genau die 20 beauftragten Einheiten einschließlich § 241a und der leeren Stelle § 237 wurden vollständig am amtlichen XML geprüft. [Einzelbefunde und exakte reviewed_ids](review-p233-p251.json). Sechs Kommentare sind präzisiert: § 234 zu sämtlichen verwiesenen Kündigungsvoraussetzungen, § 245 sprachlich zur Unterzeichnung, § 246 zu Schuldnerzuordnung, Firmenwert und zwingender Verrechnung, § 248 zu vergleichbaren immateriellen Werten, § 250 zu Ausgaben-/Einnahmenbegriffen und zeitlicher Objektivierbarkeit, § 251 zur besonderen Anhangregel. Die übrigen 14 bleiben nach Einzelprüfung erhalten.

Der erneute amtliche Abruf ergab HTTP 200 und dasselbe gültige XML wie die wirksamkeitsgeprüfte Fassung vom 19. Oktober. Inkrafttretensnachweis und Intake-Vergleich wurden erneut gelesen. Alle 696 Kennungen und Texte stimmen überein; 814 XML-Knoten sind zugeordnet. Keine historische Dublette, ausgelassene Eingangsformel oder operative Gesetzesanlage. Keine identischen längeren Prosaabsätze innerhalb dieser Gruppe; Mindestlänge beweist keine juristische Qualität.

Der [BFH-Volltext IV R 22/20](cases/BFH-2023-IV-R-22-20.md) wurde vollständig ausgewertet, einschließlich der Grenzen des steuerlichen Altfalls. [Selektive Web- und lokale Suche](sources/research/case-search-p233-p251.json); keine erschöpfende Rechtsprechungsabdeckung. Keine externe anwaltliche Freigabe. Der vollständige Builder und die strenge Gesamtvalidierung bleiben durch 463 fehlende Kommentare außerhalb des Auftrags gesperrt; Kapitel 13 und 14 werden als überprüfbarer Teilstand erzeugt. Dies schließt nur den begrenzten Prüfauftrag ab.

Autorenkontrolle §§ 264–266 am 21. Oktober 2026: alle sieben Kommentare mit dem amtlichen Wortlaut abgeglichen; Absätze, Befreiungsalternativen, Bilanzhierarchie und fiktive Beispiele geprüft. [Ergebnis](author-p264-p266-result.json). Dies ist keine unabhängige Zweitprüfung.


## Begrenzter zweiter Durchgang: §§ 252–266, 21. Oktober 2026

Genau die 20 beauftragten Einheiten einschließlich §§ 256a, 264a–264d und der Leerstelle § 262 sind am amtlichen XML vollständig gelesen. [Exakte reviewed_ids und Einzelbefunde](review-p252-p266.json). Acht Kommentare wurden präzisiert: § 252 zum Kenntniszeitraum, § 253 zu Zeitwertbewertung, Rentenverbindlichkeiten und Ausschüttungsdeckung, § 254 zur Rückstellungsausnahme, § 255 zu Kostenbestandteilen und letzter Zeitwertbasis, § 257 zu Reproduktionsformen, § 264 zu Erklärung, Einstand und Offenlegungsbedingungen, § 264c zur Eigenkapitalgliederung und Steuerkorrektur, § 265 zur arabischen Gliederungsebene. Die übrigen zwölf bleiben nach inhaltlicher Prüfung erhalten.

Erneuter amtlicher Abruf: HTTP 200, gültiges ZIP/XML, unveränderte Prüfsumme. Inkrafttretensnachweis Artikel 64 BGBl. 2026 I Nr. 33 und Intake-Vergleich geprüft; spätere Änderungen 2028/2030 nicht vorgezogen. Alle 696 Kennungen und Normtexte stimmen überein, alle 814 XML-Knoten sind zugeordnet. Keine historische Dublette, ausgelassene operative Eingangsformel oder eigenständige Anlage; § 262 bleibt ausdrücklich erhalten.

Der amtliche gesicherte Volltext OLG Köln 28 Wx 21/22 wurde vollständig erneut gelesen; Rn. 22–33 tragen die Aussage zu § 264b. Die Altfassung und Grenzen sind in der Fallkarte dargestellt. Selektive vorhandene Recherche, keine umfassende neue Rechtsprechungssuche. Längere Absätze sind innerhalb der Gruppe nicht identisch; dies und Mindestlängen ersetzen keine juristische Prüfung. Keine externe anwaltliche Freigabe. Der Standardbuilder stoppt wegen 456 fehlender Kommentare außerhalb der Gruppe. Kapitel 14, 15 und das vorhandene Teilkapitel 16 werden deshalb separat aus unveränderten Normdaten und geprüften Kommentaren erzeugt. Keine Gesamtfertigstellung.

Autorenkontrolle der Charge §§ 267–288 am 21. Oktober 2026: alle 20 zugewiesenen Einheiten gegen den amtlichen Wortlaut gelesen; Grenzen, Absätze, Verweise, weggefallene Stellen, Beispiele und Checklisten kontrolliert. Besonders § 285 vollständig nach Nummern sowie die verbleibenden Pflichten des § 288 behandelt. [Technischer Chargenbefund](author-p267-p288-result.json). Dies ist eine Autorenkontrolle, keine unabhängige Zweitprüfung. Das Gesamtbuch bleibt unvollständig.

## Begrenzte unabhängige Zweitprüfung §§ 267–288 — 21. Oktober 2026

Alle genau 20 beauftragten Einheiten einschließlich Buchstabenparagraphen und Sammelleerstelle §§ 279 bis 283 wurden mit dem amtlichen Volltext gelesen und materiell geprüft. Sechs Kommentare wurden präzisiert: § 267 (Bezugszeiträume), § 268 (Haftungsverhältnisse), § 272 (Rücklagenbildung und -auflösung), § 276 (Zwischensaldo ohne Doppelzählung), § 285 (Einzelpflichten und Konzernhonorarausnahme), § 286 (Nachteile des anderen Unternehmens). Die anderen 14 Einheiten wurden unverändert bestätigt. Die amtliche Entscheidung BGH Xa ZR 175/07 wurde vollständig erneut gelesen; ihre historische Prüfungsvertragsfrage bleibt von der aktuellen systematischen Anhangfunktion getrennt.

[Einzelbefunde mit exakten reviewed_ids](review-p267-p288.json), [vollständiger XML-Abgleich](review-p267-p288-coverage.json), [amtlicher Wiederabruf](sources/review-p267-p288-fetch.json), [Gesamtvalidierung](review-p267-p288-validation.json). Der Gesamtbuilder bricht wegen 436 noch fehlender Kommentare außerhalb der Charge ab; die betroffenen Kapitel wurden deshalb aus unverändertem Normtext und geprüften Kommentaren erneut gerendert. Diese Zweitprüfung gilt allein dieser Charge; keine externe anwaltliche Freigabe und keine Gesamtbuchfertigstellung.

## Begrenzte unabhängige Zweitprüfung §§ 289–301 — 21. Oktober 2026

Genau 20 zugewiesene Einheiten einschließlich §§ 289a–289f, 292a und 295 wurden jeweils gegen den amtlichen Wortlaut auf Voraussetzungen, Folgen, Absatzunterschiede, Querverweise, Beispiele und Wiederholungen geprüft. Vier Kommentare sind präzisiert: § 289a (Kenntnisvorbehalt und Doppelangaben), § 289c (Wahrscheinlichkeits- und Schweregrenze der Risiken), § 290 (Sicherungsrechte eines Kreditinstituts) und § 291 (Vermerk über die Versagung der Bestätigung). Die übrigen 16 Einheiten wurden unverändert bestätigt. Die zitierte BAG-Entscheidung 3 AZR 505/21 wurde erneut vollständig gelesen; ihr betriebsrentenrechtlicher Kontext begrenzt die Verwendung zu § 289.

[Einzelbefunde und exakte reviewed_ids](review-p289-p301.json), [Kennungs- und Wortlautprüfung](review-p289-p301-coverage.json), [amtlicher Wiederabruf](sources/review-p289-p301-fetch.json), [Gesamtbuild](review-p289-p301-build.txt), [Gesamtvalidierung](review-p289-p301-validation.json). Der Gesamtbuild scheitert an 416 fehlenden Kommentaren ab § 302 außerhalb dieser Charge. Das geprüfte Teilkapitel wurde mit der gemeinsamen Zitierfunktion aus den unveränderten Normtexten erneut gerendert. Keine Gesamtbuchfertigstellung und keine externe anwaltliche Freigabe.
