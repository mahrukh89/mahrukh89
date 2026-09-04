from pathlib import Path
import json, os, urllib.request
from datetime import datetime, timezone
USER='mahrukh89'; OUT=Path('metrics'); OUT.mkdir(exist_ok=True)
def api(path):
    req=urllib.request.Request('https://api.github.com'+path,headers={'Accept':'application/vnd.github+json','Authorization':'Bearer '+os.getenv('GITHUB_TOKEN',''),'User-Agent':'mahrukh89-profile'})
    with urllib.request.urlopen(req,timeout=30) as r: return json.load(r)
def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def make_svg(title,rows,width=760):
    h=90+len(rows)*34; y=78
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}">',
       '<rect width="100%" height="100%" rx="16" fill="#0d1117" stroke="#30363d"/>',
       f'<text x="28" y="42" font-family="Segoe UI,Arial" font-size="22" font-weight="700" fill="#58a6ff">{esc(title)}</text>']
    for k,v in rows:
        p.append(f'<text x="30" y="{y}" font-family="Segoe UI,Arial" font-size="15" fill="#8b949e">{esc(k)}</text>')
        p.append(f'<text x="{width-30}" y="{y}" text-anchor="end" font-family="Segoe UI,Arial" font-size="15" font-weight="600" fill="#f0f6fc">{esc(v)}</text>')
        y+=34
    p.append('</svg>'); return '\n'.join(p)
repos=api(f'/users/{USER}/repos?per_page=100&type=owner'); profile=api(f'/users/{USER}')
repos=[r for r in repos if not r.get('fork')]
stars=sum(r.get('stargazers_count',0) for r in repos); forks=sum(r.get('forks_count',0) for r in repos)
langs={}; topics={}
for r in repos:
    if r.get('language'): langs[r['language']]=langs.get(r['language'],0)+1
    for t in r.get('topics',[]) or []: topics[t]=topics.get(t,0)+1
(OUT/'metrics-overview.svg').write_text(make_svg('GitHub Portfolio Metrics', [('Public repositories',len(repos)),('Followers',profile.get('followers',0)),('Repository stars',stars),('Repository forks',forks),('Updated',datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC'))]),encoding='utf-8')
(OUT/'languages.svg').write_text(make_svg('Repository Languages',sorted(langs.items(),key=lambda x:(-x[1],x[0]))[:7] or [('No language data yet','—')]),encoding='utf-8')
(OUT/'topics.svg').write_text(make_svg('Security Repository Topics',sorted(topics.items(),key=lambda x:(-x[1],x[0]))[:8] or [('Add repository topics','recommended')]),encoding='utf-8')
recent=sorted(repos,key=lambda r:r.get('pushed_at') or '',reverse=True)[:6]
(OUT/'activity.svg').write_text(make_svg('Recent Repository Activity',[(r['name'],(r.get('pushed_at') or '')[:10]) for r in recent] or [('No repositories found','—')]),encoding='utf-8')
