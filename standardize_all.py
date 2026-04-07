import os
from bs4 import BeautifulSoup

base = r'c:\Users\admin\Downloads\New folder'

# ============================================================
# COMPREHENSIVE UNIVERSITY TABLE DATA (5-10 per country)
# ============================================================

uni_table_data = {
    'usa.html': [
        ('Harvard University','Cambridge, MA','Private','QS #4','\u002425k-60k','Business, Law, Medicine, STEM'),
        ('MIT','Cambridge, MA','Private','QS #1','\u002455k-60k','Engineering, CS, AI, Physics'),
        ('Stanford University','Stanford, CA','Private','QS #5','\u002455k-60k','Tech, Business, Engineering'),
        ('University of Michigan','Ann Arbor, MI','Public','QS #33','\u002425k-50k','Engineering, MBA, Healthcare'),
        ('Columbia University','New York, NY','Private','QS #23','\u002460k-65k','Journalism, Law, Business'),
        ('University of California, Berkeley','Berkeley, CA','Public','QS #10','\u002420k-45k','CS, Engineering, Sciences'),
        ('University of Chicago','Chicago, IL','Private','QS #11','\u002460k-65k','Economics, MBA, Data Science'),
        ('NYU','New York, NY','Private','QS #38','\u002455k-60k','Arts, Business, Film'),
    ],
    'uk.html': [
        ('University of Oxford','Oxford','Public','QS #3','\u00a326k-40k','All Disciplines'),
        ('University of Cambridge','Cambridge','Public','QS #2','\u00a324k-40k','Sciences, Engineering, Arts'),
        ('Imperial College London','London','Public','QS #6','\u00a330k-45k','STEM, Medicine, Business'),
        ('UCL (University College London)','London','Public','QS #9','\u00a322k-35k','Architecture, Law, Medicine'),
        ('London School of Economics','London','Public','QS #50','\u00a322k-30k','Economics, Finance, Law'),
        ('University of Edinburgh','Edinburgh','Public','QS #22','\u00a320k-32k','Medicine, AI, Humanities'),
        ('University of Manchester','Manchester','Public','QS #32','\u00a320k-30k','Engineering, Business, Sciences'),
        ('Kings College London','London','Public','QS #37','\u00a322k-38k','Law, Medicine, Humanities'),
    ],
    'canada.html': [
        ('University of Toronto','Toronto, ON','Public','QS #21','CAD \u002440k-60k','Medicine, CS, Engineering'),
        ('University of British Columbia','Vancouver, BC','Public','QS #34','CAD \u002435k-50k','Sciences, Business, Forestry'),
        ('McGill University','Montreal, QC','Public','QS #30','CAD \u002425k-50k','Medicine, Law, Engineering'),
        ('University of Waterloo','Waterloo, ON','Public','QS #112','CAD \u002435k-50k','CS, Engineering (Co-op Leader)'),
        ('University of Alberta','Edmonton, AB','Public','QS #111','CAD \u002425k-35k','Engineering, AI, Energy'),
        ('McMaster University','Hamilton, ON','Public','QS #140','CAD \u002430k-40k','Health Sciences, Engineering'),
        ('University of Montreal','Montreal, QC','Public','QS #116','CAD \u002420k-30k','AI Research, Medicine, Law'),
        ('University of Ottawa','Ottawa, ON','Public','QS #203','CAD \u002430k-42k','Law, Political Science, STEM'),
    ],
    'australia.html': [
        ('University of Melbourne','Melbourne, VIC','Public','QS #13','AUD \u002435k-50k','All Disciplines'),
        ('University of Sydney','Sydney, NSW','Public','QS #18','AUD \u002440k-55k','Business, Law, Medicine'),
        ('UNSW Sydney','Sydney, NSW','Public','QS #19','AUD \u002438k-50k','Engineering, Business, Law'),
        ('Australian National University','Canberra, ACT','Public','QS #30','AUD \u002435k-48k','Policy, Sciences, Research'),
        ('University of Queensland','Brisbane, QLD','Public','QS #40','AUD \u002435k-48k','Medicine, Engineering, Biotech'),
        ('Monash University','Melbourne, VIC','Public','QS #37','AUD \u002435k-48k','Pharmacy, IT, Engineering'),
        ('University of Western Australia','Perth, WA','Public','QS #77','AUD \u002430k-44k','Mining, Agriculture, Sciences'),
        ('University of Adelaide','Adelaide, SA','Public','QS #89','AUD \u002430k-44k','Wine Studies, Health, Engineering'),
    ],
    'germany.html': [
        ('Technical University of Munich (TUM)','Munich','Public','QS #37','EUR 0-1,500 (admin)','Engineering, CS, Sciences'),
        ('LMU Munich','Munich','Public','QS #54','EUR 0-300','Medicine, Law, Humanities'),
        ('Heidelberg University','Heidelberg','Public','QS #47','EUR 0-1,500','Medicine, Sciences, Philosophy'),
        ('RWTH Aachen University','Aachen','Public','QS #106','EUR 0-300','Engineering, Technology'),
        ('Humboldt University of Berlin','Berlin','Public','QS #120','EUR 0-300','Social Sciences, Humanities'),
        ('Free University of Berlin','Berlin','Public','QS #98','EUR 0-300','Political Science, Medicine'),
        ('University of Freiburg','Freiburg','Public','QS #192','EUR 0-1,500','Environment, Medicine, Law'),
        ('TU Berlin','Berlin','Public','QS #154','EUR 0-300','Engineering, CS, Urban Planning'),
    ],
    'france.html': [
        ('Sorbonne University','Paris','Public','QS #59','EUR 2,770-3,770','Sciences, Medicine, Humanities'),
        ('PSL University','Paris','Public','QS #24','EUR 3,000-15,000','Sciences, Arts, Social Sciences'),
        ('Ecole Polytechnique','Palaiseau','Public','QS #48','EUR 12,000-15,000','Engineering, STEM, Mathematics'),
        ('HEC Paris','Jouy-en-Josas','Private','FT #2 MBA','EUR 20,000-45,000','MBA, Business, Management'),
        ('Sciences Po','Paris','Public','QS #242','EUR 10,000-14,000','Political Science, Law, IR'),
        ('University of Paris-Saclay','Saclay','Public','QS #15','EUR 2,770-3,770','Physics, Mathematics, Sciences'),
        ('ESSEC Business School','Cergy','Private','FT #5','EUR 15,000-30,000','Business, Finance, Marketing'),
        ('INSEAD','Fontainebleau','Private','FT #1 MBA','EUR 50,000+','MBA, Executive Education'),
    ],
    'ireland.html': [
        ('Trinity College Dublin','Dublin','Public','QS #81','EUR 18k-25k','All Disciplines'),
        ('University College Dublin','Dublin','Public','QS #126','EUR 16k-24k','Business, Law, Engineering'),
        ('University College Cork','Cork','Public','QS #292','EUR 15k-22k','Pharma, Medicine, Sciences'),
        ('NUI Galway','Galway','Public','QS #259','EUR 14k-20k','Marine Science, Engineering'),
        ('Dublin City University','Dublin','Public','QS #410','EUR 12k-16k','Engineering, Business, Tech'),
        ('University of Limerick','Limerick','Public','QS #420','EUR 12k-18k','Engineering, Business, Co-op'),
    ],
    'netherlands.html': [
        ('Delft University of Technology','Delft','Public','QS #47','EUR 10k-18k','Engineering, Architecture, CS'),
        ('University of Amsterdam','Amsterdam','Public','QS #53','EUR 10k-15k','Business, AI, Social Sciences'),
        ('Erasmus University Rotterdam','Rotterdam','Public','QS #176','EUR 10k-18k','Economics, Business, Medicine'),
        ('Eindhoven University of Technology','Eindhoven','Public','QS #120','EUR 12k-16k','Engineering, Design, CS'),
        ('Leiden University','Leiden','Public','QS #122','EUR 12k-18k','Law, Humanities, Sciences'),
        ('Utrecht University','Utrecht','Public','QS #107','EUR 10k-16k','Sciences, Medicine, Humanities'),
        ('University of Groningen','Groningen','Public','QS #139','EUR 9k-14k','Sciences, Business, AI'),
    ],
    'new-zealand.html': [
        ('University of Auckland','Auckland','Public','QS #68','NZD \u002428k-42k','All Disciplines'),
        ('University of Otago','Dunedin','Public','QS #206','NZD \u002425k-38k','Medicine, Health Sciences'),
        ('Victoria University of Wellington','Wellington','Public','QS #241','NZD \u002425k-35k','Law, Business, Design'),
        ('University of Canterbury','Christchurch','Public','QS #256','NZD \u002425k-35k','Engineering, Sciences'),
        ('Massey University','Palmerston North','Public','QS #239','NZD \u002424k-33k','Agriculture, Aviation, Vet'),
        ('University of Waikato','Hamilton','Public','QS #331','NZD \u002423k-32k','CS, Business, Education'),
    ],
    'spain.html': [
        ('IE University','Madrid/Segovia','Private','FT Top 10','EUR 12k-25k','Business, Tech, Law'),
        ('University of Barcelona','Barcelona','Public','QS #149','EUR 1k-3k','Sciences, Medicine, Arts'),
        ('Autonomous University of Madrid','Madrid','Public','QS #149','EUR 1.5k-4k','Sciences, Law, Medicine'),
        ('University of Navarra','Pamplona','Private','QS #252','EUR 10k-18k','Business, Communication, Law'),
        ('Pompeu Fabra University','Barcelona','Public','QS #226','EUR 2k-5k','Economics, Health, Media'),
        ('Carlos III University of Madrid','Madrid','Public','QS #280','EUR 2k-6k','Engineering, Business, Law'),
        ('University of Salamanca','Salamanca','Public','QS #601','EUR 1k-3k','Spanish Language, Humanities'),
    ],
    'switzerland.html': [
        ('ETH Zurich','Zurich','Public','QS #7','CHF 1,300/yr','Engineering, CS, Sciences'),
        ('EPFL','Lausanne','Public','QS #36','CHF 1,300/yr','Engineering, CS, Architecture'),
        ('University of Zurich','Zurich','Public','QS #69','CHF 2,000-4,000','Medicine, Law, Economics'),
        ('University of Geneva','Geneva','Public','QS #105','CHF 1,000-2,000','International Relations, Law'),
        ('University of Bern','Bern','Public','QS #120','CHF 1,500-2,500','Sciences, Medicine, Veterinary'),
        ('University of Basel','Basel','Public','QS #87','CHF 1,400-2,000','Pharma, Medicine, Sciences'),
        ('University of Lausanne','Lausanne','Public','QS #131','CHF 1,100-2,000','Business, Law, Geosciences'),
    ],
}


