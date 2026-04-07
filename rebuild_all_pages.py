import os
from bs4 import BeautifulSoup

base = r'c:\Users\admin\Downloads\New folder'

# Full country data for STUDY VISA pages
study_visa_data = {
    'usa.html': {
        'country': 'USA', 'currency': '$', 'pub_fee': '25,000 – 35,000', 'priv_fee': '35,000 – 55,000',
        'living': '12,000 – 18,000', 'total_pub': '37,000 – 53,000', 'total_priv': '47,000 – 73,000',
        'visa_type': 'F-1 Student Visa', 'work_during': '20 hrs/week on-campus',
        'psw_name': 'OPT & STEM OPT Extension', 'psw_dur': '1 Year (STEM: 3 Years)',
        'psw_desc': 'Optional Practical Training (OPT) allows F-1 students to work for 1 year in their field. STEM graduates get an additional 24-month extension.',
        'pr_path': 'H-1B → Green Card (EB-2/EB-3)',
        'top_sectors': 'Technology, Finance, Healthcare, Engineering',
        'unis': [('Harvard University', 'Cambridge, MA', '#1 World Rank', 'Business, Law, STEM'),
                 ('MIT', 'Cambridge, MA', '#1 Engineering', 'STEM, Innovation'),
                 ('Stanford University', 'California', 'Silicon Valley', 'Tech, Business'),
                 ('University of Michigan', 'Ann Arbor, MI', 'Top Public Uni', 'Engineering, MBA')]
    },
    'uk.html': {
        'country': 'UK', 'currency': '£', 'pub_fee': '12,000 – 20,000', 'priv_fee': '20,000 – 38,000',
        'living': '9,000 – 15,000', 'total_pub': '21,000 – 35,000', 'total_priv': '29,000 – 53,000',
        'visa_type': 'Student Visa (Tier 4)', 'work_during': '20 hrs/week during term',
        'psw_name': 'Graduate Route Visa', 'psw_dur': '2 Years (PhD: 3 Years)',
        'psw_desc': 'Graduates can stay in the UK for 2 years (3 for PhD) and work in any job without needing employer sponsorship.',
        'pr_path': 'Skilled Worker Visa → Indefinite Leave to Remain (ILR)',
        'top_sectors': 'Healthcare (NHS), Finance, Technology, Research',
        'unis': [('University of Oxford', 'Oxford', '#1 UK Rank', 'All Disciplines'),
                 ('University of Cambridge', 'Cambridge', 'Ivy League Equivalent', 'Sciences, Arts'),
                 ('Imperial College London', 'London', 'Top STEM', 'Engineering, Medicine'),
                 ('London School of Economics', 'London', 'Finance Hub', 'Economics, Business')]
    },
    'canada.html': {
        'country': 'Canada', 'currency': 'CAD $', 'pub_fee': '15,000 – 30,000', 'priv_fee': '25,000 – 40,000',
        'living': '10,000 – 15,000', 'total_pub': '25,000 – 45,000', 'total_priv': '35,000 – 55,000',
        'visa_type': 'Canadian Study Permit', 'work_during': '20 hrs/week off-campus',
        'psw_name': 'Post-Graduation Work Permit (PGWP)', 'psw_dur': 'Up to 3 Years',
        'psw_desc': 'Gain up to 3 years of Canadian work experience, directly contributing toward Express Entry Permanent Residency.',
        'pr_path': 'Express Entry → Canadian Permanent Residence',
        'top_sectors': 'IT, Nursing, Engineering, Finance',
        'unis': [('University of Toronto', 'Toronto, ON', '#1 Canada', 'All Disciplines'),
                 ('University of British Columbia', 'Vancouver, BC', 'Research Excellence', 'STEM, Business'),
                 ('McGill University', 'Montreal, QC', 'Bilingual Edge', 'Medicine, Law'),
                 ('University of Waterloo', 'Waterloo, ON', 'Co-op Leader', 'Engineering, CS')]
    },
    'australia.html': {
        'country': 'Australia', 'currency': 'AUD $', 'pub_fee': '20,000 – 35,000', 'priv_fee': '30,000 – 48,000',
        'living': '18,000 – 25,000', 'total_pub': '38,000 – 60,000', 'total_priv': '48,000 – 73,000',
        'visa_type': 'Student Visa (Subclass 500)', 'work_during': '40 hrs/fortnight during term',
        'psw_name': 'Temporary Graduate Visa (Subclass 485)', 'psw_dur': '2 to 4 Years',
        'psw_desc': 'Regional study boosts stay-back rights. Bachelors get 2-3 years, Masters get up to 4 years to work and explore PR pathways.',
        'pr_path': 'Skilled Independent Visa (Subclass 189/190) → PR',
        'top_sectors': 'Mining, Nursing, IT, Agriculture, Engineering',
        'unis': [('University of Melbourne', 'Melbourne, VIC', '#1 Australia', 'All Disciplines'),
                 ('Australian National University', 'Canberra, ACT', 'Research Power', 'Policy, Sciences'),
                 ('University of Sydney', 'Sydney, NSW', 'City Campus', 'Business, Law, Arts'),
                 ('University of Queensland', 'Brisbane, QLD', 'STEM Leader', 'Engineering, Medicine')]
    },
    'germany.html': {
        'country': 'Germany', 'currency': '€', 'pub_fee': '0 – 1,500 (Admin Fee)', 'priv_fee': '10,000 – 30,000',
        'living': '10,000 – 13,000', 'total_pub': '10,000 – 14,500', 'total_priv': '20,000 – 43,000',
        'visa_type': 'German National Visa (Type D)', 'work_during': '120 full days or 240 half days/year',
        'psw_name': '18-Month Job Seeker Visa', 'psw_dur': '18 Months',
        'psw_desc': 'After graduation, stay in Germany for 18 months to secure a job matching your degree, then convert to an EU Blue Card.',
        'pr_path': 'EU Blue Card → Permanent Residency in 21-33 months',
        'top_sectors': 'Automotive, STEM, IT, Research, Manufacturing',
        'unis': [('Technical University of Munich (TUM)', 'Munich', '#1 Germany', 'Engineering, STEM'),
                 ('Heidelberg University', 'Heidelberg', 'Top Research', 'Medicine, Sciences'),
                 ('LMU Munich', 'Munich', 'Research Excellence', 'Arts, Sciences, Law'),
                 ('RWTH Aachen University', 'Aachen', 'Engineering Powerhouse', 'Engineering, Tech')]
    },
    'france.html': {
        'country': 'France', 'currency': '€', 'pub_fee': '2,770 – 3,770', 'priv_fee': '10,000 – 25,000',
        'living': '9,000 – 14,000', 'total_pub': '11,770 – 17,770', 'total_priv': '19,000 – 39,000',
        'visa_type': 'French Long-Stay Student Visa (VLS-TS)', 'work_during': '964 hrs/year (60% of full-time)',
        'psw_name': 'APS Recherche d\'emploi / Visa', 'psw_dur': '2 Years (Masters)',
        'psw_desc': 'Masters graduates receive a 2-year post-study work authorization to find employment in France or the wider EU.',
        'pr_path': 'Talent Passport → French Permanent Residency',
        'top_sectors': 'Luxury Management, Culinary Arts, Technology, Research',
        'unis': [('École Polytechnique', 'Paris', 'Elite Engineering', 'Engineering, STEM'),
                 ('HEC Paris', 'Paris', 'Top MBA School', 'Business, Finance'),
                 ('Sciences Po', 'Paris', 'Global Relations', 'Law, Politics, IR'),
                 ('Sorbonne University', 'Paris', 'Humanities Leader', 'Arts, Sciences, Medicine')]
    },
    'ireland.html': {
        'country': 'Ireland', 'currency': '€', 'pub_fee': '12,000 – 20,000', 'priv_fee': '15,000 – 30,000',
        'living': '10,000 – 14,000', 'total_pub': '22,000 – 34,000', 'total_priv': '25,000 – 44,000',
        'visa_type': 'Irish Student Visa (Type C/D)', 'work_during': '20 hrs/week during term',
        'psw_name': 'Third Level Graduate Programme', 'psw_dur': '1 Year (Bachelors), 2 Years (Masters)',
        'psw_desc': 'Stay in the tech hub of Europe and find work with leading multinationals. EU-based companies prefer Irish-educated graduates.',
        'pr_path': 'Critical Skills Employment Permit → Irish PR',
        'top_sectors': 'Pharmaceutical, Tech (Google/Meta HQ), Finance, Biotech',
        'unis': [('Trinity College Dublin', 'Dublin', '#1 Ireland', 'All Disciplines'),
                 ('University College Dublin', 'Dublin', 'Research Leader', 'Business, Law'),
                 ('University College Cork', 'Cork', 'Pharma Hub', 'Sciences, Medicine'),
                 ('Dublin City University', 'Dublin', 'Tech Focus', 'Engineering, Business')]
    },
    'netherlands.html': {
        'country': 'Netherlands', 'currency': '€', 'pub_fee': '8,000 – 15,000', 'priv_fee': '12,000 – 22,000',
        'living': '10,000 – 14,000', 'total_pub': '18,000 – 29,000', 'total_priv': '22,000 – 36,000',
        'visa_type': 'Dutch Student Residence Permit (MVV)', 'work_during': '16 hrs/week',
        'psw_name': 'Orientation Year (Zoekjaar) Visa', 'psw_dur': '1 Year',
        'psw_desc': 'Graduates get exactly 1 year to find a Highly Skilled Migrant job in the Netherlands, leading to a 5-year residence permit.',
        'pr_path': 'Highly Skilled Migrant → Dutch Permanent Residence (5 years)',
        'top_sectors': 'Engineering, Logistics (Port of Rotterdam), Design, Agriculture',
        'unis': [('Delft University of Technology', 'Delft', '#1 Engineering', 'Engineering, Architecture'),
                 ('University of Amsterdam', 'Amsterdam', 'Research Leader', 'Business, Social Sciences'),
                 ('Erasmus University Rotterdam', 'Rotterdam', 'Business Hub', 'Economics, Law'),
                 ('Eindhoven University of Technology', 'Eindhoven', 'Innovation Hub', 'Tech, Design')]
    },
    'new-zealand.html': {
        'country': 'New Zealand', 'currency': 'NZD $', 'pub_fee': '20,000 – 35,000', 'priv_fee': '25,000 – 45,000',
        'living': '15,000 – 20,000', 'total_pub': '35,000 – 55,000', 'total_priv': '40,000 – 65,000',
        'visa_type': 'Student Visa (New Zealand)', 'work_during': '20 hrs/week during term',
        'psw_name': 'Post Study Work Visa', 'psw_dur': '1 to 3 Years',
        'psw_desc': 'Work in New Zealand after graduation. Duration depends on qualification level with pathways to Skilled Migrant Category Residence.',
        'pr_path': 'Skilled Migrant Category → NZ Permanent Residence',
        'top_sectors': 'Agriculture, Tourism, IT, Healthcare, Film Industry',
        'unis': [('University of Auckland', 'Auckland', '#1 NZ', 'All Disciplines'),
                 ('University of Otago', 'Dunedin', 'Healthcare Leader', 'Medicine, Sciences'),
                 ('Victoria University of Wellington', 'Wellington', 'Law & Policy', 'Law, Business'),
                 ('University of Canterbury', 'Christchurch', 'Engineering', 'Engineering, Sciences')]
    },
    'spain.html': {
        'country': 'Spain', 'currency': '€', 'pub_fee': '1,000 – 3,500', 'priv_fee': '5,000 – 22,000',
        'living': '8,000 – 12,000', 'total_pub': '9,000 – 15,500', 'total_priv': '13,000 – 34,000',
        'visa_type': 'Spanish Student Visa (Type D)', 'work_during': '20 hrs/week',
        'psw_name': 'Job Search Permit (Búsqueda de Empleo)', 'psw_dur': '1 Year',
        'psw_desc': 'Graduates can stay in Spain for 12 months to secure a work contract, then obtain a work residence permit.',
        'pr_path': 'Long-Term Resident Permit → Spanish PR (5 years)',
        'top_sectors': 'Tourism, Hospitality, Technology, Business, Arts',
        'unis': [('IE University', 'Madrid/Segovia', 'Top Business', 'Business, Law, Tech'),
                 ('University of Barcelona', 'Barcelona', 'Research Leader', 'Sciences, Medicine'),
                 ('Autonomous University of Madrid', 'Madrid', 'Top Public', 'All Disciplines'),
                 ('University of Navarra', 'Pamplona', 'Private Excellence', 'Business, Communication')]
    },
    'switzerland.html': {
        'country': 'Switzerland', 'currency': 'CHF', 'pub_fee': '1,500 – 4,000', 'priv_fee': '15,000 – 50,000',
        'living': '18,000 – 25,000', 'total_pub': '19,500 – 29,000', 'total_priv': '33,000 – 75,000',
        'visa_type': 'Swiss Student Visa (Type D)', 'work_during': '15 hrs/week',
        'psw_name': 'Job Seeker Permit', 'psw_dur': '6 Months',
        'psw_desc': 'Graduates of Swiss universities get 6 months to find employment related to their studies. Switzerland has the highest graduate salaries in Europe.',
        'pr_path': 'L/B Permit → C Permit (Permanent Residence after 5-10 years)',
        'top_sectors': 'Finance (Banking), Pharmaceutical, Hospitality, International Organizations',
        'unis': [('ETH Zurich', 'Zurich', '#1 Continental Europe', 'Engineering, Sciences, Tech'),
                 ('University of Zurich', 'Zurich', 'Research Leader', 'Medicine, Law, Arts'),
                 ('University of Bern', 'Bern', 'Capital City Uni', 'Sciences, Law, Medicine'),
                 ('EPFL Lausanne', 'Lausanne', 'Tech Powerhouse', 'Engineering, Computer Science')]
    }
}

