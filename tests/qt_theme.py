import sys, os, re, json, zipfile, hashlib
from pathlib import Path
if os.environ.get('QT_TEST_RUNTIME'):sys.path.insert(0,os.environ['QT_TEST_RUNTIME'])
os.environ['QT_QPA_PLATFORM']='offscreen'
from PyQt5 import QtWidgets as W, QtCore as C, QtGui as G
root=Path(__file__).resolve().parents[1]
results=root/'test-results';results.mkdir(exist_ok=True)
app=W.QApplication([]); app.setStyle('Fusion')
font_id=G.QFontDatabase.addApplicationFont(os.environ.get('TEST_FONT','C:/Windows/Fonts/segoeui.ttf'))
app.setFont(G.QFont('Segoe UI',10))
errors=[]
C.qInstallMessageHandler(lambda mode,ctx,msg: errors.append(msg))
C.QDir.addSearchPath('styles',str(root/'styles'))
qss=(root/'styles/ocb_obsidian.qss').read_text(encoding='utf-8')
for p in re.findall(r"url\('styles:([^']+)'\)",qss):
    assert (root/'styles'/p).is_file(),p
    assert not G.QImage(str(root/'styles'/p)).isNull(),p
app.setStyleSheet(qss)
window=W.QMainWindow(); window.setWindowTitle('OCB Obsidian Glass — native Qt test preview (not live TS3)');window.resize(1280,850)
for title in ['Verbindungen','Lesezeichen','Selbst','Rechte','Extras','Hilfe']:
    menu=window.menuBar().addMenu(title);menu.addAction('Beispielaktion')
bar=window.addToolBar('Audio')
for title in ['Verbinden','Mikrofon','Lautsprecher','Abwesend']:bar.addAction(title)
split=W.QSplitter();window.setCentralWidget(split)
tree=W.QTreeWidget();tree.setObjectName('ServerTreeView');tree.setHeaderHidden(True)
server=W.QTreeWidgetItem(tree,['OCB.GG | #OTHERSCANTBEAT']);server.setIcon(0,G.QIcon(str(root/'styles/ocb_obsidian/bigcircle.webp')))
for group,channels in [('ADMIN',['Administration · Büro','Administration · Besprechung']),('SUPPORT',['Support-Channel #1','Wartezimmer']),('COMMUNITY',['OCB.VIP','OCB.RUBY','OCB.EMERALD','OCB.SAPPHIRE','OCB.GOLD']),('LIVESTREAM',['Streaming-Lounge','Public-Viewing']),('MATCHROOMS',['Matchroom #1','Matchroom #2']),('ESPORT',['MAIN · OCB.GG','NEMORA · OCB.NEM','APEX · OCB.APX'])]:
    item=W.QTreeWidgetItem(server,[group])
    for label in channels:W.QTreeWidgetItem(item,[label])