# ============================================================
# STANDARD BLOCKS (same for every page)
# ============================================================

def make_uni_table_html(country, unis):
    rows = ''
    for name, loc, utype, rank, fee, programs in unis:
        rows += f"""
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:0.8rem;font-weight:600">{name}</td>
      <td style="padding:0.8rem">{loc}</td>
      <td style="padding:0.8rem">{utype}</td>
      <td style="padding:0.8rem">{rank}</td>
      <td style="padding:0.8rem">{fee}</td>
      <td style="padding:0.8rem">{programs}</td>
     </tr>"""
    return f"""
<section class="section section-bg" id="university-comparison">
 <div class="container">
  <div class="section-header">
   <h2>University Comparison Table \u2014 {country}</h2>
   <p>Compare top institutions by ranking, fees, and program strengths at a glance.</p>
  </div>
  <div style="overflow-x:auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead>
     <tr style="background:#b91c1c;color:white">
      <th style="padding:0.8rem;text-align:left;white-space:nowrap">University</th>
      <th style="padding:0.8rem;text-align:left">Location</th>
      <th style="padding:0.8rem;text-align:left">Type</th>
      <th style="padding:0.8rem;text-align:left">Ranking</th>
      <th style="padding:0.8rem;text-align:left;white-space:nowrap">Annual Fees</th>
      <th style="padding:0.8rem;text-align:left">Key Programs</th>
     </tr>
    </thead>
    <tbody>{rows}
    </tbody>
   </table>
  </div>
 </div>
</section>"""