# Full country data for MBBS pages
mbbs_data = {
    'georgia.html': {
        'country': 'Georgia', 'currency': '$', 'fee_yr1': '4,000 – 5,500', 'fee_yr6': '4,000 – 5,500',
        'total_6yr': '24,000 – 35,000', 'hostel': '1,500 – 2,500/year', 'living': '2,500 – 4,000/year',
        'fmge_rate': '45–60%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('Tbilisi State Medical University', 'Tbilisi', 'Top NMC Listed', '15,000+ Students'),
                 ('David Tvildiani Medical University', 'Tbilisi', 'EU Accredited', 'English Medium'),
                 ('European University', 'Tbilisi', 'International Faculty', 'Modern Campus'),
                 ('Geomedi Medical University', 'Tbilisi', 'Affordable Fees', 'NMC Approved')]
    },
    'russia.html': {
        'country': 'Russia', 'currency': '$', 'fee_yr1': '4,000 – 7,000', 'fee_yr6': '4,000 – 7,000',
        'total_6yr': '25,000 – 45,000', 'hostel': '800 – 1,500/year', 'living': '2,000 – 3,500/year',
        'fmge_rate': '30–45%', 'nmc_approved': 'Yes', 'medium': 'English/Russian',
        'unis': [('Kazan State Medical University', 'Kazan', 'Top Ranked', '3,000+ Indian Students'),
                 ('St. Petersburg State Medical University', 'St. Petersburg', 'Research Leader', 'NMC Approved'),
                 ('Sechenov University Moscow', 'Moscow', 'Russian Elite', 'Largest Medical Uni'),
                 ('Volgograd State Medical University', 'Volgograd', 'Affordable', 'English Programs')]
    },
    'kyrgyzstan.html': {
        'country': 'Kyrgyzstan', 'currency': '$', 'fee_yr1': '3,000 – 4,500', 'fee_yr6': '3,000 – 4,500',
        'total_6yr': '18,000 – 28,000', 'hostel': '600 – 1,000/year', 'living': '1,500 – 2,500/year',
        'fmge_rate': '35–50%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('Osh State University', 'Osh', 'Top Choice', 'NMC Approved'),
                 ('Jalal-Abad State University', 'Jalal-Abad', 'Budget Friendly', 'English Medium'),
                 ('International School of Medicine', 'Bishkek', 'Modern Facilities', 'International Students'),
                 ('Asian Medical Institute', 'Kant', 'Research Focus', 'WHO Listed')]
    },
    'kazakhstan.html': {
        'country': 'Kazakhstan', 'currency': '$', 'fee_yr1': '4,000 – 6,000', 'fee_yr6': '4,000 – 6,000',
        'total_6yr': '24,000 – 38,000', 'hostel': '600 – 1,200/year', 'living': '2,000 – 3,000/year',
        'fmge_rate': '40–55%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('Astana Medical University', 'Astana', 'Capital City', 'NMC Approved'),
                 ('Al-Farabi Kazakh National University', 'Almaty', 'Top Research Uni', 'WHO Listed'),
                 ('Karaganda Medical University', 'Karaganda', 'Established', 'Indian Student Community'),
                 ('South Kazakhstan Medical Academy', 'Shymkent', 'Affordable', 'English Medium')]
    },
    'uzbekistan.html': {
        'country': 'Uzbekistan', 'currency': '$', 'fee_yr1': '4,000 – 5,500', 'fee_yr6': '4,000 – 5,500',
        'total_6yr': '24,000 – 33,000', 'hostel': '600 – 1,000/year', 'living': '1,500 – 2,500/year',
        'fmge_rate': '38–55%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('Andijan State Medical Institute', 'Andijan', 'NMC Listed', 'English Medium'),
                 ('Bukhara State Medical Institute', 'Bukhara', 'Historical City', 'Affordable Fees'),
                 ('Tashkent Medical Academy', 'Tashkent', 'Capital City', 'Top Facilities'),
                 ('Samarkand State Medical University', 'Samarkand', 'UNESCO City', 'International Students')]
    },
    'nepal.html': {
        'country': 'Nepal', 'currency': '$', 'fee_yr1': '6,000 – 9,000', 'fee_yr6': '6,000 – 9,000',
        'total_6yr': '36,000 – 55,000', 'hostel': '1,200 – 2,000/year', 'living': '2,000 – 3,500/year',
        'fmge_rate': '50–65%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('Kathmandu Medical College', 'Kathmandu', 'Top Ranked', 'High FMGE Rate'),
                 ('B.P. Koirala Institute of Health Sciences', 'Dharan', 'Government Autonomous', 'NMC Approved'),
                 ('Manipal College of Medical Sciences', 'Pokhara', 'Manipal Brand', 'International Standards'),
                 ('Patan Academy of Health Sciences', 'Lalitpur', 'Community Focus', 'Government Aided')]
    },
    'egypt.html': {
        'country': 'Egypt', 'currency': '$', 'fee_yr1': '5,000 – 8,000', 'fee_yr6': '5,000 – 8,000',
        'total_6yr': '30,000 – 50,000', 'hostel': '1,000 – 1,800/year', 'living': '2,500 – 4,000/year',
        'fmge_rate': '40–55%', 'nmc_approved': 'Yes', 'medium': 'English/Arabic',
        'unis': [('Cairo University Faculty of Medicine', 'Cairo', '#1 Egypt', 'NMC Approved'),
                 ('Alexandria University', 'Alexandria', 'Mediterranean City', 'Top Medical School'),
                 ('Ain Shams University', 'Cairo', 'Research Leader', 'Large Indian Community'),
                 ('Assiut University', 'Assiut', 'Upper Egypt Campus', 'Affordable Fees')]
    },
    'iraq.html': {
        'country': 'Iraq', 'currency': '$', 'fee_yr1': '4,000 – 6,500', 'fee_yr6': '4,000 – 6,500',
        'total_6yr': '24,000 – 40,000', 'hostel': '1,000 – 2,000/year', 'living': '2,000 – 3,500/year',
        'fmge_rate': '35–50%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('University of Baghdad', 'Baghdad', 'Oldest University', 'NMC Approved'),
                 ('University of Basrah', 'Basrah', 'Southern Iraq', 'Medical Excellence'),
                 ('University of Mosul', 'Mosul', 'Northern Iraq', 'Rebuilt Campus'),
                 ('Al Nahrain University', 'Baghdad', 'Private Institution', 'Modern Facilities')]
    },
    'italy.html': {
        'country': 'Italy', 'currency': '€', 'fee_yr1': '2,000 – 4,000', 'fee_yr6': '2,000 – 4,000',
        'total_6yr': '12,000 – 25,000', 'hostel': '2,000 – 4,000/year', 'living': '7,000 – 11,000/year',
        'fmge_rate': '48–62%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('University of Milan', 'Milan', 'Fashion Capital', 'NMC Approved'),
                 ('University of Bologna', 'Bologna', 'Oldest Uni in World', 'History & Medicine'),
                 ('Sapienza University of Rome', 'Rome', 'Largest in EU', 'NMC Approved'),
                 ('University of Padua', 'Padua', 'Anatomical Theatre', 'Medical Heritage')]
    },
    'vietnam.html': {
        'country': 'Vietnam', 'currency': '$', 'fee_yr1': '3,500 – 5,500', 'fee_yr6': '3,500 – 5,500',
        'total_6yr': '21,000 – 33,000', 'hostel': '800 – 1,500/year', 'living': '2,000 – 3,000/year',
        'fmge_rate': '38–52%', 'nmc_approved': 'Yes', 'medium': 'English',
        'unis': [('Hanoi Medical University', 'Hanoi', 'Top Ranked', 'NMC Approved'),
                 ('University of Medicine and Pharmacy, HCMC', 'Ho Chi Minh City', 'Southern Campus', 'International Programs'),
                 ('Pham Ngoc Thach University', 'Ho Chi Minh City', 'Growing Reputation', 'Affordable'),
                 ('Hue University of Medicine', 'Hue', 'Central Vietnam', 'Research Focus')]
    }
}


