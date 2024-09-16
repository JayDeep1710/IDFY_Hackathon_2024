from code_text import *
labels = ["Date of Birth","credit card Number","API Key","Bank Account Number","aadhar number" ,"company", "booking number","age", "city", "country", "personally identifiable information", "driver licence", "person", "address", "email", "passport number", "Social Security Number", "phone number"]


pii_sensitivity = {
    "Date of Birth": 2,  
    "credit card Number": 3,  
    "API Key": 3,  
    "Bank Account Number": 3,  
    "aadhar number": 3,  
    "company": 1,  # Low
    "booking number": 1,  # Low
    "age": 1,  # Low
    "city": 1,  # Low
    "country": 1,  # Low
    "personally identifiable information": 3,  # High
    "driver licence": 3,  # High
    "person": 2,  # Medium
    "address": 2,  # Medium
    "email": 2,  # Medium
    "passport number": 3,  # High
    "Social Security Number": 3,  # High
    "phone number": 2  # Medium
}


compliance_scores = {
    'gdpr': 'partially_compliant', 
    'ccpa': 'non_compliant' 
}

# Define data volume
data_volume = {
    'small': 1,   # < 1,000 records
    'medium': 2,  # 1,000 - 100,000 records
    'large': 3    # > 100,000 records
}

# Assign scores to compliance levels
compliance_values = {
    'fully_compliant': 1,
    'partially_compliant': 2,
    'non_compliant': 3
}

# Define weights
weights = {
    'pii_weight': 0.4,
    'volume_weight': 0.3,
    'compliance_weight': 0.3
}
compliance_status = {'gdpr': 'partially_compliant', 'ccpa': 'non_compliant'}

def calculate_risk_score(pii_data, data_vol):
    length=len(pii_data)+1
    total_pii_score = 0
    for data_type in pii_data:
        # Get the sensitivity score for each PII data type
        sensitivity_score = pii_sensitivity.get(data_type, 0)
        total_pii_score += sensitivity_score
        
    # Average PII sensitivity score
    average_pii_score = total_pii_score / length
    
    # Data volume score
    volume_score = data_volume[data_vol]
    

    gdpr_score = compliance_values[compliance_status['gdpr']]
    ccpa_score = compliance_values[compliance_status['ccpa']]
    compliance_score = max(gdpr_score, ccpa_score)
    
    risk_score = (
        (average_pii_score * weights['pii_weight']) +
        (volume_score * weights['volume_weight']) +
        (compliance_score * weights['compliance_weight'])
    )
    
    return get_score()