def make_roadmap_html(country):
    return f"""
<section class="section section-bg">
 <div class="container">
  <div class="section-header">
   <h2>{country} Study Pathway</h2>
   <p>Step-by-step support for admissions, visa processing, and pre-departure preparation.</p>
  </div>
  <div class="process-timeline">
   <div class="process-step">
    <div class="step-number">1</div>
    <div class="step-content">
     <h4>Profile Evaluation</h4>
     <p>We match your academic profile, test scores, and career goals to the best {country} programs.</p>
    </div>
   </div>
   <div class="process-step">
    <div class="step-number">2</div>
    <div class="step-content">
     <h4>Application Support</h4>
     <p>End-to-end application guidance including SOP, LORs, and document review.</p>
    </div>
   </div>
   <div class="process-step">
    <div class="step-number">3</div>
    <div class="step-content">
     <h4>Visa Processing</h4>
     <p>Complete student visa preparation, interview coaching, and documentation check.</p>
    </div>
   </div>
   <div class="process-step">
    <div class="step-number">4</div>
    <div class="step-content">
     <h4>Pre-Departure Support</h4>
     <p>Travel planning, accommodation guidance, and cultural orientation before departure.</p>
    </div>
   </div>
  </div>
 </div>
</section>"""


def make_cta_html(country):
    return f"""
<section class="cta-section" id="contact-form">
 <div class="container">
  <div class="cta-content">
   <h2>Start Your {country} Education Journey</h2>
   <p>Begin your application today with expert guidance from Voyage Horizon.</p>
   <div class="cta-buttons">
    <a class="btn btn-white btn-lg" href="../contact.html">Book Free Consultation</a>
    <a class="btn btn-outline btn-lg" href="tel:+919876543210" style="border-color:white;color:white;">Call Now</a>
   </div>
  </div>
 </div>
</section>"""


