# Task 3: Filter Claims by Date Range
# Part A:
# Write a function to filter claims for a given patient within a
# specific date range. Return the filtered claims as a list.

from datetime import datetime

class Solution:
    def filter_claims_by_date_range(self, patient_id, start_date, end_date, data):
        """
        Filter claims for a given patient within a specific date range.
        
        Args:
            patient_id (str): The ID of the patient whose claims to filter.
            start_date (str): The start date of the range in "YYYY-MM-DD" format.
            end_date (str): The end date of the range in "YYYY-MM-DD" format.
            data (dict): The JSON data containing patients and claims.
        
        Returns:
            list: A list of filtered claims that fall within the date range.
        """
        # Convert the start and end dates from string to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        filtered_claims = []  # List to store the filtered claims
        
        # Find the patient by ID and filter their claims by date range
        for patient in data["patients"]:
            if patient["id"] == patient_id:
                for claim in patient["claims"]:
                    claim_date = datetime.strptime(claim["date"], "%Y-%m-%d")
                    if start_date <= claim_date <= end_date:
                        filtered_claims.append(claim)
        return filtered_claims  # Return the filtered list of claims

def main():
    data = {
        "patients": [
            {
                "id": "P001",
                "claims": [
                    {"id": "C001", "amount": 100, "billingCode": "B001", "date": "2024-01-01"},
                    {"id": "C002", "amount": 200, "billingCode": "B001", "date": "2024-01-05"},
                    {"id": "C003", "amount": 150, "billingCode": "B002", "date": "2024-01-10"},
                    {"id": "C004", "amount": 120, "billingCode": "B001", "date": "2024-01-15"},
                    {"id": "C005", "amount": 180, "billingCode": "B002", "date": "2024-01-20"}
                ]
            }
        ]
    }
    
    patient_id = "P001"
    start_date = "2024-01-05"
    end_date = "2024-01-15"
    solution = Solution()
    filtered_claims = solution.filter_claims_by_date_range(patient_id, start_date, end_date, data)
    print("Filtered Claims:", filtered_claims) # Expected output: C002, C003, C004

if __name__ == '__main__':
    main()
