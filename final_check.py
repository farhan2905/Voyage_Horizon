from bs4 import BeautifulSoup
import os

base = r'c:\Users\admin\Downloads\New folder\study_visa'

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.html'):
        continue
    with open(os.path.join(base, fname), 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    secs = []
    for s in soup.find_all('section'):
        h2 = s.find('h2')
        secs.append(h2.get_text(strip=True) if h2 else 'HERO')
    
    has_f = bool(soup.find('footer'))
    has_w = bool(soup.find('a', class_='whatsapp-float'))
    tables = len(soup.find_all('table'))
    has_form = bool(soup.find('form'))
    has_fee = any('Financial' in s for s in secs)
    has_psw = any('Post-Study' in s or 'Career' in s for s in secs)
    has_uni_table = any('Comparison' in s for s in secs)
    has_roadmap = any(any(k in s for k in ['Pathway','Roadmap','Process','Admission', 'Plan']) for s in secs)
    
    missing = []
    if not has_f: missing.append('FOOTER')
    if not has_w: missing.append('WHATSAPP')
    if not has_form: missing.append('FORM')
    if not has_fee: missing.append('FEE')
    if not has_psw: missing.append('PSW')
    if not has_uni_table: missing.append('UNI_TABLE')
    if not has_roadmap: missing.append('ROADMAP')
    
    status = 'OK' if not missing else 'ISSUE'
    miss_str = ', '.join(missing) if missing else 'None'
    print(f'[{status}] {fname} | Tables:{tables} Footer:{has_f} WA:{has_w} Form:{has_form} | Missing: {miss_str}')
    for i, s in enumerate(secs):
        print(f'    {i+1}. {s}')
    print()
