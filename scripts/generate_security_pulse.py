from pathlib import Path
from datetime import datetime, timezone
import json, urllib.request
OUT=Path('assets/security-pulse.svg'); OUT.parent.mkdir(exist_ok=True)
url='https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'
try:
    req=urllib.request.Request(url,headers={'User-Agent':'mahrukh89-profile'})
    with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)
    vulns=sorted(data.get('vulnerabilities',[]),key=lambda x:x.get('dateAdded',''),reverse=True)[:4]
except Exception: vulns=[]
def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
rows=[(v.get('cveID','CVE'),((v.get('vendorProject','')+' '+v.get('product','')).strip()[:56])) for v in vulns] or [('Feed unavailable','Workflow will retry automatically')]
h=120+len(rows)*42; y=108
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{h}" viewBox="0 0 900 {h}">','<rect width="100%" height="100%" rx="16" fill="#0d1117" stroke="#30363d"/>','<text x="28" y="42" font-family="Segoe UI,Arial" font-size="23" font-weight="700" fill="#f85149">SOC Pulse · CISA Known Exploited Vulnerabilities</text>','<text x="28" y="68" font-family="Segoe UI,Arial" font-size="12" fill="#8b949e">Automated public threat-awareness panel · educational portfolio use</text>']
for cve,desc in rows:
    p += [f'<text x="30" y="{y}" font-family="Segoe UI,Arial" font-size="15" font-weight="700" fill="#58a6ff">{esc(cve)}</text>',f'<text x="190" y="{y}" font-family="Segoe UI,Arial" font-size="14" fill="#c9d1d9">{esc(desc)}</text>']; y+=42
p.append(f'<text x="28" y="{h-22}" font-family="Segoe UI,Arial" font-size="12" fill="#8b949e">Updated {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}</text></svg>')
OUT.write_text('\n'.join(p),encoding='utf-8')