def make_form_html(country):
    return f"""
<section class="section">
 <div class="container">
  <div class="section-header">
   <h2>Contact Our {country} Study Advisors</h2>
   <p>Fill in your details and we'll contact you within 24 hours.</p>
  </div>
  <form action="../php/contact.php" class="contact-form" data-validate="" method="POST">
   <div class="form-group">
    <label class="form-label" for="name">Full Name *</label>
    <input class="form-input" id="name" name="name" placeholder="Enter your full name" required="" type="text"/>
   </div>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem">
    <div class="form-group">
     <label class="form-label" for="email">Email Address *</label>
     <input class="form-input" id="email" name="email" placeholder="Enter your email" required="" type="email"/>
    </div>
    <div class="form-group">
     <label class="form-label" for="phone">Phone Number *</label>
     <input class="form-input" id="phone" name="phone" placeholder="Enter your phone number" required="" type="tel"/>
    </div>
   </div>
   <div class="form-group">
    <label class="form-label" for="service">Interested In</label>
    <select class="form-input" id="service" name="service">
     <option value="">Select program</option>
     <option value="ms">Masters</option>
     <option value="mba">MBA</option>
     <option value="ug">Undergraduate</option>
     <option value="phd">PhD</option>
    </select>
   </div>
   <div class="form-group">
    <label class="form-label" for="message">Your Message</label>
    <textarea class="form-input" id="message" name="message" placeholder="Tell us about your goals and scores"></textarea>
   </div>
   <button class="btn btn-primary btn-lg w-full" type="submit">Send Message</button>
  </form>
 </div>
</section>"""