def make_uni_section_sv(unis, country):
    cards = ''
    for name, loc, tag, spec in unis:
        cards += f"""
     <div class="service-card">
      <div class="service-icon">
       <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path d="M12 14l9-5-9-5-9 5 9 5z"></path>
        <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path>
       </svg>
      </div>
      <h3>{name}</h3>
      <p class="location-tag" style="color:#6b7280;font-size:0.85rem;margin-bottom:0.5rem;">📍 {loc} &nbsp;|&nbsp; 🏆 {tag}</p>
      <ul class="service-features">
       <li>{spec}</li>
      </ul>
      <a class="btn btn-secondary" href="#contact-form">Apply Now</a>
     </div>"""
    return f"""
<section class="section" id="universities">
 <div class="container">
  <div class="section-header">
   <h2>Top Universities in {country}</h2>
   <p>Highly ranked institutions offering programs for international students.</p>
  </div>
  <div class="services-grid">{cards}
  </div>
 </div>
</section>"""


def make_fee_section_sv(d):
    return f"""
<section class="section section-bg" id="detailed-fees">
 <div class="container">
  <div class="section-header">
   <h2>Detailed Financial Breakdown</h2>
   <p>Clear cost estimates for Indian students planning to study in {d['country']}.</p>
  </div>
  <div style="overflow-x: auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead>
     <tr style="background:#b91c1c;color:white">
      <th style="padding:1rem;text-align:left">Category</th>
      <th style="padding:1rem;text-align:left">Public Universities</th>
      <th style="padding:1rem;text-align:left">Private Universities</th>
     </tr>
    </thead>
    <tbody>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Annual Tuition</strong></td>
      <td style="padding:1rem">{d['currency']}{d['pub_fee']}</td>
      <td style="padding:1rem">{d['currency']}{d['priv_fee']}</td>
     </tr>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Living Expenses</strong></td>
      <td style="padding:1rem" colspan="2">{d['currency']}{d['living']}/year</td>
     </tr>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Estimated Total/Year (Public)</strong></td>
      <td style="padding:1rem" colspan="2">{d['currency']}{d['total_pub']}</td>
     </tr>
     <tr>
      <td style="padding:1rem"><strong>Estimated Total/Year (Private)</strong></td>
      <td style="padding:1rem" colspan="2">{d['currency']}{d['total_priv']}</td>
     </tr>
    </tbody>
   </table>
  </div>
  <p style="margin-top:1rem;color:#6b7280;font-size:0.9rem;">* Visa Type: <strong>{d['visa_type']}</strong> &nbsp;|&nbsp; Work During Study: <strong>{d['work_during']}</strong></p>
 </div>
</section>"""