tree.expandAll();split.addWidget(tree)
right=W.QWidget();layout=W.QVBoxLayout(right);split.addWidget(right);split.setSizes([450,830])
info=W.QTextEdit();info.setObjectName('InfoFrame');info.setReadOnly(True)
info.document().setDefaultStyleSheet((root/'styles/ocb_obsidian_chat.qss').read_text())
tpl=(root/'styles/ocb_obsidian/serverinfo.tpl').read_text()
values={'SERVER_NAME':'OCB.GG | #OTHERSCANTBEAT','SERVER_CLIENTS_ONLINE':'12','SERVER_MAXCLIENTS':'64','SERVER_CHANNELS_ONLINE':'28','SERVER_UPTIME':'2 Tage','SERVER_ADDRESS':'ts.ocb.gg','SERVER_PORT':'9987','SERVER_VERSION':'TeamSpeak 3','SERVER_PLATFORM':'Beispieldaten','SERVER_LICENSE':'Community'}
tpl=re.sub(r'%%(\??[A-Z_]+)%%',lambda m:values.get(m[1],m[1][3:].replace('_',' ').title() if m[1].startswith('TR_') else ''),tpl)
info.setHtml(tpl);layout.addWidget(info,3)
tabs=W.QTabWidget();chat=W.QTextEdit();chat.setObjectName('ChatTab');chat.setReadOnly(True);chat.setHtml('<b>OCB.GG</b><p>Willkommen bei #OTHERSCANTBEAT.</p><p>Native Qt-Vorschau · Beispieldaten</p>');tabs.addTab(chat,'Serverchat');layout.addWidget(tabs,1)
line=W.QLineEdit();line.setPlaceholderText('Nachricht eingeben …');layout.addWidget(line)
row=W.QHBoxLayout();row.addWidget(W.QCheckBox('Benachrichtigungen'));row.addStretch();row.addWidget(W.QPushButton('Senden'));layout.addLayout(row)
window.statusBar().showMessage('OCB Obsidian Glass · TS3 Beta · native Qt-Testoberfläche')
window.show();app.processEvents();window.grab().save(str(results/'preview.png'))
window.resize(1280,1700);app.processEvents()
window.grab().save(str(results/'preview-tall.png'))
client_tpl=(root/'styles/ocb_obsidian/clientinfo.tpl').read_text(encoding='utf-8')
documented=Path(os.environ['TS3_CLIENTINFO']).read_text(encoding='utf-8')
fields=set(re.findall(r'%%\?{0,2}([A-Z_]+)%%',client_tpl))
assert all(f in documented for f in fields),fields
assert '%%CLIENT_UNIQUE_ID%%' in client_tpl
assert 'AVATAR_IMAGE_DONT_APPEND%%1' not in client_tpl
assert 'STATUS_ICONS_DONT_APPEND%%1' not in client_tpl
demo={'CLIENT_NAME':'OCB Member (Beispiel)','CLIENT_ID':'42','CLIENT_UNIQUE_ID':'AbCdEfGhIjKlMnOpQrStUvWxYz0=','CLIENT_NAME_PERCENT_ENCODED':'OCB%20Member','CLIENT_DATABASE_ID':'1234','CLIENT_VERSION_LONG':'3.6.2 [Stable] Windows','CLIENT_PLATFORM':'Windows','CLIENT_CONNECTED_SINCE':'25 Minuten','CLIENT_CREATED':'01.01.2025 12:00','CLIENT_LASTCONNECTED':'22.10.2026 18:00','CLIENT_TOTALCONNECTIONS':'128','CLIENT_TALK_POWER':'0','CLIENT_DESCRIPTION':'Beispieldaten zur Vorschau','CLIENT_SERVER_GROUP_NAME':'Member','CLIENT_CHANNEL_GROUP_NAME':'Gast','CLIENT_FLAG_BADGES':'1','CLIENT_BADGE_NAME':'Beispiel-Abzeichen'}
def render_client(data):
    # Emulate documented line conditionals only; TS3's own group expansion is not emulated.
    content=re.sub(r'<!--.*?-->','',client_tpl,flags=re.S)
    lines=[]
    for line in content.splitlines():
        if any(not data.get(f) or data.get(f)=='0' for f in re.findall(r'%%\?{1,2}([A-Z_]+)%%',line)):continue
        line=re.sub(r'%%\?\?([A-Z_]+)%%','',line)
        lines.append(re.sub(r'%%\??([A-Z_]+)%%',lambda m:data.get(m[1],''),line))
    return '\n'.join(lines)
minimal=render_client({'CLIENT_NAME':'Minimal','CLIENT_ID':'1','CLIENT_UNIQUE_ID':'example=','CLIENT_TALK_POWER':'0'})
assert 'Datenbank-ID' not in minimal and 'Abwesend' not in minimal and '%%' not in minimal
assert 'CLIENT_TALK_POWER' not in client_tpl
assert client_tpl.index('<b>Channelgruppe</b>') < client_tpl.index('<b>Abzeichen</b>') < client_tpl.index('<b>Verbindung &amp; Client</b>')
info.setHtml(render_client(demo));window.resize(1100,1100);split.setSizes([650,450]);app.processEvents()
window.grab().save(str(results/'preview-client.png'))
assert 'border-image: none' in qss and 'background-attachment: fixed' in qss
assert 'stretch stretch' not in qss
controls=W.QWidget();controls.setWindowTitle('Qt control-state regression fixture')
form=W.QFormLayout(controls)
disabled=W.QLineEdit('Nicht verfügbar');disabled.setEnabled(False);form.addRow('Deaktiviert',disabled)
decimal=W.QDoubleSpinBox();decimal.setValue(42.5);form.addRow('Dezimalwert',decimal)
slider=W.QSlider(C.Qt.Vertical);slider.setRange(0,100);slider.setValue(65);slider.setMinimumHeight(120);form.addRow('Lautstärke',slider)
for points in (10,15):
 controls.setFont(G.QFont('Segoe UI',points));controls.resize(500,400);controls.show();decimal.setFocus();app.processEvents()
 controls.grab().save(str(results/f'controls-{points}pt.png'))
 assert disabled.palette().color(G.QPalette.Disabled,G.QPalette.Text).name()=='#969eaa'
 assert decimal.minimumSizeHint().height()<=decimal.height()
 assert decimal.value()==42.5 and slider.value()==65
controls.close()
parse=[m for m in errors if 'stylesheet' in m.lower() or 'unknown property' in m.lower() or 'could not' in m.lower()]
assert not parse,parse
report={'version':'1.0.0-beta.8','qt':C.QT_VERSION_STR,'qss_parse_errors':parse,'assets_decode':True,'native_fixture':['1280x850','1280x1700','1100x1100 client info'],'controls_fonts_pt':[10,15],'disabled_text_palette_verified':True,'background_stretch_removed':True,'client_fields_documented':True,'optional_fields_fixture_test':True,'live_ts3_test':False,'limitations':['No connected TS3 runtime test','No macOS or Linux runtime test','Hostbanner scaling must be configured on the server','TS3 group and badge expansion not emulated by fixture']}
(results/'VALIDATION.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))
