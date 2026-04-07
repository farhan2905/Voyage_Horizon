import os
from bs4 import BeautifulSoup

base = r'c:\Users\admin\Downloads\New folder\study_visa'

# ============================================================
# FEE + PSW data for pages that are missing them
# ============================================================

missing_data = {
    'spain.html': {
        'country': 'Spain',
        'fee_html': """<section class="section section-bg" id="detailed-fees">
 <div class="container">
  <div class="section-header"><h2>Detailed Financial Breakdown</h2><p>Clear cost estimates for Indian students planning to study in Spain.</p></div>
  <div style="overflow-x:auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead><tr style="background:#b91c1c;color:white">
     <th style="padding:1rem;text-align:left">Category</th>
     <th style="padding:1rem;text-align:left">Public Universities</th>
     <th style="padding:1rem;text-align:left">Private Universities</th>
    </tr></thead>
    <tbody>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Annual Tuition</strong></td><td style="padding:1rem">EUR 1,000 - 3,500</td><td style="padding:1rem">EUR 5,000 - 25,000</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Living Expenses</strong></td><td style="padding:1rem" colspan="2">EUR 8,000 - 12,000/year</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Health Insurance</strong></td><td style="padding:1rem" colspan="2">EUR 500 - 1,200/year</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Est. Total/Year (Public)</strong></td><td style="padding:1rem" colspan="2">EUR 9,500 - 16,700</td></tr>
     <tr><td style="padding:1rem"><strong>Est. Total/Year (Private)</strong></td><td style="padding:1rem" colspan="2">EUR 13,500 - 38,200</td></tr>
    </tbody>
   </table>
  </div>
  <p style="margin-top:1rem;color:#6b7280;font-size:0.9rem;">Visa Type: <strong>Type D Student Visa</strong> | Work Rights: <strong>20 hrs/week during term</strong></p>
 </div>
</section>""",
        'psw_html': """<section class="section" id="post-study-work">
 <div class="container">
  <div class="section-header"><h2>Post-Study Work &amp; Career Opportunities</h2><p>Your pathway to employment and settlement after studying in Spain.</p></div>
  <div class="services-grid" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
    <h3>Post-Study Job Search Visa</h3>
    <p style="color:#b91c1c;font-weight:600;">12 Months</p>
    <p>Spain offers a 12-month residence permit for graduates to seek employment or start a business after completing their degree.</p>
   </div>
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg></div>
    <h3>PR Pathways</h3>
    <p style="color:#b91c1c;font-weight:600;">Residency After 5 Years</p>
    <p>Work permit holders can apply for permanent residency after 5 years of legal residence in Spain.</p>
   </div>
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect></svg></div>
    <h3>Top Hiring Sectors</h3>
    <p style="color:#b91c1c;font-weight:600;">In-Demand Fields</p>
    <p>Tourism &amp; Hospitality, Renewable Energy, Business &amp; Marketing, Technology, Healthcare</p>
   </div>
  </div>
 </div>
</section>"""
    },
    'uk.html': {
        'country': 'UK',
        'fee_html': """<section class="section section-bg" id="detailed-fees">
 <div class="container">
  <div class="section-header"><h2>Detailed Financial Breakdown</h2><p>Clear cost estimates for Indian students planning to study in the UK.</p></div>
  <div style="overflow-x:auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead><tr style="background:#b91c1c;color:white">
     <th style="padding:1rem;text-align:left">Category</th>
     <th style="padding:1rem;text-align:left">Undergraduate</th>
     <th style="padding:1rem;text-align:left">Postgraduate</th>
    </tr></thead>
    <tbody>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Annual Tuition</strong></td><td style="padding:1rem">GBP 12,000 - 38,000</td><td style="padding:1rem">GBP 15,000 - 45,000</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Living Expenses (London)</strong></td><td style="padding:1rem" colspan="2">GBP 12,000 - 15,000/year</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Living Expenses (Outside London)</strong></td><td style="padding:1rem" colspan="2">GBP 9,000 - 12,000/year</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>NHS Health Surcharge</strong></td><td style="padding:1rem" colspan="2">GBP 776/year</td></tr>
     <tr><td style="padding:1rem"><strong>Estimated Total/Year</strong></td><td style="padding:1rem">GBP 22,000 - 53,000</td><td style="padding:1rem">GBP 25,000 - 60,000</td></tr>
    </tbody>
   </table>
  </div>
  <p style="margin-top:1rem;color:#6b7280;font-size:0.9rem;">Visa Type: <strong>Student Visa (Tier 4)</strong> | Work Rights: <strong>20 hrs/week during term</strong></p>
 </div>
</section>""",
        'psw_html': """<section class="section" id="post-study-work">
 <div class="container">
  <div class="section-header"><h2>Post-Study Work &amp; Career Opportunities</h2><p>Your pathway to employment and settlement after studying in the UK.</p></div>
  <div class="services-grid" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
    <h3>Graduate Route Visa</h3>
    <p style="color:#b91c1c;font-weight:600;">2 Years (3 for PhD)</p>
    <p>The UK Graduate Route allows international students to stay and work for 2 years after completing a Bachelor's or Master's degree, and 3 years for PhD graduates.</p>
   </div>
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg></div>
    <h3>PR Pathways</h3>
    <p style="color:#b91c1c;font-weight:600;">Skilled Worker to ILR</p>
    <p>Transition to a Skilled Worker Visa and apply for Indefinite Leave to Remain (ILR) after 5 years of continuous employment.</p>
   </div>
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect></svg></div>
    <h3>Top Hiring Sectors</h3>
    <p style="color:#b91c1c;font-weight:600;">In-Demand Fields</p>
    <p>Finance &amp; Banking, Healthcare (NHS), Technology, Engineering, Consulting &amp; Professional Services</p>
   </div>
  </div>
 </div>
</section>"""
    },
}

for fname, data in missing_data.items():
    fp = os.path.join(base, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Check if fee and PSW sections already exist
    has_fee = False
    has_psw = False
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            txt = h2.get_text(strip=True)
            if 'Financial Breakdown' in txt or 'Fee' in txt:
                has_fee = True
            if 'Post-Study' in txt or 'Career Opportunities' in txt:
                has_psw = True
    
    if has_fee and has_psw:
        print(f"  {fname}: Already has fee and PSW - skipping")
        continue
    
    # Find insertion point: before roadmap/pathway section
    insert_before = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and any(k in h2.get_text() for k in ['Pathway', 'Roadmap', 'Process']):
            if not sec.find('form'):
                insert_before = sec
                break
    
    if not insert_before:
        # Try before CTA
        insert_before = soup.find('section', class_='cta-section')
    
    if not insert_before:
        # Try before footer
        insert_before = soup.find('footer')
    
    parts_to_add = []
    if not has_fee:
        parts_to_add.append(data['fee_html'])
    if not has_psw:
        parts_to_add.append(data['psw_html'])
    
    combined_html = '\n'.join(parts_to_add)
    new_soup = BeautifulSoup(combined_html, 'html.parser')
    
    if insert_before:
        insert_before.insert_before(new_soup)
        print(f"  {fname}: Inserted fee/PSW before {insert_before.find('h2').get_text(strip=True) if insert_before.find('h2') else 'target'}")
    else:
        soup.find('body').append(new_soup)
        print(f"  {fname}: Appended fee/PSW to body")
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("\nSpain and UK fee/PSW sections patched.")