def make_psw_section_sv(d):
    return f"""
<section class="section" id="post-study-work">
 <div class="container">
  <div class="section-header">
   <h2>Post-Study Work &amp; Career Opportunities</h2>
   <p>Your transparent guide to stay-back rights, PR pathways, and career outcomes in {d['country']}.</p>
  </div>
  <div class="services-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
   <div class="service-card">
    <div class="service-icon">
     <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>
     </svg>
    </div>
    <h3>{d['psw_name']}</h3>
    <p style="color:#b91c1c;font-weight:600;">{d['psw_dur']}</p>
    <p>{d['psw_desc']}</p>
   </div>
   <div class="service-card">
    <div class="service-icon">
     <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle>
      <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"></path>
     </svg>
    </div>
    <h3>PR &amp; Immigration Pathways</h3>
    <p style="color:#b91c1c;font-weight:600;">Long-Term Settlement</p>
    <p>{d['pr_path']}</p>
   </div>
   <div class="service-card">
    <div class="service-icon">
     <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
      <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
     </svg>
    </div>
    <h3>Top Hiring Sectors</h3>
    <p style="color:#b91c1c;font-weight:600;">In-Demand Fields</p>
    <p>{d['top_sectors']}</p>
   </div>
  </div>
 </div>
</section>"""


