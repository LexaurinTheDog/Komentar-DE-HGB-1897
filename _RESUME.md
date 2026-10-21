# Fortsetzungsstand

Stichtag: 19. Oktober 2026. Die Originalzuweisung bleibt das gesamte HGB mit 696 Normeinheiten. 233 Kommentare zu §§ 1–263 sind geschrieben und gesichert. Nächste Einheit: `p264`. Ab dort fehlen 463 Kommentare; kein abgeschlossenes Manuskript und keine unabhängige Zweitprüfung.

Der amtliche XML-Bestand liegt in `sources/hgb-2026-10-19.xml`, direkt im Quellenwurzelverzeichnis. `_parse.py` erzeugt alle Einheiten und die vollständige Gesamtgliederung. Nicht auf den bereits kommentierten Umfang verkürzen. `_audit.py` prüft unabhängig XML-Textbestand und HTML-Inventar sowie die tatsächlich vorhandene Kommentierung. `_export_checkpoint.py` exportiert nur vollständig kommentierte Kapitel und bezeichnet das Projekt ausdrücklich als unvollständig. Er ersetzt den gemeinsamen Vollständigkeits-Build nicht.

Die 15 ausgegebenen Kapitel entsprechen den vollständig kommentierten ersten beiden Büchern und dem ersten Abschnitt des dritten Buchs. Der gemeinsame Builder schlägt wegen 463 fehlender Kommentare fehl. `validation.json` ist korrekt negativ bei einer Wortlautquote von 1,0. Diese Schranke darf nicht durch verkleinerte Einheitenlisten, Platzhalter oder gemeinsame Absatzvorlagen umgangen werden.

Drei amtliche Entscheidungen sind in Fallkarten und Rohdateien gesichert. § 75 Absatz 3 ist trotz Abdruck nicht wörtlich anwendbar; der Kommentar erläutert dies mit BAG 10 AZR 260/14. Änderungen nach Artikel 64 des Standortfördergesetzes für 2028 und 2030 nicht vorziehen. Aktuelle OHG-Nummerierung beachten; persönliche Haftung heute § 126, alte §§ 153–160 als Sammelleerstelle.

Weiterarbeit in selbst geschriebenen Batches von 10–20 Einheiten, jeweils nach Lesen des tatsächlichen Gesetzestexts, mit konkreten Beispielen und relevanten verifizierten Autoritäten. Vorhandene Erläuterungen nicht durch generische Kurztexte ersetzen. Nach tatsächlicher Vollständigkeit regulären `build_repo.py WORK` und strengen `validate.py WORK` ausführen, unterstützende Quellen in OUTPUT nachführen, lokal committen und erst dann den tatsächlichen Abschlussstatus setzen. Kein Push, keine Veröffentlichung und keine Kommunikation nach außen.
