from bs4 import BeautifulSoup

fee_html = """<section class="section section-bg" id="detailed-fees">
 <div class="container">
  <div class="section-header"><h2>Detailed Financial Breakdown</h2><p>Clear cost estimates for Indian students planning to study in France.</p></div>
  <div style="overflow-x:auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead><tr style="background:#b91c1c;color:white">
     <th style="padding:1rem;text-align:left">Category</th>
     <th style="padding:1rem;text-align:left">Public Universities</th>
     <th style="padding:1rem;text-align:left">Private Universities</th>
    </tr></thead>
    <tbody>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Annual Tuition</strong></td><td style="padding:1rem">EUR 2,770 - 3,770</td><td style="padding:1rem">EUR 10,000 - 25,000</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Living Expenses</strong></td><td style="padding:1rem" colspan="2">EUR 9,000 - 14,000/year</td></tr>
     <tr style="border-bottom:1px solid #e5e7eb"><td style="padding:1rem"><strong>Est. Total/Year (Public)</strong></td><td style="padding:1rem" colspan="2">EUR 11,770 - 17,770</td></tr>
     <tr><td style="padding:1rem"><strong>Est. Total/Year (Private)</strong></td><td style="padding:1rem" colspan="2">EUR 19,000 - 39,000</td></tr>
    </tbody>
   </table>
  </div>
  <p style="margin-top:1rem;color:#6b7280;font-size:0.9rem;">Visa Type: <strong>Long-Stay Student Visa (VLS-TS)</strong> | Work Rights: <strong>964 hrs/year</strong></p>
 </div>
</section>"""

psw_html = """<section class="section" id="post-study-work">
 <div class="container">
  <div class="section-header"><h2>Post-Study Work and Career Opportunities</h2><p>Transparent guide to stay-back rights and career outcomes in France.</p></div>
  <div class="services-grid" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
    <h3>APS Recherche Visa</h3>
    <p style="color:#b91c1c;font-weight:600;">2 Years (Masters)</p>
    <p>Masters graduates receive 2-year post-study authorization to find employment in France or the EU.</p>
   </div>
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg></div>
    <h3>PR Pathways</h3>
    <p style="color:#b91c1c;font-weight:600;">Long-Term Settlement</p>
    <p>Talent Passport to French Permanent Residency through skilled employment.</p>
   </div>
   <div class="service-card">
    <div class="service-icon"><svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect></svg></div>
    <h3>Top Hiring Sectors</h3>
    <p style="color:#b91c1c;font-weight:600;">In-Demand Fields</p>
    <p>Luxury Management, Culinary Arts, Technology, Research</p>
   </div>
  </div>
 </div>
</section>"""

fp = r'c:\Users\admin\Downloads\New folder\study_visa\france.html'
with open(fp, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Remove any existing duplicates
for sec in soup.find_all('section'):
    h2 = sec.find('h2')
    if h2 and any(k in h2.get_text() for k in ['Detailed Financial', 'Post-Study Work', 'Career Opportunities']):
        sec.decompose()

new_secs = BeautifulSoup(fee_html + psw_html, 'html.parser')

# Find the contact form section to insert before
target = None
all_sections = soup.find_all('section')
for sec in all_sections:
    if sec.find('form'):
        target = sec
        break
    h2 = sec.find('h2')
    if h2 and 'Contact' in h2.get_text():
        target = sec
        break

if target:
    target.insert_before(new_secs)
    print('Inserted before contact/form section')
else:
    # Append before footer
    footer = soup.find('footer')
    if footer and footer.parent:
        footer.insert_before(new_secs)
        print('Inserted before footer')
    else:
        soup.body.append(new_secs)
        print('Appended to body')

with open(fp, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('France.html patched successfully.')
