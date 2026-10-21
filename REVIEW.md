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
