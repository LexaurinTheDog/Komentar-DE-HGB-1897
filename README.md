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

Autorencheckpoint §§ 346–364: 20 neue Einheiten, Gesamtstand 420/696; 276 Kommentare ab § 365 offen. [Chargenbericht](author-p346-p364-result.json), [Teilkapitel](25-hgb-teil-p346-p364.md). Unveränderter amtlicher Wiederabruf vom 21. Oktober 2026, Titelstichtag 19. Oktober 2026. Zweitprüfung der Charge ausstehend; Gesamtbuch unvollständig.

Zweitprüfung vom 21. Oktober 2026, ausschließlich §§ 346–364 einschließlich § 354a: alle 20 zugewiesenen Einheiten gegen amtlichen Wortlaut geprüft. Präzisierungen zu Handelsbräuchen (§ 346), Übergabe und Legitimation (§ 364). BGH VI ZR 121/17 vollständig erneut gelesen. [Einzelergebnisse](review-p346-p364.json), [Abdeckung](review-p346-p364-coverage.json), [Chargenvalidierung](review-p346-p364-bounded-validation.json). 100 % Wortlautübereinstimmung für die Charge; Gesamtbuch wegen 276 fehlender Kommentare außerhalb des Auftrags unvollständig. Keine externe fachliche Freigabe.

Zweitprüfung vom 21. Oktober 2026, ausschließlich §§ 365–383 einschließlich § 365a: alle 20 zugewiesenen Einheiten gegen amtlichen Wortlaut geprüft. Präzisierungen zu Indossament und Gutglaubensschutz (§§ 365–367), Fristbeginn (§ 368), Schuldnerschutz (§ 371) und Versteigerungsinformationen (§ 373). BGH VIII ZR 246/16 vollständig erneut gelesen. [Einzelergebnisse](review-p365-p383.json), [Abdeckung](review-p365-p383-coverage.json), [Chargenvalidierung](review-p365-p383-bounded-validation.json). 100 % Wortlautübereinstimmung der Charge. Gesamtbuch bleibt wegen 256 fehlender Kommentare außerhalb des Auftrags unvollständig. Keine externe fachliche Freigabe.

## Begrenzte Zweitprüfung §§ 384–403, 21. Oktober 2026

Alle 20 zugewiesenen Einheiten einzeln gegen amtlichen Wortlaut geprüft. § 384 zur eigenständigen Kundenstammherausgabe und § 400 zu Kursarten und amtlicher Preisgrenze präzisiert. BGH I ZR 229/15 erneut im Volltext gelesen; historische Entscheidung nicht als umfassende aktuelle Rechtsprechung ausgegeben. [Einzelergebnisse](review-p384-p403.json), [Abdeckung](review-p384-p403-coverage.json), [Validierung der Charge](review-p384-p403-bounded-validation.json). Der Chargenneubau gelingt, der Wortlaut stimmt zu 100 % überein. Das Gesamtbuch bleibt wegen 236 fehlender Kommentare außerhalb dieser Charge unvollständig. Keine externe fachliche Freigabe.

Autorencheckpoint §§ 404–423: 20 spezifische Kommentare; 480/696 Einheiten vorhanden. [Chargenbericht](author-p404-p423-result.json). Teilbuild erfolgreich, Gesamtbuch unvollständig; unabhängige Zweitprüfung ausstehend. Titelstichtag 19. Oktober 2026; amtlicher Wiederabruf unverändert.

## Begrenzte Zweitprüfung §§ 404–423, 21. Oktober 2026

Alle 20 zugewiesenen Einheiten einzeln gegen den amtlichen Wortlaut geprüft. § 410 zum Haftungsausschluss für zulässige Gefahrgutmaßnahmen präzisiert; praktische Prüfliste zur Abwicklung nach §§ 407–423 ergänzt. Amtlicher BGH I ZR 37/09 erneut vollständig gelesen. [Einzelergebnisse](review-p404-p423.json), [Abdeckung](review-p404-p423-coverage.json), [Teilvalidierung](review-p404-p423-bounded-validation.json). Teilbuild erfolgreich; 100 % Wortlautübereinstimmung. Gesamtbuch wegen 216 fehlender Kommentare außerhalb des Auftrags unvollständig. Keine externe fachliche Freigabe.

