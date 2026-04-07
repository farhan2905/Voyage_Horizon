import os

# France and Spain have € encoded as &euro; or &#8364; by BeautifulSoup, 
# causing the audit to miss the currency. Let's verify by reading raw.

for fname in ['france.html', 'spain.html']:
    fp = os.path.join(r'c:\Users\admin\Downloads\New folder\study_visa', fname)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find table with any euro marker
    if '€' in content or '&euro;' in content or '&#8364;' in content or '8364' in content:
        print(f"{fname}: euro symbol FOUND")
    else:
        print(f"{fname}: euro symbol MISSING - checking...")
        # Check what currency text is near fee table
        idx = content.find('detailed-fees')
        if idx > -1:
            snippet = content[idx:idx+500]
            print(f"  Snippet: {snippet[:300]}")
