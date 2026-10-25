# Entwicklung
`python tools/build.py` erzeugt deterministische .ts3_style- und Nutzer-ZIP-Pakete in dist. Nur tatsächlich verwendete Style-Dateien werden aufgenommen. Originale Banner und alte Vorschauen verbleiben im Repository, nicht im Installer.
`pip install -r tests/requirements.txt` installiert die Qt-Testabhängigkeit. `TS3_CLIENTINFO` auf das clientinfo.tpl der installierten TS3-Standardvorlage setzen. Dann `python tests/qt_theme.py` ausführen. Optional: QT_TEST_RUNTIME für einen vorhandenen PyQt5-Paketordner, TEST_FONT für eine Schriftdatei.
Tests verwenden native Qt-Widgets, aber keinen verbundenen TS3-Client. Berichte und Vorschauen landen nur in test-results. Client-Liveprüfung und Betriebssystemmatrix bleiben gesondert erforderlich.

`python tests/package.py` prüft Archivinhalt, Referenzen, Anleitung, Nutzungsbedingungen, Nutzerfelder, Prüfsummen und reproduzierbaren Paketbau. Diese Prüfung läuft auch in GitHub Actions.
