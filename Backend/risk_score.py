from collections import defaultdict

def calculate_risk_score(data):
    sensitivity_scores = {
        "Date of Birth": 4,
        "credit card Number": 5,
        "API Key": 5,
        "Bank Account Number": 5,
        "aadhar number": 5,
        "company": 2,
        "booking number": 2,
        "age": 2,
        "city": 1,
        "country": 1,
        "personally identifiable information": 5,
        "driver licence": 4,
        "person": 2,
        "address": 2,
        "email": 3,
        "passport number": 5,
        "Social Security Number": 5,
        "phone number": 4,
        "pan": 1,  # Sensitivity score for images
        "dl": 1,   # Sensitivity score for driver's license images
        "PII identified images": 2  # Sensitivity score for identifiable PII in images
    }

    pii_count = defaultdict(int)

    # Count occurrences of each PII label
    for category, files in data.items():
        for file, content in files.items():
            if isinstance(content, dict):
                for label, pii_type in content.items():
                    pii_count[pii_type] += 1

    # Calculate weighted sensitivity and volume for each PII type
    final_pii_sensitivity_value = 0
    total_data = 0
    for key, items in pii_count.items():
        final_pii_sensitivity_value += items * sensitivity_scores.get(key, 1)
        total_data += items

    avg_pii_sens_score = final_pii_sensitivity_value / total_data if total_data > 0 else 0

    weighted_volume = 0
    for pii_type, count in pii_count.items():
        if pii_type in sensitivity_scores:
            if count <= 2:
                weighted_volume += count
            elif count <= 4:
                weighted_volume += 2 * count
            elif count <= 5:
                weighted_volume += 3 * count
            elif count <= 9:
                weighted_volume += 4 * count
            else:
                weighted_volume += 5 * count

    final_average_weighted_score = weighted_volume / total_data if total_data > 0 else 0

    # Sensitivity ratings for regulatory compliance
    sensitivity_ratings = {
        "Date of Birth": {"GDPR": 2, "CCPA": 2, "HIPAA": 1},
        "credit card Number": {"GDPR": 5, "CCPA": 5, "HIPAA": 3},
        "API Key": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},
        "Bank Account Number": {"GDPR": 5, "CCPA": 5, "HIPAA": 3},
        "aadhar number": {"GDPR": 4, "CCPA": 3, "HIPAA": 1},
        "company": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},
        "booking number": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},
        "age": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},
        "city": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},
        "country": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},
        "personally identifiable information": {"GDPR": 5, "CCPA": 5, "HIPAA": 5},
        "driver licence": {"GDPR": 4, "CCPA": 4, "HIPAA": 2},
        "person": {"GDPR": 5, "CCPA": 5, "HIPAA": 5},
        "address": {"GDPR": 3, "CCPA": 3, "HIPAA": 1},
        "email": {"GDPR": 3, "CCPA": 3, "HIPAA": 1},
        "passport number": {"GDPR": 5, "CCPA": 4, "HIPAA": 1},
        "Social Security Number": {"GDPR": 5, "CCPA": 5, "HIPAA": 5},
        "phone number": {"GDPR": 3, "CCPA": 3, "HIPAA": 1},
        "pan": {"GDPR": 1, "CCPA": 1, "HIPAA": 1},  # Pan card images
        "dl": {"GDPR": 2, "CCPA": 2, "HIPAA": 1},  # Driver's license images
        "PII identified images": {"GDPR": 3, "CCPA": 3, "HIPAA": 2}  # PII identified in images
    }

    regulatory_compliance_score = 0
    for key, value in pii_count.items():
        reg_score = (sensitivity_ratings[key]["GDPR"] + sensitivity_ratings[key]["CCPA"] + sensitivity_ratings[key]["HIPAA"]) / 3
        regulatory_compliance_score += reg_score * value

    avg_reg_compliance_score = regulatory_compliance_score / total_data if total_data > 0 else 0

    # Calculate overall risk score
    overall_risk_score = 0.4 * avg_pii_sens_score + 0.3 * final_average_weighted_score + 0.3 * avg_reg_compliance_score
    return float(f"{overall_risk_score:.2f}")
