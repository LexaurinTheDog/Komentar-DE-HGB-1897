# Kommentar zum Handelsgesetzbuch

**Unvollständiger Arbeitsentwurf vom 19. Oktober 2026.** Ausgearbeitet sind 360 von 696 amtlichen Normeinheiten: das gesamte Erste und Zweite Buch sowie der Erste Abschnitt des Dritten Buchs, §§ 1–263 einschließlich der amtlichen Sammelleerstellen. Zusätzlich sind §§ 264–341g kommentiert; ab § 341h fehlen noch 336 Kommentare. Dieser Teilstand ist kein fertiges Gesamtmanuskript.

Gegenstand des Gesamtprojekts ist das gesamte Handelsgesetzbuch vom 10. Mai 1897 (RGBl. S. 219), mit allen fünf Büchern, erhaltenen leeren und weggefallenen Stellen. Die 696 Normeinheiten und 117 Gliederungsknoten sind vollständig aus amtlichem XML extrahiert; die Intake-Zahl 813 zählt beide Kategorien zusammen. Gruppen wie §§ 180–229 bleiben als amtliche Sammelstelle erhalten und werden nicht als fünfzig gegenwärtig operative Vorschriften ausgegeben. Das EGHGB ist ein gesondertes Gesetz und wird nicht in das HGB eingemischt.

Der lesbare Teilstand enthält vollständige Kommentarkapitel und Teilkapitel bis § 341g. Die Gesamtgliederung sieht 44 Kapitel vor. [INDEX](INDEX.md) und [Einleitung](00-einleitung.md) erschließen den vorhandenen Text. [Bearbeitungsstatus](status.json), [Autorenkontrolle](REVIEW.md) und [Quellennachweise](SOURCES.md) zeigen die Grenzen.

## Gesetzesstand und Quellen

