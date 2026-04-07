import os
from bs4 import BeautifulSoup

base = r'c:\Users\admin\Downloads\New folder\mbbs_abroad'

mbbs_table_data = {
    'georgia.html': [
        ('Tbilisi State Medical University', 'Tbilisi', 'Public', 'Top NMC Listed', '$4,000 - 5,500', '15,000+ Students'),
        ('David Tvildiani Medical University', 'Tbilisi', 'Private', 'EU Accredited', '$5,000 - 6,000', 'English Medium'),
        ('European University', 'Tbilisi', 'Private', 'International Faculty', '$4,500 - 5,500', 'Modern Campus'),
        ('Geomedi Medical University', 'Tbilisi', 'Private', 'Affordable', '$4,000 - 5,000', 'NMC Approved')
    ],
    'russia.html': [
        ('Kazan State Medical University', 'Kazan', 'Public', 'Top Ranked', '$4,500 - 6,000', '3,000+ Indian Students'),
        ('St. Petersburg State Medical University', 'St. Petersburg', 'Public', 'Research Leader', '$5,000 - 7,000', 'NMC Approved'),
        ('Sechenov University Moscow', 'Moscow', 'Public', 'Russian Elite', '$6,000 - 8,000', 'Largest Medical Uni'),
        ('Volgograd State Medical University', 'Volgograd', 'Public', 'Affordable', '$4,000 - 5,500', 'English Programs')
    ],
    'kyrgyzstan.html': [
        ('Osh State University', 'Osh', 'Public', 'Top Choice', '$3,000 - 4,500', 'NMC Approved'),
        ('Jalal-Abad State University', 'Jalal-Abad', 'Public', 'Budget Friendly', '$3,000 - 4,000', 'English Medium'),
        ('International School of Medicine', 'Bishkek', 'Private', 'Modern Facilities', '$4,000 - 5,000', 'International Students'),
        ('Asian Medical Institute', 'Kant', 'Private', 'Research Focus', '$3,500 - 4,500', 'WHO Listed')
    ],
    'kazakhstan.html': [
        ('Astana Medical University', 'Astana', 'Public', 'Capital City', '$4,500 - 6,000', 'NMC Approved'),
        ('Al-Farabi Kazakh National University', 'Almaty', 'Public', 'Top Research', '$5,000 - 6,500', 'WHO Listed'),
        ('Karaganda Medical University', 'Karaganda', 'Public', 'Established', '$4,000 - 5,500', 'Indian Student Community'),
        ('South Kazakhstan Medical Academy', 'Shymkent', 'Public', 'Affordable', '$4,000 - 5,000', 'English Medium')
    ],
    'uzbekistan.html': [
        ('Andijan State Medical Institute', 'Andijan', 'Public', 'NMC Listed', '$4,000 - 5,000', 'English Medium'),
        ('Bukhara State Medical Institute', 'Bukhara', 'Public', 'Historical City', '$4,000 - 5,500', 'Affordable Fees'),
        ('Tashkent Medical Academy', 'Tashkent', 'Public', 'Capital City', '$4,500 - 6,000', 'Top Facilities'),
        ('Samarkand State Medical University', 'Samarkand', 'Public', 'UNESCO City', '$4,000 - 5,500', 'International Students')
    ],
    'nepal.html': [
        ('Kathmandu Medical College', 'Kathmandu', 'Private', 'Top Ranked', '$6,000 - 8,000', 'High FMGE Rate'),
        ('B.P. Koirala Institute of Health Sciences', 'Dharan', 'Public', 'Autonomous', '$7,000 - 9,000', 'NMC Approved'),
        ('Manipal College of Medical Sciences', 'Pokhara', 'Private', 'Manipal Brand', '$7,000 - 9,000', 'International Standards'),
        ('Patan Academy of Health Sciences', 'Lalitpur', 'Public', 'Community Focus', '$6,000 - 8,000', 'Government Aided')
    ],
    'egypt.html': [
        ('Cairo University Faculty of Medicine', 'Cairo', 'Public', '#1 Egypt', '$6,000 - 8,000', 'NMC Approved'),
        ('Alexandria University', 'Alexandria', 'Public', 'Top Medical School', '$5,500 - 7,500', 'Mediterranean City'),
        ('Ain Shams University', 'Cairo', 'Public', 'Research Leader', '$6,000 - 8,000', 'Large Indian Community'),
        ('Assiut University', 'Assiut', 'Public', 'Affordable', '$5,000 - 6,500', 'Upper Egypt Campus')
    ],
    'iraq.html': [
        ('University of Baghdad', 'Baghdad', 'Public', 'Oldest Uni', '$5,000 - 6,500', 'NMC Approved'),
        ('University of Basrah', 'Basrah', 'Public', 'Medical Excellence', '$4,500 - 6,000', 'Southern Iraq'),
        ('University of Mosul', 'Mosul', 'Public', 'Rebuilt Campus', '$4,000 - 5,500', 'Northern Iraq'),
        ('Al Nahrain University', 'Baghdad', 'Public', 'Modern Facilities', '$5,000 - 6,500', 'Baghdad Center')
    ],
    'italy.html': [
        ('University of Milan', 'Milan', 'Public', 'Fashion Capital', '€2,000 - 4,000', 'NMC Approved'),
        ('University of Bologna', 'Bologna', 'Public', 'Oldest Uni', '€2,000 - 4,000', 'History & Medicine'),
        ('Sapienza University of Rome', 'Rome', 'Public', 'Largest in EU', '€2,500 - 4,500', 'NMC Approved'),
        ('University of Padua', 'Padua', 'Public', 'Anatomical Theatre', '€2,000 - 4,000', 'Medical Heritage')
    ],
    'vietnam.html': [
        ('Hanoi Medical University', 'Hanoi', 'Public', 'Top Ranked', '$4,500 - 5,500', 'NMC Approved'),
        ('University of Medicine and Pharmacy', 'HCMC', 'Public', 'International', '$4,500 - 5,500', 'Southern Campus'),
        ('Pham Ngoc Thach University', 'HCMC', 'Public', 'Growing Rep', '$3,500 - 4,500', 'Affordable'),
        ('Hue University of Medicine', 'Hue', 'Public', 'Research Focus', '$3,500 - 4,500', 'Central Vietnam')
    ]
}