Autorencheckpoint §§ 424–443: 20 spezifische Kommentare; 500/696 Einheiten vorhanden. [Chargenbericht](author-p424-p443-result.json). Teilbuild erfolgreich, Gesamtbuch unvollständig; unabhängige Zweitprüfung ausstehend. Titelstichtag 19. Oktober 2026; amtlicher Wiederabruf unverändert.

## Begrenzte Zweitprüfung §§ 424–443, 21. Oktober 2026

Alle 20 zugewiesenen Einheiten einzeln gegen den amtlichen Wortlaut geprüft. § 434 zur gewichtsbezogenen Grenze und Reichweite der Rückausnahme, § 435 zum Umfang des Privilegienwegfalls und § 439 zu Anspruchsbereich, Verjährungshemmung und Zugang präzisiert. Amtlicher BGH I ZR 75/11 erneut vollständig gelesen; seine frühere Schriftformprämisse wird nicht auf die heutige Textform übertragen. [Einzelergebnisse](review-p424-p443.json), [Abdeckung](review-p424-p443-coverage.json), [Teilvalidierung](review-p424-p443-bounded-validation.json). Teilbuild erfolgreich, 100 % Wortlautübereinstimmung. Gesamtbuch wegen 196 fehlender Kommentare außerhalb dieses Auftrags unvollständig. Keine externe fachliche Freigabe.

Autorencheckpoint §§ 444–452c: genau 20 spezifische Kommentare einschließlich § 451c als Leerstelle. [Chargenbericht](author-p444-p452c-result.json), [Abdeckung](author-p444-p452c-coverage.json), Teilkapitel [§§ 444–451e](30-hgb-teil-p444-p451e.md) und [§§ 451f–452c](31-hgb-teil-p451f-p452c.md) im Ausgabeverzeichnis. Begrenzter Teilbuild und strenge Chargenvalidierung erfolgreich, 100 % Wortlautübereinstimmung. Gesamtbuch unvollständig; unabhängige Zweitprüfung ausstehend.

## Begrenzte Zweitprüfung §§ 444–452c, 21. Oktober 2026

Alle 20 zugewiesenen Einheiten einschließlich der weggefallenen Nummer § 451c einzeln gegen amtlichen Wortlaut geprüft. Gewichtsbezug in § 449, Widerleglichkeit in § 451d, Anzeigeform in § 451f, Informationszeitpunkt in § 451g und Schadensortbeispiel in § 452a präzisiert. BGH I ZR 128/15 vollständig erneut gelesen; alte Seefrachtgrenzen und ADSp 2003 nicht als heutiges Recht übernommen. [Einzelergebnisse](review-p444-p452c.json), [Abdeckung](review-p444-p452c-coverage.json), [Teilvalidierung](review-p444-p452c-bounded-validation.json). Teilbuild erfolgreich, 100 % Wortlautübereinstimmung. Gesamtbuch wegen 176 fehlender Kommentare außerhalb des Auftrags weiter unvollständig. Keine externe fachliche Freigabe.

## Autorencharge §§ 452d–471, 21. Oktober 2026

20 von 20 zugewiesenen Einheiten ausgearbeitet; Rechtsstand zum Titelbeginn 19. Oktober 2026, amtlicher Wiederabruf bytegleich. [Quellenprüfung](sources/verification-p452d-p471.json), [Abdeckung](author-p452d-p471-coverage.json), [Fallkarte BGH I ZR 150/10](cases/bgh-I-ZR-150-10-p454-p461.md). Selektive Rechtsprechung, keine erschöpfende Übersicht. Teilbuild und strenge Teilvalidierung; Gesamtband mit 156 noch fehlenden Kommentaren unvollständig. Unabhängige Zweitprüfung dieser Charge steht aus. Originalkommentar © 2026 Vojtěch Říha, Apache-2.0.

