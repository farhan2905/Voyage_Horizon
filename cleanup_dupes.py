import os
from bs4 import BeautifulSoup

base = r'c:\Users\admin\Downloads\New folder\study_visa'

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.html'):
        continue
    
    fp = os.path.join(base, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    changed = False
    
    # 1. Remove duplicate contact form sections (keep only the first one with a form)
    form_sections = []
    for sec in soup.find_all('section'):
        if sec.find('form'):
            form_sections.append(sec)
    
    if len(form_sections) > 1:
        for dup in form_sections[1:]:
            dup.decompose()
        changed = True
        print(f"  {fname}: Removed {len(form_sections)-1} duplicate form sections")
    
    # 2. Remove duplicate CTA sections (keep first)
    cta_sections = soup.find_all('section', class_='cta-section')
    if len(cta_sections) > 1:
        for dup in cta_sections[1:]:
            dup.decompose()
        changed = True
        print(f"  {fname}: Removed {len(cta_sections)-1} duplicate CTA sections")
    
    # 3. Remove duplicate "Contact Our X" header sections that have no form
    contact_headings = []
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and 'Contact Our' in h2.get_text() and not sec.find('form'):
            contact_headings.append(sec)
    for dup in contact_headings:
        dup.decompose()
        changed = True
    if contact_headings:
        print(f"  {fname}: Removed {len(contact_headings)} orphaned contact headers")
    
    if changed:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(str(soup))

print("\nDuplicate sections cleaned up across all study_visa pages.")