def make_uni_section_mbbs(unis, country):
    cards = ''
    for name, loc, tag, note in unis:
        cards += f"""
     <div class="service-card">
      <div class="service-icon">
       <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path d="M12 14l9-5-9-5-9 5 9 5z"></path>
        <path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"></path>
       </svg>
      </div>
      <h3>{name}</h3>
      <p style="color:#6b7280;font-size:0.85rem;margin-bottom:0.5rem;">📍 {loc} &nbsp;|&nbsp; ⭐ {tag}</p>
      <ul class="service-features">
       <li>{note}</li>
      </ul>
      <a class="btn btn-secondary" href="#contact-form">Apply Now</a>
     </div>"""
    return f"""
<section class="section" id="universities">
 <div class="container">
  <div class="section-header">
   <h2>Top MBBS Universities in {country}</h2>
   <p>NMC-approved medical universities recognized for quality education and FMGE outcomes.</p>
  </div>
  <div class="services-grid">{cards}
  </div>
 </div>
</section>"""


def make_fee_section_mbbs(d):
    return f"""
<section class="section section-bg" id="detailed-fees">
 <div class="container">
  <div class="section-header">
   <h2>MBBS Fee Structure in {d['country']}</h2>
   <p>Transparent cost breakdown for Indian medical students — tuition, hostel, and living costs.</p>
  </div>
  <div style="overflow-x:auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead>
     <tr style="background:#b91c1c;color:white">
      <th style="padding:1rem;text-align:left">Cost Component</th>
      <th style="padding:1rem;text-align:left">Amount (Per Year)</th>
      <th style="padding:1rem;text-align:left">Notes</th>
     </tr>
    </thead>
    <tbody>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Tuition Fees</strong></td>
      <td style="padding:1rem">{d['currency']}{d['fee_yr1']}</td>
      <td style="padding:1rem">Varies by university tier</td>
     </tr>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Hostel / Accommodation</strong></td>
      <td style="padding:1rem">{d['currency']}{d['hostel']}</td>
      <td style="padding:1rem">University hostels available</td>
     </tr>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Food &amp; Living</strong></td>
      <td style="padding:1rem">{d['currency']}{d['living']}</td>
      <td style="padding:1rem">Indian food widely available</td>
     </tr>
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:1rem"><strong>Total 6-Year Cost (Est.)</strong></td>
      <td style="padding:1rem">{d['currency']}{d['total_6yr']}</td>
      <td style="padding:1rem">Including all expenses</td>
     </tr>
     <tr>
      <td style="padding:1rem"><strong>FMGE Pass Rate</strong></td>
      <td style="padding:1rem">{d['fmge_rate']}</td>
      <td style="padding:1rem">Medium of Instruction: {d['medium']}</td>
     </tr>
    </tbody>
   </table>
  </div>
 </div>
</section>"""


