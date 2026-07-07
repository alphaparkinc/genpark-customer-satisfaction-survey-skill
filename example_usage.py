"""
example_usage.py -- Demonstrates CustomerSatisfactionSurveyClient
"""
from client import CustomerSatisfactionSurveyClient

def main():
    client = CustomerSatisfactionSurveyClient()
    result = client.calculate_nps([10, 9, 8, 5, 10, 9, 7, 4, 9, 8])
    print("[NPS Results]")
    print(f"NPS Score: {result['nps_score']}")
    print(f"Promoters: {result['percentage_promoters']}%")
    print(f"Detractors: {result['percentage_detractors']}%")

if __name__ == "__main__":
    main()