FOOTER_HTML = """
<footer class="footer">
 <div class="container">
  <div class="footer-grid">
   <div class="footer-brand">
    <div class="footer-logo"><img alt="Voyage Horizon" src="../images/logo.png" style="height:40px;width:auto;"/></div>
    <p>Your trusted partner for international education with personalized study visa services.</p>
   </div>
   <div class="footer-column">
    <h4>Quick Links</h4>
    <ul class="footer-links">
     <li><a href="../index.html">Home</a></li>
     <li><a href="../about.html">About Us</a></li>
     <li><a href="../study-visa.html">Study Visa</a></li>
     <li><a href="../mbbs-abroad.html">MBBS Abroad</a></li>
     <li><a href="../test-preparation.html">Test Preparation</a></li>
     <li><a href="../blogs.html">Blogs</a></li>
    </ul>
   </div>
   <div class="footer-column">
    <h4>Study Visa Destinations</h4>
    <ul class="footer-links">
     <li><a href="usa.html">USA</a></li>
     <li><a href="canada.html">Canada</a></li>
     <li><a href="germany.html">Germany</a></li>
     <li><a href="uk.html">UK</a></li>
     <li><a href="australia.html">Australia</a></li>
     <li><a href="new-zealand.html">New Zealand</a></li>
    </ul>
   </div>
   <div class="footer-column">
    <h4>Contact Us</h4>
    <ul class="footer-links footer-contact">
     <li><svg fill="none" height="16" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="16"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg><span>123 Education Street, Knowledge City</span></li>
     <li><svg fill="none" height="16" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="16"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg><span>+91 98765 43210</span></li>
     <li><svg fill="none" height="16" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="16"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg><span>info@voyagehorizon.com</span></li>
    </ul>
   </div>
  </div>
  <div class="footer-bottom"><p>&copy; 2026 Voyage Horizon. All rights reserved.</p></div>
 </div>
</footer>"""

WHATSAPP_HTML = """
<a aria-label="Chat on WhatsApp" class="whatsapp-float" href="https://wa.me/919876543210" target="_blank">
 <svg fill="currentColor" height="28" viewBox="0 0 24 24" width="28"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"></path></svg>
</a>"""

SCROLL_HTML = """
<button aria-label="Scroll to top" class="scroll-top">
 <svg fill="none" height="24" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" width="24"><polyline points="18 15 12 9 6 15"></polyline></svg>
</button>"""

SCRIPT_HTML = """<script src="../js/main.js"></script>"""


# ============================================================
# COUNTRY NAME MAP
# ============================================================
country_names = {
    'usa.html': 'USA', 'uk.html': 'UK', 'canada.html': 'Canada',
    'australia.html': 'Australia', 'germany.html': 'Germany', 'france.html': 'France',
    'ireland.html': 'Ireland', 'netherlands.html': 'Netherlands',
    'new-zealand.html': 'New Zealand', 'spain.html': 'Spain', 'switzerland.html': 'Switzerland'
}


# ============================================================
# PROCESS EACH FILE
# ============================================================
sv_dir = os.path.join(base, 'study_visa')

