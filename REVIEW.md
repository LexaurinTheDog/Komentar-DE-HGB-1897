# Autorenkontrolle — kein unabhängiges Zweitgutachten

Stand: 19. Oktober 2026. Dieser Bericht dokumentiert die eigene Arbeitskontrolle des Entwurfs. Eine unabhängige zweite Prüfung durch einen frischen Prozess hat nicht stattgefunden. Es liegt keine externe anwaltliche Freigabe vor.

## Gesicherte technische Befunde

- Amtliches HGB-XML und HTML-Inhaltsverzeichnis enthalten dieselben 696 Normkennungen; kein fehlender oder doppelter Eintrag im Parsergebnis.
- 117 Gliederungsknoten sind von Vorschriften getrennt; amtliche Sammelleerstellen und interne Wegfallmarker bleiben erhalten. Keine eigene Anlage im amtlichen HGB-XML.
- Sämtlicher extrahierter Gesetzestext stimmt ohne Leerraum mit dem XML überein. Die strenge Wortlautprüfung gegen die kanonische Quelle ergibt 100 Prozent. Gegenüber dem erhaltenen Intake besteht nach Leerraumnormalisierung keine Textabweichung.
- 233 Kommentare mit 290.299 Zeichen sind vorhanden. Es gibt keine doppelte Kommentarzuordnung, keinen unbekannten Einheitenbezeichner, keinen zu kurzen vorhandenen Kommentar nach den technischen Mindestgrenzen und keinen exakt identischen wiederholten längeren Prosaabsatz.

Die Berichte [audit-report.json](audit-report.json) und [completeness-report.json](completeness-report.json) enthalten Einzelkennungen und Quellenhashes. Die Längen- und Wiederholungsprüfung beweist keine rechtliche Qualität und erkennt nicht jede semantische Ähnlichkeit.

## Sachliche Kontrollpunkte

Zeitliche Fassungen wurden anhand des Standortfördergesetzes getrennt. Die aktuelle OHG-Nummerierung ist zugrunde gelegt; alte Nummern werden nicht unbesehen fortgeschrieben. Die amtlich noch abgedruckte Regel des § 75 Absatz 3 wird im Kommentar anhand des vollständig gelesenen BAG-Urteils als nicht anwendbar erläutert. Firmen- und Etablissementbezeichnung sowie interne Geschäftsführung und Außenvertretung werden getrennt behandelt. Die drei aufgenommenen Fallkarten begrenzen ihre Aussagen auf tatsächlich gelesene Entscheidungsinhalte.

## Offene Arbeit

463 Kommentare ab § 264 fehlen. Der gemeinsame Builder lehnt das Gesamtmanuskript deshalb ab; die strenge Gesamtvalidierung ist negativ. Ein lesbarer Export der 15 bereits vollständig kommentierten Kapitel ist ein ausdrücklich gekennzeichneter Teilstand und keine Verengung der Gesamtzuweisung. [Build-Ergebnis](build-result.json), [Validierung](validation.json) und [Status](status.json) bleiben zugänglich.

Die rechtliche Qualität jedes später hinzukommenden Abschnitts, zusätzliche einschlägige Rechtsprechung, externe Querverweise und eine unabhängige Durchsicht des gesamten fertigen Manuskripts stehen weiter aus. Es wird kein Abschlussstatus `drafted_technical_validation` vergeben.
