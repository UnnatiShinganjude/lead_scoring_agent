
# scoring_logic.py
def calculate_score(row):

    score = 0
    #base score
    target_roles = ['toxicology', 'safety', 'hepatic', '3d', 'preclinical', 'discovery', 'research']
    if any(keyword in row['Title'].lower() for keyword in target_roles):
        score += 30
        
    #funding status
    if row['Funding_Status'] in ['Series A', 'Series B']:
        score += 20
        
  #tech usage
    if row['Uses_Similar_Tech']:
        score += 15
        
    #location
    hubs = ['boston', 'cambridge', 'bay area', 'basel', 'london', 'oxford', 'san francisco', 'new york']
    if any(hub in row['Location_HQ'].lower() for hub in hubs):
        score += 10
        
    #recent publication
    if row['Recent_Publication']:
        score += 40
        
   
    return min(score, 100)