
# data_generator.py
import pandas as pd
import random
from scoring_logic import calculate_score

def generate_mock_data(num_rows=500):
    """
    Generates a DataFrame of mock leads and calculates their scores.
    """
    
    first_names = ["Sarah", "Michael", "Elena", "David", "Jessica", "Raj", "Wei", "Lucas", "Emily", "Robert", "Akash", "Priya", "John", "Maria", "Ahmed", "Sophie", "Daniel", "Lisa", "Tom", "Anna"]
    last_names = ["Chen", "Ross", "Rostova", "Miller", "Smith", "Patel", "Zhang", "Muller", "Johnson", "Williams", "Gupta", "Singh", "Lee", "Kim", "Garcia", "Martinez", "Lopez", "Gonzalez", "Wilson", "Anderson"]
    
    titles = [
        "Director of Toxicology", "Head of Preclinical Safety", "Junior Scientist", 
        "VP of Safety Assessment", "Research Associate", "Head of Discovery", 
        "Toxicologist", "Lab Technician", "Chief Scientific Officer", 
        "Senior Scientist", "PhD Candidate", "Principal Investigator", "Lab Manager"
    ]
    
    companies = [
        "BioTech Innovations", "StartUp X", "PharmaGiant", "LiverChip Inc", 
        "NextGen Therapies", "SafetyFirst Labs", "Basel Bio", "Cambridge InVitro",
        "Moderna Therapeutics", "Pfizer", "Vertex", "Novo Nordisk", "Gilead", 
        "Small Fish Bio", "Academic Lab A", "University Spinout"
    ]
    
    locations = [
        "Remote (Colorado)", "Cambridge, MA", "Basel, Switzerland", "Austin, TX", 
        "London, UK", "San Francisco, CA", "Remote (Florida)", "New York, NY",
        "San Diego, CA", "Seattle, WA", "Berlin, Germany", "Singapore", "Boston, MA"
    ]
    
    funding_rounds = ["Seed", "Series A", "Series B", "Public (IPO)", "Grant Funded", "Bootstrapped", "Unknown"]
    
    data = []
    
    for _ in range(num_rows):
        person = {
            "Name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "Title": random.choice(titles),
            "Company": random.choice(companies),
            "Location_Person": random.choice(locations),
            "Location_HQ": random.choice(locations),
            "Email": "contact@company.com", 
            "Funding_Status": random.choice(funding_rounds),
            # Weighted random choices to make data realistic
            "Uses_Similar_Tech": random.choices([True, False], weights=[0.3, 0.7])[0],
            "Recent_Publication": random.choices([True, False], weights=[0.2, 0.8])[0]
        }
        
        
        last_name = person["Name"].split()[-1].lower()
        company_domain = person["Company"].replace(" ", "").lower() + ".com"
        person["Email"] = f"{last_name}@{company_domain}"
        
        data.append(person)
        
    df = pd.DataFrame(data)
    
    
    df['Score'] = df.apply(calculate_score, axis=1)
    
    
    df = df.sort_values(by='Score', ascending=False)
    
    return df