def make_mbbs_table_html(country, unis):
    rows = ''
    for name, loc, utype, rep, fee, note in unis:
        rows += f"""
     <tr style="border-bottom:1px solid #e5e7eb">
      <td style="padding:0.8rem;font-weight:600">{name}</td>
      <td style="padding:0.8rem">{loc}</td>
      <td style="padding:0.8rem">{utype}</td>
      <td style="padding:0.8rem">{rep}</td>
      <td style="padding:0.8rem">{fee}</td>
      <td style="padding:0.8rem">{note}</td>
     </tr>"""
    return f"""
<section class="section section-bg" id="university-comparison">
 <div class="container">
  <div class="section-header">
   <h2>University Comparison Table — MBBS in {country}</h2>
   <p>Compare top NMC-approved medical universities by tuition fees, location, and key highlights.</p>
  </div>
  <div style="overflow-x:auto">
   <table style="width:100%;border-collapse:collapse;background:white;border-radius:8px;box-shadow:0 4px 6px -1px rgb(0 0 0/0.1)">
    <thead>
     <tr style="background:#b91c1c;color:white">
      <th style="padding:0.8rem;text-align:left;white-space:nowrap">University Name</th>
      <th style="padding:0.8rem;text-align:left">Location</th>
      <th style="padding:0.8rem;text-align:left">Type</th>
      <th style="padding:0.8rem;text-align:left">Reputation</th>
      <th style="padding:0.8rem;text-align:left;white-space:nowrap">Annual Tuition</th>
      <th style="padding:0.8rem;text-align:left">Key Highlight</th>
     </tr>
    </thead>
    <tbody>{rows}
    </tbody>
   </table>
  </div>
 </div>
</section>"""

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.html'):
        continue
    
    country = fname.replace('.html', '').replace('-', ' ').title()
    fp = os.path.join(base, fname)
    with open(fp, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # 1. Target the duplicate section "Top NMC Approved" and remove it
    for sec in soup.find_all('section'):
        h2 = sec.find('h2')
        if h2:
            txt = h2.get_text(strip=True)
            if 'NMC Approved Universities in' in txt:
                sec.decompose()
                print(f"Removed duplicate NMC section in {fname}")
                
            # Also remove existing Comparison tables if any exists already to rebuild freshly
            if 'University Comparison' in txt:
                sec.decompose()
                
    # 2. Inject university comparison table immediately after Top MBBS Universities
    if fname in mbbs_table_data:
        table_html = make_mbbs_table_html(country, mbbs_table_data[fname])
        table_soup = BeautifulSoup(table_html, 'html.parser')
        
        target_sec = None
        for sec in soup.find_all('section'):
            h2 = sec.find('h2')
            if h2 and 'Top MBBS Universities in' in h2.get_text():
                target_sec = sec
                break
                
        if target_sec:
            target_sec.insert_after(table_soup)
            print(f"Injected comparison table in {fname}")
        else:
            print(f"Could NOT find target section in {fname}")
            
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("MBBS cleanup complete!")
