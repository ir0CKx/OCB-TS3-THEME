# OCB.GG Obsidian Glass — TeamSpeak 3

Eigenständiges OCB-Client-Theme für TeamSpeak 3, Version **1.0.0-beta.4**.
Anthrazit, Silber, durchgehende Glastextur im Serverbaum und Original-OCB-Banner.
Menüs, Einstellungen, Chat, Tabellen, Eingaben und Statusleiste erhalten passende Farben.

## Download und Installation
1. [OCB-Obsidian-Glass-TS3-1.0.0-beta.4.ts3_style](downloads/OCB-Obsidian-Glass-TS3-1.0.0-beta.4.ts3_style) herunterladen (bei GitHub **Download raw file**).
2. Datei doppelklicken und im TeamSpeak-Paketinstaller installieren.
3. In TS3 **Extras → Optionen → Design** das Theme **ocb_obsidian** wählen. Falls angeboten, den Stil **Fusion** wählen; dieser ist die geprüfte Qt-Basis.
4. Übernehmen und TS3 gegebenenfalls neu starten.

Falls keine Dateizuordnung existiert: Rechtsklick → Öffnen mit → `package_inst.exe` aus dem TeamSpeak-3-Installationsordner.
Alternativ den Inhalt von `styles/` nach `%APPDATA%/TS3Client/styles/` kopieren. Bereits vorhandene Dateien dieses Themes vorher sichern.
Linux: `~/.ts3client/styles/`; macOS: `~/Library/Application Support/TeamSpeak 3/styles/`.
Deinstallation: zuerst Standardtheme wählen, danach `ocb_obsidian.qss`, `ocb_obsidian_chat.qss` und den Ordner `ocb_obsidian` aus dem Benutzer-Styles-Verzeichnis entfernen.

## Grafik und Grenzen
- Glastextur: 3840 × 2160, aus 1672 × 941 hochskaliert; keine native 4K-Detailaufnahme.
- Originalbanner: 2172 × 724, unverändert mitgeliefert. Als TS3-Hostbanner mit proportionaler Skalierung verwenden; kein zusätzliches Bild mit fester Breite im Info-Template.
- Ein Hintergrund über den gesamten Kanalbaum, keine wiederholten Bildstreifen je Kanal. Die Textur bleibt proportional und fest verankert, wird nicht auf die Fensterform gestreckt und läuft nach unten weich in die Grundfarbe aus.
- Original-Bigcircle im Infobereich. Vorhandene Server-, Gruppen-, Mikrofon- und Statusicons bleiben erhalten. Dieses Paket ersetzt keine globalen Servericons.
- Keine Plugins, Skripte oder extern geladenen Ressourcen. Das Theme fügt keine Bildschirmfreigabe oder andere Clientfunktionen hinzu.
- Aufbau anhand der installierten TS3-3.5.6-Dateien geprüft. Native Qt-5-Testoberfläche geprüft; noch kein vollständiger Funktionstest im laufenden TS3-Client. Daher ausdrücklich Beta. Andere Versionen und Betriebssysteme sind nicht live geprüft.

## Vorschau
![Native Qt-Testoberfläche, kein Screenshot eines verbundenen TS3-Clients](preview.png)
Die Vorschau verwendet die echten QSS-Dateien in einer nativen Qt-5-Testoberfläche. Serverdaten sind Beispieldaten.

## Nutzerinformationen (ab Beta 3)
Beim Anklicken eines Nutzers zeigt das Infofenster UID, Sitzungs-ID, Datenbank-ID, Version, Plattform, Onlinezeit, erste/letzte Verbindung und Verbindungsanzahl. Beschreibung, Abwesenheit und lokale Lautstärke erscheinen bei vorhandenem Inhalt. Server-/Channelgruppen, Abzeichen, Avatar, Statusicons und Plugininformationen bleiben vorgesehen. Manche Angaben liefert TS3 nur mit passenden Berechtigungen oder nach einer Datenabfrage; ein Theme kann fehlende Daten nicht beschaffen. UID und Sitzungs-ID sind unterschiedliche Werte. Die Texte dieses eigenen Templates sind deutsch.

## Banner proportional mitskalieren
Der Banner oberhalb des Infofensters ist der **Hostbanner des Servers**. Seine Größenanpassung wird serverseitig gesteuert, nicht durch das QSS-Theme.
Als Serveradmin: Rechtsklick auf den Server → Virtuellen Server bearbeiten → gegebenenfalls Mehr → Host → Hostbanner → Größenanpassung **Anpassen und Seitenverhältnis beibehalten** (englisch: Adjust and keep aspect ratio).
Der entsprechende ServerQuery-Wert ist `virtualserver_hostbanner_mode=2`. Nur in einer bereits korrekt ausgewählten ServerQuery-Sitzung: `serveredit virtualserver_hostbanner_mode=2`.
Das Originalbild hat ein Seitenverhältnis von 3:1. Die TS3-eigene Bannerfläche kann die maximal verfügbare Höhe begrenzen. Dieses Theme setzt keine feste Bannerbreite und enthält ab Beta 3 keinen zusätzlichen 480-Pixel-Banner im Server-Infotext.
Referenz: [TeamSpeak SDK – HostBannerMode](https://github.com/teamspeak/ts3client-pluginsdk/blob/master/include/teamspeak/public_rare_definitions.h).

## Weitere OCB-Themes
[TeamSpeak 6 Theme](https://github.com/ir0CKx/OCB-TS6-THEME) — eigenes Paket, separat installieren.

## Nutzung
Kostenlose Nutzung gemäß [Nutzungsbedingungen](LICENSE.txt). Kein Weiterverkauf, keine separate Verwendung des Logos ohne Erlaubnis. Community-Projekt von OCB.GG, kein offizielles TeamSpeak-Produkt.

## Formatreferenzen
Paketstruktur: [Improved Default Theme](https://github.com/svenpaulsen/ts3client-improved-theme). QSS wurde eigenständig für OCB geschrieben; kein fremder Theme-Code übernommen.
