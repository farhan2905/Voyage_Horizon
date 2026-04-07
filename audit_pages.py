import os
from bs4 import BeautifulSoup

def audit_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    sections = []
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            sections.append(h2.get_text(strip=True))
    
    has_uni = any('Universit' in k or 'Top ' in k for k in sections)
    has_fee = any('Fee' in k or 'Financial' in k or 'Cost' in k for k in sections)
    has_psw = any('Post-Study' in k or 'Career' in k or 'Opportunit' in k for k in sections)
    has_process = any('Plan' in k or 'Process' in k or 'Pathway' in k or 'Admission' in k or 'Step' in k or 'Journey' in k for k in sections)
    has_why = any('Why' in k for k in sections)
    has_form = bool(soup.find('form'))
    has_table = bool(soup.find('table'))
    
    return {
        'uni': has_uni,
        'fee': has_fee,
        'psw': has_psw,
        'process': has_process,
        'why': has_why,
        'form': has_form,
        'table': has_table,
        'sections': sections
    }

base = r'c:\Users\admin\Downloads\New folder'

print("--- STUDY VISA AUDIT ---")
print(f"{'File':<25} | Uni | Fee | PSW | Proc | Why | Form | Table")
print("-" * 70)
for f in sorted(os.listdir(os.path.join(base, 'study_visa'))):
    if f.endswith('.html'):
        r = audit_page(os.path.join(base, 'study_visa', f))
        u, fe, p, pr, w, fm, t = r['uni'], r['fee'], r['psw'], r['process'], r['why'], r['form'], r['table']
        flags = f"{'Y' if u else 'N':^5}|{'Y' if fe else 'N':^5}|{'Y' if p else 'N':^5}|{'Y' if pr else 'N':^6}|{'Y' if w else 'N':^5}|{'Y' if fm else 'N':^6}|{'Y' if t else 'N':^6}"
        print(f"{f:<25} | {flags}")

print()
print("--- MBBS ABROAD AUDIT ---")
print(f"{'File':<25} | Uni | Fee | PSW | Proc | Why | Form | Table")
print("-" * 70)
for f in sorted(os.listdir(os.path.join(base, 'mbbs_abroad'))):
    if f.endswith('.html'):
        r = audit_page(os.path.join(base, 'mbbs_abroad', f))
        u, fe, p, pr, w, fm, t = r['uni'], r['fee'], r['psw'], r['process'], r['why'], r['form'], r['table']
        flags = f"{'Y' if u else 'N':^5}|{'Y' if fe else 'N':^5}|{'Y' if p else 'N':^5}|{'Y' if pr else 'N':^6}|{'Y' if w else 'N':^5}|{'Y' if fm else 'N':^6}|{'Y' if t else 'N':^6}"
        print(f"{f:<25} | {flags}")
