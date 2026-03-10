def calculate_risk_and_interest(profile, loan_amount):
    # Calculate risk based on profile and loan amount

    #Modular design ml can be integrated here in future
    interest_rate = 0
    risk_score=0
    base_rate = 10.0 # Base interest rate

    #Rule1: Income vs Loan Ratio
    if loan_amount > (profile.monthly_income * 12):
        return {"approved": False,"interest_rate": interest_rate, "reason": "Loan amount too high for income"}

    #Rule2: Credit Score
    if profile.cibil_score < 600:
        return {"approved": False,"interest_rate": interest_rate, "reason": "Credit score too low"}
    
    #Rule3: Interest Rate Logic
    if profile.cibil_score >= 750:
        interest_rate = base_rate - 2.0 #Discount for good users
    else:
        interest_rate = base_rate + 2.0 #Higher rate for risky users

    return {
        "approved": True,
        "interest_rate": interest_rate,
        "reason": "Profile looks good"
    }