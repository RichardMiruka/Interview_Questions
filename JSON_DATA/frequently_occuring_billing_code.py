# Part B:
# Using the same JSON data, write a function to find the most
# frequently occurring billing code for a given patient ID.

from collections import Counter

class Solution:
    def get_most_frequent_billing_code(self, patient_id, data):
        """
        Task 2B: Find the most frequent billing code for a given patient ID.
        
        Args:
            patient_id (str): The ID of the patient to analyze.
            data (dict): The JSON data containing patients and claims.
        
        Returns:
            str: The most frequent billing code for the given patient, or None if no claims exist.
        """
        billing_codes = []  # List to store billing codes for the patient
        
        # Find patient by ID and collect their billing codes
        for patient in data["patients"]:
            if patient["id"] == patient_id:
                billing_codes = [claim["billingCode"] for claim in patient["claims"]]
                break  # Exit the loop once the patient is found

        # Return None if no billing codes were found
        if not billing_codes:
            return None
        
        # Find and return the most frequent billing code
        return Counter(billing_codes).most_common(1)[0][0]

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
    patient_id = "P001"  # Specify patient ID
    solution = Solution()
    most_frequent_billing_code = solution.get_most_frequent_billing_code(patient_id, data)
    print("Most Frequent Billing Code:", most_frequent_billing_code)

if __name__ == '__main__':
    main()