for fname in sorted(os.listdir(sv_dir)):
    if not fname.endswith('.html'):
        continue
    
    country = country_names.get(fname, fname.replace('.html','').replace('-',' ').title())
    fp = os.path.join(sv_dir, fname)
    
    with open(fp, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # 1. Remove duplicate/old university sections (keep only the one with id="universities")
    uni_sections = []
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            t = h2.get_text(strip=True)
            if any(k in t for k in ['Top Universities', 'Top Study Visa', 'Top French', 'Top UK',
                                     'Top German', 'Top Canadian', 'Top Australian', 'Top Dutch',
                                     'Top Kiwi', 'Top Spanish', 'Top Swiss', 'Leading',
                                     'University Comparison']):
                uni_sections.append(sec)
    
    # Keep max 1, remove rest
    if len(uni_sections) > 1:
        for dup in uni_sections[1:]:
            dup.decompose()
        print(f"  {fname}: Removed {len(uni_sections)-1} duplicate uni sections")
    
    # 2. Add University Comparison Table after the university cards section
    if fname in uni_table_data:
        # Remove old table if exists
        for sec in soup.find_all('section'):
            h2 = sec.find('h2')
            if h2 and 'University Comparison' in h2.get_text():
                sec.decompose()
        
        table_html = make_uni_table_html(country, uni_table_data[fname])
        table_soup = BeautifulSoup(table_html, 'html.parser')
        
        # Find the university cards section
        uni_sec = None
        for sec in soup.find_all('section'):
            h2 = sec.find('h2')
            if h2 and sec.get('id') == 'universities':
                uni_sec = sec
                break
            if h2 and 'Top Universit' in h2.get_text():
                uni_sec = sec
                break
        
        if uni_sec:
            uni_sec.insert_after(table_soup)
        else:
            # Insert after Why section
            why_sec = None
            for sec in soup.find_all('section'):
                h2 = sec.find('h2')
                if h2 and 'Why' in h2.get_text():
                    why_sec = sec
                    break
            if why_sec:
                why_sec.insert_after(table_soup)
    
    # 3. Ensure Roadmap section exists
    has_roadmap = False
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and any(k in h2.get_text() for k in ['Pathway', 'Roadmap', 'Process', 'Journey', 'Plan', 'Admission']):
            if not sec.find('form'):  # Don't count form sections
                has_roadmap = True
                break
    
    # 4. Ensure CTA section exists
    has_cta = bool(soup.find('section', class_='cta-section'))
    
    # 5. Ensure contact form section exists
    has_form = False
    for sec in soup.find_all('section'):
        if sec.find('form') and not sec.get('class'):
            has_form = True
            break
    
    # 6. Ensure footer exists
    has_footer = bool(soup.find('footer'))
    has_whatsapp = bool(soup.find('a', class_='whatsapp-float'))
    has_scroll = bool(soup.find('button', class_='scroll-top'))
    
    # Find insertion point (before footer or at end of body)
    body = soup.find('body')
    footer = soup.find('footer')
    
    # Build missing sections and insert before footer / end of body
    missing_parts = []
    
    if not has_roadmap:
        missing_parts.append(make_roadmap_html(country))
    if not has_cta:
        missing_parts.append(make_cta_html(country))
    if not has_form:
        missing_parts.append(make_form_html(country))
    
    if missing_parts:
        combined = '\n'.join(missing_parts)
        new_soup = BeautifulSoup(combined, 'html.parser')
        if footer:
            footer.insert_before(new_soup)
        elif body:
            body.append(new_soup)
    
    if not has_footer:
        footer_soup = BeautifulSoup(FOOTER_HTML, 'html.parser')
        if body:
            # Insert before </body>
            script_tag = soup.find('script', src='../js/main.js')
            if script_tag:
                script_tag.insert_before(footer_soup)
            else:
                body.append(footer_soup)
    
    if not has_whatsapp:
        wa_soup = BeautifulSoup(WHATSAPP_HTML, 'html.parser')
        body.append(wa_soup)
    
    if not has_scroll:
        sc_soup = BeautifulSoup(SCROLL_HTML, 'html.parser')
        body.append(sc_soup)
    
    # Ensure main.js is loaded
    if not soup.find('script', src='../js/main.js'):
        js_soup = BeautifulSoup(SCRIPT_HTML, 'html.parser')
        body.append(js_soup)
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"  OK: {fname} ({'fixed' if missing_parts or not has_footer else 'verified'})")

print("\nAll study_visa pages fully standardized.")