Maßgeblicher Stichtag ist der 19. Oktober 2026. An diesem Tag wurden das [amtliche HGB-XML](https://www.gesetze-im-internet.de/hgb/xml.zip), der [amtliche Volltext](https://www.gesetze-im-internet.de/hgb/BJNR002190897.html) und das [Inhaltsverzeichnis](https://www.gesetze-im-internet.de/hgb/) erneut erfolgreich abgerufen. Standvermerk: zuletzt geändert durch Artikel 4 des Gesetzes vom 4. Februar 2026 (BGBl. 2026 I Nr. 33), mit berücksichtigter mittelbarer Änderung nach Artikel 59 Nummer 1. XML-Build: 9. Juli 2026, Kennung `20260709215513`.

Der Standvermerk allein belegt keine bereits eingetretene Wirksamkeit jeder Änderung. Das verkündete Standortfördergesetz wurde zusätzlich anhand des amtlichen PDFs und seiner Inkrafttretensregel geprüft. Die 2026 wirksamen Änderungen werden von den erst 2028 beziehungsweise 2030 wirksamen Fassungen getrennt; siehe [Inkrafttreten](sources/commencement.md). Der erneut abgerufene Wortlaut stimmt nach Leerraumnormalisierung mit dem erhaltenen Intake vom 1. Oktober 2026 überein. [verification.json](sources/verification.json) enthält Abrufzeiten, HTTP-Ergebnisse, Formatprüfungen und SHA-256; [change-map.json](sources/change-map.json) dokumentiert den Vergleich.

## Methode und Prüfstand

Der Gesetzeswortlaut wird mechanisch aus amtlichem XML übernommen; `_parse.py` ist im Arbeitsverzeichnis erhalten. Listen, Absätze, Buchstaben und redaktionelle Quellenhinweise bleiben unterscheidbar. Die vollständige [kanonische Transkription](sources/hgb-canonical.md) ist Quellenmaterial und keine Behauptung vollständiger Kommentierung.

Die vorhandenen Erläuterungen sind eigenständige deutsche Texte mit konkreten Tatbestandsunterscheidungen, systematischen Bezügen, fiktiven Beispielen und praktischen Prüflisten. Verifizierte Rechtsprechung wird selektiv verwendet, nicht als erschöpfende Rechtsprechungsübersicht. Die [Fallkarten](cases/INDEX.md) dokumentieren vollständige amtliche Entscheidungen, tragende Randnummern und Grenzen. Besonders § 75 Absatz 3 zeigt, warum der Abdruck eines Gesetzestexts nicht dessen unbesehene Anwendbarkeit beweist.

Die Quellenabdeckung beträgt 696/696 ohne fehlende oder doppelte Kennung. Der Wortlaut stimmt zu 100 % mit der kanonischen Quelle und auf Zeichenebene ohne Leerraum mit dem amtlichen XML überein. Diese technischen Befunde beweisen weder die Vollständigkeit der Kommentierung noch juristische Fehlerfreiheit. Der gemeinsame Vollständigkeits-Build und die strenge Gesamtvalidierung bleiben wegen der 336 fehlenden Kommentare erfolglos. Die bisherigen begrenzten Zweitprüfungen sind in REVIEW.md dokumentiert; für die neue Charge §§ 340d–341g steht sie aus. Es gibt keine externe fachliche Freigabe.

## Rechte und Nutzung

Eigenständiger Kommentartext © 2026 Vojtěch Říha. Für die originären Erläuterungen gilt die [Apache License 2.0](LICENSE). Amtliche Gesetzes- und Entscheidungstexte, amtliche Metadaten sowie als solche gekennzeichnete fremde Quellenbestandteile werden nicht als eigene originäre Kommentarleistung beansprucht; ihre jeweilige rechtliche Behandlung wird durch diese Lizenz nicht umdefiniert. Kommerzielle Kommentierungen wurden nicht übernommen.

Der Entwurf wird im vorhandenen Bearbeitungsstand bereitgestellt und ersetzt keine Prüfung eines konkreten Mandats. Projektprofil: [LexaurinTheDog](https://github.com/LexaurinTheDog). Keine Veröffentlichung, kein Push und keine externe Übermittlung wurden vorgenommen.

Quellen- und Parsernachprüfung vom 21. Oktober 2026: Die amtlichen Wiederabrufe sind mit dem Bestand vom 19. Oktober identisch. Sieben Sammelleerstellen tragen jetzt ihre exakte amtliche Bezeichnung einschließlich `(XXXX)`. [Preflight-Ergebnis](preflight-result.json) und [Knotenabdeckung](sources/preflight-coverage.json) dokumentieren auch Kopfnorm, Rechnungslegungsanhang und fehlende eigene Gesetzesanlagen. Der Bearbeitungsstichtag bleibt unverändert.

Neuer Teilstand vom 21. Oktober 2026: [§§ 264–266](16-hgb-16-teil-p264-p266.md), sieben zusätzliche Kommentare; [Chargenprüfung](author-p264-p266-result.json).

Charge §§ 267–288 vom 21. Oktober 2026: 20 zusätzliche Kommentare in [part-15](commentary/part-15.md); [Chargenprüfung](author-p267-p288-result.json). Kapitel 16 ist damit vollständig, Kapitel 17 nur bis § 288 ausgearbeitet.

Charge §§ 289–301 vom 21. Oktober 2026: genau 20 weitere Normeinheiten einschließlich §§ 289a–289f und der weggefallenen §§ 292a und 295. [Chargenprüfung](author-p289-p301-result.json). Ab § 316 bleiben 396 Kommentare offen.

Charge §§ 302–315e vom 21. Oktober 2026: 20 weitere Normeinheiten; [Chargenprüfung](author-p302-p315e-result.json). 300/696 Einheiten sind kommentiert; 396 ab § 316 bleiben offen. Die unabhängige Zweitprüfung dieser Charge ist dokumentiert in review-p316-p328.json.

Begrenzte unabhängige Zweitprüfung §§ 302–315e abgeschlossen: [Einzelbefunde](review-p302-p315e.json), [Prüfbericht](REVIEW.md). Nur diese 20 Einheiten; Gesamtbuch weiterhin unvollständig.

Charge §§ 316–328 vom 21. Oktober 2026: 20 weitere Normeinheiten; [Chargenprüfung](author-p316-p328-result.json). 320/696 Einheiten sind kommentiert; 376 ab § 329 bleiben offen. Die unabhängige Zweitprüfung dieser Charge ist dokumentiert in review-p316-p328.json.

Begrenzte unabhängige Zweitprüfung §§ 316–328: [20 Einzelbefunde](review-p316-p328.json), [Prüfbericht](REVIEW.md). Gesamtbuch weiterhin unvollständig.

Charge §§ 329–340c: genau 20 weitere Normeinheiten; [Chargenprüfung](author-p329-p340c-result.json). Aktueller Gesamtstand 340/696; 356 Kommentare ab § 340d fehlen. Unabhängige Zweitprüfung dieser Charge: review-p329-p340c.json.

Begrenzte unabhängige Zweitprüfung §§ 329–340c: [20 Einzelbefunde](review-p329-p340c.json), [Prüfbericht](REVIEW.md). Gesamtbuch weiterhin unvollständig.

Aktueller Autorencheckpoint §§ 340d–341g: genau 20 neue Normeinheiten; [Chargenprüfung](author-p340d-p341g-result.json). Gesamtstand 360/696, 336 Kommentare ab § 341h offen. Zweitprüfung dieser Charge ausstehend. Ältere Zahlen in den nachstehenden beziehungsweise vorangehenden Chargennotizen dokumentieren frühere Zwischenstände.

Autorencheckpoint §§ 341h–342a: 20 neue Normeinheiten, Gesamtstand 380/696; 316 Kommentare ab § 342b offen. [Chargenbericht](author-p341h-p342a-result.json), [Teilkapitel](22-hgb-teil-p341h-p342a.md). Titelstichtag weiterhin 19. Oktober 2026, amtlicher Wiederabruf vom 21. Oktober unverändert. Zweitprüfung dieser Charge ausstehend; Gesamtbuch nicht abgeschlossen.

Zweitprüfung vom 21. Oktober 2026, ausschließlich §§ 341h–342a: 20/20 Einheiten anhand des amtlichen XML geprüft. Drei Präzisierungen zu Hauptversammlung, Größenprüfung und Stimmrechtsvoraussetzung vorgenommen. [Einzelergebnisse](review-p341h-p342a.json), [Abdeckungsnachweis](review-p341h-p342a-coverage.json). Kein Abschluss des Gesamtbuchs; 316 Kommentare außerhalb dieses Prüfauftrags fehlen weiterhin.

Autorencheckpoint §§ 342b–345: 20 neue Normeinheiten, Gesamtstand 400/696; 296 Kommentare ab § 346 offen. [Chargenbericht](author-p342b-p345-result.json), [Teilkapitel](22-hgb-teil-p342b-p345.md). Amtlicher XML-Wiederabruf vom 21. Oktober unverändert zum Titelstichtag 19. Oktober 2026. Unabhängige Zweitprüfung dieser Charge ausstehend; Gesamtbuch nicht abgeschlossen.

Zweitprüfung vom 21. Oktober 2026, ausschließlich §§ 342b–345: alle 20 zugewiesenen Einheiten gegen amtlichen Wortlaut geprüft. Vier Präzisierungen zu branchenspezifischen Umsatzgrößen und Offenlegungsbefreiungen in §§ 342b, 342d–342f. [Einzelergebnisse](review-p342b-p345.json), [Abdeckung](review-p342b-p345-coverage.json). BGH VI ZR 121/17 vollständig erneut gelesen; selektive Rechtsprechungsprüfung. Kein Gesamtbuchabschluss und keine externe fachliche Freigabe; 296 Kommentare außerhalb dieser Charge fehlen.
