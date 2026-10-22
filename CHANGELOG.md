# Changelog

Änderungen am OCB.GG Obsidian Glass Theme für TeamSpeak 3.
Alle nachfolgenden Beta-Versionen wurden am 22. Oktober 2026 veröffentlicht.

## 1.0.0-beta.7

- Bigcircle-Logo im Infobereich als dezentes Wasserzeichen unten rechts: 44 × 44 Pixel, 24 % Deckkraft und Abstand zum Rand.
- Vorschauen und Downloadpaket aktualisiert.
- Bekannte Einschränkung: Der `[cspacer]`-Präfix in Chatmeldungen wird vom Theme nicht entfernt. Kanalnamen bleiben unverändert.

## 1.0.0-beta.6

- Identität mit UID, Client-ID und Datenbank-ID an das Ende des eigenen Nutzer-Templates verschoben, hinter Verbindung & Client.
- Vorschau und Downloadpaket an die neue Reihenfolge angepasst.

## 1.0.0-beta.5

- Lachsrote Akzentfarbe `#FA8072` für Links, Fokusmarkierungen und aktive Tab-Unterstreichungen eingeführt.
- Dunklere, dazu passende Farbtöne für Auswahlflächen, Hover-Zustände und weitere Bedienelemente ergänzt.
- Nutzerinformationen neu sortiert: optionale Beschreibung, Servergruppen, Channelgruppe, Abzeichen, Identität, Verbindung & Client. Die Identität wurde anschließend in Beta 6 ganz nach unten verschoben.
- Hintergrund sowie Gruppen- und Statusicons beibehalten.

## 1.0.0-beta.4

- Talk Power aus der Nutzeransicht entfernt.
- Dokumentation und Vorschau entsprechend aktualisiert.

## 1.0.0-beta.3

- Eigenes Nutzer-Template mit eindeutiger ID (UID), Sitzungs-ID und Datenbank-ID ergänzt.
- Version, Plattform, Onlinezeit, erste und letzte Verbindung sowie Verbindungsanzahl aufgenommen; Talk Power war zunächst enthalten.
- Optionale Beschreibung, Abwesenheitsnachricht und lokale Lautstärke ergänzt. Gruppen, Abzeichen, Plugininformationen sowie die vom Client angehängten Avatar- und Statusanzeigen berücksichtigt.
- Zusätzlichen Banner mit fester Breite aus dem Server-Infotext entfernt.
- Anleitung zur proportionalen Skalierung des serverseitigen Hostbanners ergänzt: `virtualserver_hostbanner_mode=2`. Das Theme ändert diese Servereinstellung nicht.
- Separate Vorschau der Nutzeransicht hinzugefügt.

## 1.0.0-beta.2

- Verzerrende Streckung der Glastextur auf die Fensterfläche entfernt.
- Hintergrund proportional und fest verankert; Glasdetails abgedunkelt und weichen Übergang zur Grundfarbe am unteren Rand ergänzt.
- Qt-Vorschau mit normaler und doppelter Fensterhöhe geprüft und hohe Vorschau hinzugefügt.

## 1.0.0-beta.1

- Eigenständiges TS3-Theme und separates Repository veröffentlicht.
- Dunkle Gestaltung für Kanalbaum, Menüs, Dialoge, Chat, Tabellen, Eingaben und Statusleiste erstellt.
- Original-OCB-Banner, Bigcircle-Logo und durchgehende Glastextur eingebunden.
- Installierbares `.ts3_style`-Paket, Installationsanleitung, Nutzungsbedingungen, Prüfsummen und native Qt-Vorschau bereitgestellt.

## Prüfstand und Grenzen

- QSS, Bilddateien und Paketstruktur wurden mit einer nativen Qt-5-Testoberfläche geprüft. Die Vorschauen sind keine Screenshots eines verbundenen TS3-Clients.
- Nutzer-Screenshots lieferten Rückmeldungen zur tatsächlichen TS3-Darstellung. Ein vollständiger Funktionstest aller Clientbereiche sowie Live-Tests unter Linux und macOS stehen weiterhin aus.
- Die Glastextur wurde auf 3840 × 2160 hochskaliert; sie enthält keine nativen 4K-Details.
- Verfügbarkeit einzelner Nutzerinformationen hängt von den Daten und Berechtigungen ab, die TeamSpeak bereitstellt.