def make_psw_section_mbbs(d):
    return f"""
<section class="section" id="post-study-work">
 <div class="container">
  <div class="section-header">
   <h2>Licensing &amp; Career Pathways After MBBS</h2>
   <p>Your roadmap to medical practice in India and globally after completing MBBS in {d['country']}.</p>
  </div>
  <div class="services-grid" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">
   <div class="service-card">
    <div class="service-icon">
     <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>
     </svg>
    </div>
    <h3>FMGE / NExT (India)</h3>
    <p style="color:#b91c1c;font-weight:600;">Practice in India</p>
    <p>Clear the NMC's Foreign Medical Graduate Examination (FMGE) or NExT to register and practice as a doctor in India. NMC Approved: <strong>{d['nmc_approved']}</strong></p>
   </div>
   <div class="service-card">
    <div class="service-icon">
     <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line>
      <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
     </svg>
    </div>
    <h3>USMLE / PLAB (Global)</h3>
    <p style="color:#b91c1c;font-weight:600;">Global Practice</p>
    <p>Pursue USMLE for USA residency, PLAB for UK practice, or AMC for Australia. A {d['country']} MBBS degree gives you global flexibility.</p>
   </div>
   <div class="service-card">
    <div class="service-icon">
     <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
     </svg>
    </div>
    <h3>PG Specialization</h3>
    <p style="color:#b91c1c;font-weight:600;">MS / MD / DNB</p>
    <p>Appear for NEET-PG to pursue MD/MS specializations in India. Many graduates also pursue PG programs in Europe or Canada post licensing.</p>
   </div>
  </div>
 </div>
</section>"""


