"""Validate release archives, required assets and reproducibility."""
from pathlib import Path
import hashlib, io, re, subprocess, sys, zipfile
r=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(r/'tools/build.py')],check=True)
version=re.search(r'^Version = (.+)$',(r/'package.ini').read_text(),re.M)[1]
base=f'OCB.GG-Glass-Dark-Theme-TS3-v{version}'
paths=[r/'dist'/f'{base}{suffix}' for suffix in ['.zip','.ts3_style']]
before=[p.read_bytes() for p in paths]
subprocess.run([sys.executable,str(r/'tools/build.py')],check=True)
assert before==[p.read_bytes() for p in paths], 'Build is not reproducible'
with zipfile.ZipFile(paths[0]) as z:
 assert set(z.namelist())=={base+'.ts3_style','HOW TO USE.html','NUTZUNGSBEDINGUNGEN.txt'}
 assert z.read(base+'.ts3_style')==paths[1].read_bytes()
 guide=z.read('HOW TO USE.html').decode('utf-8')
 assert base+'.ts3_style' in guide
 for href in re.findall(r'href="([^"]+)"',guide):
  assert href.startswith(('https://','#')) or href in z.namelist(),href
with zipfile.ZipFile(paths[1]) as z:
 assert z.testzip() is None
 assert len(z.namelist())==13
 assert all('..' not in Path(n).parts and not n.startswith(('/','\\')) for n in z.namelist())
 qss=z.read('styles/ocb_obsidian.qss').decode('utf-8')
 for asset in re.findall(r"url\(['\"]?styles:([^'\")]+)",qss):
  assert 'styles/'+asset in z.namelist(),asset
 assert z.read('styles/ocb_obsidian/LICENSE.txt')==(r/'LICENSE.txt').read_bytes()
 client=z.read('styles/ocb_obsidian/clientinfo.tpl').decode('utf-8')
 assert 'bgcolor=' not in client
 assert 'FALLBACK=true' in z.read('gfx/ocb_white/settings.ini').decode()
 assert 'CLIENT_TALK_POWER' not in client
 assert client.index('Verbindung &amp; Client') < client.index('<b>Identität</b>')
for line in (r/'dist/SHA256SUMS.txt').read_text().splitlines():
 digest,name=line.split('  ')
 assert hashlib.sha256((r/'dist'/name).read_bytes()).hexdigest()==digest
print('PASS: package contents, references, guide links, licensing, user fields, checksums and deterministic builds')
