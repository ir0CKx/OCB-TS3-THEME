from pathlib import Path
import configparser,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
def write_zip(target,entries):
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for name,data in sorted(entries.items()):
            i=zipfile.ZipInfo(name,(2026,1,1,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o644<<16;z.writestr(i,data)
    with zipfile.ZipFile(target) as z:assert z.testzip() is None
    return target
if __name__=='__main__':
    c=configparser.ConfigParser();c.read_string('[Package]\n'+(ROOT/'package.ini').read_text());version=c['Package']['Version']
    dest=ROOT/'dist';dest.mkdir(exist_ok=True)
    names=['package.ini','styles/ocb_obsidian.qss','styles/ocb_obsidian_chat.qss']+['styles/ocb_obsidian/'+n for n in ['clientinfo.tpl','serverinfo.tpl','glass-dark.svg','watermark.svg','arrow-up.svg','arrow-down.svg','LICENSE.txt']]
    style=write_zip(dest/f'OCB.GG-Glass-Dark-Theme-TS3-v{version}.ts3_style',{n:(ROOT/n).read_bytes() for n in names})
    bundle=write_zip(dest/f'OCB.GG-Glass-Dark-Theme-TS3-v{version}.zip',{style.name:style.read_bytes(),'HOW TO USE.html':(ROOT/'docs/HOW TO USE.html').read_bytes(),'NUTZUNGSBEDINGUNGEN.txt':(ROOT/'LICENSE.txt').read_bytes()})
    (dest/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in [style,bundle]))
    print(style);print(bundle)