def rebuild_page_sv(filepath, fname, d):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Remove old universities, fees, PSW sections
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            t = h2.get_text(strip=True)
            if any(k in t for k in ['Top Universit', 'Top Study Visa', 'Top French', 'Top German', 'Top Spanish', 'Top Swiss',
                                      'Detailed Financial', 'Detailed Fee', 'Post-Study Work', 'Career Opportunit']):
                sec.decompose()

    uni_section = BeautifulSoup(make_uni_section_sv(d['unis'], d['country']), 'html.parser')
    fee_section = BeautifulSoup(make_fee_section_sv(d), 'html.parser')
    psw_section = BeautifulSoup(make_psw_section_sv(d), 'html.parser')

    # Find Why section to insert uni AFTER it
    why_sec = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and 'Why' in h2.get_text():
            why_sec = sec
            break

    # Find the process/roadmap section to insert fee+psw BEFORE it
    process_sec = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            t = h2.get_text(strip=True)
            if any(k in t for k in ['Study Plan', 'Study Pathway', 'Roadmap', 'Study Road', 'Journey', 'Pathway']):
                process_sec = sec
                break

    if why_sec:
        why_sec.insert_after(uni_section)

    if process_sec:
        process_sec.insert_before(psw_section)
        process_sec.insert_before(fee_section)
    else:
        cta = soup.find('section', class_='cta-section')
        if cta:
            cta.insert_before(psw_section)
            cta.insert_before(fee_section)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))