## Begrenzte Zweitprüfung §§ 452d–471, 21. Oktober 2026

Alle 20 zugewiesenen Vorschriften einzeln am amtlichen Wortlaut geprüft; Zuordnung des Erlangten (§ 457), Abgrenzung der Obhutshaftung (§ 461), wiederholte Anspruchserklärung (§ 463) und Lagerscheinadressat (§ 471) präzisiert. BGH I ZR 150/10 vollständig erneut gelesen; historische ADSp und Kollisionsregeln nicht als heutiges Recht übernommen. [Einzelergebnisse](review-p452d-p471.json), [Abdeckung](review-p452d-p471-coverage.json), [Teilvalidierung](review-p452d-p471-bounded-validation.json). Gesamtband wegen 156 außerhalb der Charge fehlender Kommentare unvollständig; frühere Aussage zur ausstehenden Zweitprüfung dieser Charge ist durch diesen Prüfstand überholt. Keine externe fachliche Freigabe.

Autorencharge §§ 472–483: genau 20 zusätzliche Einheiten. [Teilstandsübersicht](README-p472-p483.md), [Ergebnis](author-p472-p483-result.json), [Quellen](batch-p472-p483-SOURCES.md). 560 von 696 Einheiten sind nun kommentiert; 136 ab § 484 bleiben offen. Der Teilstandsbuild und die strenge Teilstandsvalidierung sind erfolgreich, Wortlautübereinstimmung 100 %. Keine unabhängige Zweitprüfung dieser Charge.

## Begrenzte Zweitprüfung §§ 472–483, 21. Oktober 2026

Genau 20 zugewiesene Vorschriften am amtlichen Wortlaut geprüft. Fristbeginn (§ 475a), Gefahrgutbezeichnung (§ 475c), Vertretungsrolle (§ 479) und Verweisung auf § 509 Absatz 5 (§ 480) präzisiert. BGH I ZR 146/17 einschließlich Berichtigung vollständig gelesen; Vorsatzbehauptung und gerichtliche Feststellung getrennt. [Einzelergebnisse](review-p472-p483.json), [Abdeckung](review-p472-p483-coverage.json), [Teilvalidierung](review-p472-p483-bounded-validation.json). Frühere Hinweise auf die noch ausstehende Zweitprüfung dieser Charge sind durch diesen Prüfstand überholt. Gesamtband weiterhin unvollständig; keine externe fachliche Freigabe.

Autorencharge §§ 484–503: genau 20 weitere Vorschriften ausgearbeitet. [Teilstandsübersicht](README-p484-p503.md), [Kapitel](35-hgb-teil-p484-p503.md), [Quellen](batch-p484-p503-SOURCES.md), [Autorenkontrolle](batch-p484-p503-REVIEW.md). Nun 580 von 696 Einheiten kommentiert; 116 ab § 504 fehlen weiterhin. Wortlaut und vollständiges XML-Inventar geprüft; keine Gesamtfertigstellung und keine unabhängige Zweitprüfung dieser Charge.

## Begrenzte Zweitprüfung §§ 484–503, 21. Oktober 2026

Alle 20 zugewiesenen Vorschriften einzeln am amtlichen Wortlaut geprüft. Aufwendungsmaßstab (§ 493), Eigentümergruppen (§ 495) und neun besondere Schadensursachen (§ 499) präzisiert. BGH I ZR 181/08 vollständig erneut gelesen; historische Vorschriften und geltendes Deckladungsrecht getrennt. [Einzelergebnisse](review-p484-p503.json), [Abdeckung](review-p484-p503-coverage.json), [Teilvalidierung](review-p484-p503-bounded-validation.json). Frühere Aussage zur ausstehenden Zweitprüfung dieser Charge wird durch diesen Stand ersetzt. Gesamtband weiterhin unvollständig: 580 von 696 Einheiten kommentiert, 116 außerhalb dieser Charge fehlen. Frühere Gesamtzahlen in den chronologischen Chargenvermerken geben frühere Arbeitsstände wieder. Keine externe fachliche Freigabe.

