import os
from bs4 import BeautifulSoup

base = r'c:\Users\admin\Downloads\New folder'

def deep_audit(filepath, expected_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    issues = []
    
    # Check universities section has actual uni names
    uni_cards = []
    for h3 in soup.find_all('h3'):
        text = h3.get_text(strip=True)
        if any(x in text for x in ['University', 'College', 'Institute', 'School']):
            uni_cards.append(text)
    
    if len(uni_cards) < 2:
        issues.append(f"MISSING: Only {len(uni_cards)} specific university names found")
    
    # Check PSW section has country-specific visa name
    psw_sec = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and ('Post-Study' in h2.text or 'Career' in h2.text):
            psw_sec = sec.get_text()
            break
    
    # Check fee table has actual numbers
    tables = soup.find_all('table')
    fee_table_ok = False
    for t in tables:
        text = t.get_text()
        if any(c in text for c in ['$', '€', '£', '₹', 'CHF', 'CAD', 'AUD', 'NZD']):
            fee_table_ok = True
            break
    if not fee_table_ok:
        issues.append("MISSING: No currency values found in fee table")
    
    # Check contact form is complete
    form = soup.find('form')
    if form:
        inputs = form.find_all(['input', 'select', 'textarea'])
        if len(inputs) < 4:
            issues.append(f"INCOMPLETE: Contact form has only {len(inputs)} fields")
    
    # Check hero stats
    stats = soup.find('div', class_='hero-stats')
    if not stats:
        issues.append("MISSING: Hero stats block not found")
    
    # Check country-specific relevance in hero
    h1 = soup.find('h1')
    if h1 and expected_name.lower() not in h1.get_text().lower():
        issues.append(f"MISMATCH: H1 doesn't mention '{expected_name}': '{h1.get_text(strip=True)}'")
    
    # Check Why section bullet points
    why_sec = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and 'Why' in h2.text:
            why_sec = sec
            break
    if why_sec:
        cards = why_sec.find_all('div', class_='service-card')
        if len(cards) < 4:
            issues.append(f"THIN: Only {len(cards)} Why cards (recommend 6)")
    
    return issues, uni_cards

print("=== DEEP QUALITY AUDIT ===\n")

study_visa_map = {
    'australia.html': 'Australia', 'canada.html': 'Canada', 'france.html': 'France',
    'germany.html': 'Germany', 'ireland.html': 'Ireland', 'netherlands.html': 'Netherlands',
    'new-zealand.html': 'New Zealand', 'spain.html': 'Spain', 'switzerland.html': 'Switzerland',
    'uk.html': 'UK', 'usa.html': 'USA'
}

mbbs_map = {
    'egypt.html': 'Egypt', 'georgia.html': 'Georgia', 'iraq.html': 'Iraq',
    'italy.html': 'Italy', 'kazakhstan.html': 'Kazakhstan', 'kyrgyzstan.html': 'Kyrgyzstan',
    'nepal.html': 'Nepal', 'russia.html': 'Russia', 'uzbekistan.html': 'Uzbekistan',
    'vietnam.html': 'Vietnam'
}

print("--- STUDY VISA ---")
for fname, cname in study_visa_map.items():
    fp = os.path.join(base, 'study_visa', fname)
    issues, unis = deep_audit(fp, cname)
    print(f"\n[{cname}] ({fname})")
    print(f"  Universities found: {unis[:3]}")
    if issues:
        for i in issues:
            print(f"  !! {i}")
    else:
        print(f"  OK - All checks passed")

print("\n--- MBBS ABROAD ---")
for fname, cname in mbbs_map.items():
    fp = os.path.join(base, 'mbbs_abroad', fname)
    issues, unis = deep_audit(fp, cname)
    print(f"\n[{cname}] ({fname})")
    print(f"  Universities found: {unis[:3]}")
    if issues:
        for i in issues:
            print(f"  !! {i}")
    else:
        print(f"  OK - All checks passed")