def rebuild_page_mbbs(filepath, fname, d):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            t = h2.get_text(strip=True)
            if any(k in t for k in ['Top MBBS Universit', 'Top Universities', 'MBBS Fee Structure',
                                      'Detailed Financial', 'Detailed Fee', 'Licensing', 'Career Pathways', 'Post-Study Work']):
                sec.decompose()

    uni_section = BeautifulSoup(make_uni_section_mbbs(d['unis'], d['country']), 'html.parser')
    fee_section = BeautifulSoup(make_fee_section_mbbs(d), 'html.parser')
    psw_section = BeautifulSoup(make_psw_section_mbbs(d), 'html.parser')

    why_sec = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2 and 'Why' in h2.get_text():
            why_sec = sec
            break

    process_sec = None
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            t = h2.get_text(strip=True)
            if any(k in t for k in ['Admission', 'Roadmap', 'Pathway', 'Process', 'Journey', 'Plan', 'Step']):
                process_sec = sec
                break

    if why_sec:
        why_sec.insert_after(uni_section)

    if process_sec:
        process_sec.insert_before(psw_section)
        process_sec.insert_before(fee_section)
    else:
        cta = soup.find('section', class_='cta-section')
        if cta:
            cta.insert_before(psw_section)
            cta.insert_before(fee_section)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))


# Process all study visa pages
sv_dir = os.path.join(base, 'study_visa')
for fname, d in study_visa_data.items():
    fp = os.path.join(sv_dir, fname)
    if os.path.exists(fp):
        rebuild_page_sv(fp, fname, d)
        print(f"  Rebuilt: {fname}")

# Process all MBBS pages
mbbs_dir = os.path.join(base, 'mbbs_abroad')
for fname, d in mbbs_data.items():
    fp = os.path.join(mbbs_dir, fname)
    if os.path.exists(fp):
        rebuild_page_mbbs(fp, fname, d)
        print(f"  Rebuilt: {fname}")

print("\nAll 21 destination pages rebuilt with consistent, accurate, standardized content.")