## Begrenzte Zweitprüfung §§ 504–523, 21. Oktober 2026

Alle 20 zugewiesenen Vorschriften einzeln am erneut abgerufenen amtlichen XML geprüft. Die Stück-/Gewichtsgrenzen (§ 504), Haftungserweiterungen auch gegenüber dem Empfänger (§ 509) und Zeichnungsvoraussetzungen der Reederhaftung (§ 523) wurden präzisiert; Dokumentenprüfliste ergänzt. BGH I ZR 181/08 vollständig erneut gelesen und ausschließlich historisch eingeordnet. [Einzelergebnisse](review-p504-p523.json), [Abdeckung](review-p504-p523-coverage.json), [Teilvalidierung](review-p504-p523-bounded-validation.json). Die bisher ausstehende Zweitprüfung dieser Charge ist damit durchgeführt. Gesamtband weiterhin unvollständig; keine externe fachliche Freigabe. Frühere Chargenvermerke enthalten damalige Arbeitsstände.

## Autorencharge §§ 524–543 (21. Oktober 2026)

20 Vorschriften spezifisch erläutert; [Teilmanuskript und Quellen](README-p524-p543.md), [Abdeckung](author-p524-p543-coverage.json), [Teilvalidierung](author-p524-p543-bounded-validation.json). Amtlicher Wiederabruf bytegleich mit dem zum Titelbeginn geprüften XML. Selektive Recherche ohne zitierfähigen verifizierten Entscheidungs-Volltext für diese Charge; keine Rechtsprechungsholdings behauptet. Unabhängige Zweitprüfung dieser Charge ausstehend. Gesamtband weiterhin unvollständig.

## Begrenzte Zweitprüfung §§ 524–543, 21. Oktober 2026

Alle 20 zugewiesenen Einheiten einzeln am erneut abgerufenen amtlichen XML geprüft. Unterzeichnungspflicht (§ 526), Ausnahmen der verschuldensunabhängigen Haftung (§ 538), Gefahrenkatalog (§ 541) und dokumentenrechtliche Freizeichnung (§ 525) präzisiert. Keine ungesicherte Gerichtsentscheidung angeführt. [Einzelprüfung](review-p524-p543.json), [Abdeckung](review-p524-p543-coverage.json), [Teilvalidierung](review-p524-p543-bounded-validation.json), [Quellenabruf](sources/review-p524-p543-fetch.json). Die zuvor ausstehende Zweitprüfung dieser Charge ist durchgeführt. Gesamtband weiterhin in Bearbeitung, keine externe fachliche Freigabe. Frühere Vermerke geben damalige Arbeitsstände wieder. Originalkommentar © 2026 Vojtěch Říha.

## Autorencharge §§ 564–583

20 Vorschriften individuell kommentiert; [Teilmanuskript und Quellen](README-p564-p583.md), [Abdeckung](author-p564-p583-coverage.json), [Autorendurchsicht](REVIEW-p564-p583.md). Gesamtband weiterhin in Bearbeitung; unabhängige Zweitprüfung der Charge ausstehend.

## Begrenzte Zweitprüfung §§ 564–583, 21. Oktober 2026

Alle 20 zugewiesenen Vorschriften einzeln gegen erneut abgerufenes amtliches XML geprüft. Umweltdefinition (§ 575), sämtliche Bemessungskriterien (§ 577) und Berechnungsbasis sowie alternative Zuschlagsgrenzen (§ 578) präzisiert. [Einzelprüfung](review-p564-p583.json), [Abdeckung](review-p564-p583-coverage.json), [Teilvalidierung](review-p564-p583-bounded-validation.json), [Quellenabruf](sources/review-p564-p583-fetch.json). Frühere Vermerke über die ausstehende Zweitprüfung dieser Charge geben den damaligen Stand wieder. Gesamtband weiter in Bearbeitung. Keine externe fachliche Freigabe; selektive Recherche ohne hier angeführte Gerichtsentscheidung. Originalkommentar © 2026 Vojtěch Říha.
