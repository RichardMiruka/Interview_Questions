# You are tasked with analyzing health insurance claims data
# represented in a JSON format. The data includes information
# about patients and their associated claims. You need to perform
# several tasks to extract insights and analyze patterns in the
# claims data.
# {
#        "patients": [
#            {
#                "id": "P001",
#                "claims": [
#                    {"id": "C001", "amount": 100, "billingCode": "B001", "date": "2024-01-01"},
#                    {"id": "C002", "amount": 200, "billingCode": "B001", "date": "2024-01-05"},
#                    {"id": "C003", "amount": 150, "billingCode": "B002", "date": "2024-01-10"}
#                ]
#            }
#        ]
#    }

# Task 1: 
# Part B: Part B:
# Using the same JSON data, write a function to find the maximum
# claim amount in the last 'n' days for a given patient ID.


# The question is asking you to create a function that identifies the maximum claim amount made
# by a specific patient within a specified number of days leading up to the current date.
# Key Components of the Task:
# Input Requirements:
#  Patient ID: You need to identify which patient's claims you will be examining.
# JSON Data: The data structure that contains information about multiple patients
# and their respective claims.
# Number of Days (n): This indicates how many days back from the current date
# you should consider for finding claims.

from datetime import datetime

class Solution:
    def get_max_claim_amount_in_days(self, data, patient_id, n_days):
        """
        Find the maximum claim amount made by a specific patient within a specified 
        number of days leading up to the current date.
        
        Args:
            data (dict): JSON data containing patients and their claims.
            patient_id (str): The ID of the patient whose claims you want to analyze.
            n_days (int): The number of days back from the current date to consider.
        
        Returns:
            int: The maximum claim amount made by the patient within the last 'n_days'.
            Returns 0 if no claims are found for the patient within the specified timeframe.
        """

        max_amount = 0  # Initialize the maximum claim amount to 0
        today = datetime.now()  # Get the current date

        # Iterate through patients to find the patient with the given ID
        for patient in data["patients"]:
            if patient["id"] == patient_id:
                # Iterate through each claim for the matching patient
                for claim in patient["claims"]:
                    claim_date = datetime.strptime(claim["date"], "%Y-%m-%d")  # Convert claim date to datetime object
                    if (today - claim_date).days <= n_days:  # Check if claim date is within the last n_days
                        max_amount = max(max_amount, claim["amount"])  # Update the maximum claim amount if necessary
        return max_amount  # Return the maximum claim amount within the last n_days

def main():
    data = {  # Sample JSON data
        "patients": [
            {
                "id": "P001",
                "claims": [
                    {"id": "C001", "amount": 100, "billingCode": "B001", "date": "2024-01-01"},
                    {"id": "C002", "amount": 200, "billingCode": "B001", "date": "2024-01-05"},
                    {"id": "C003", "amount": 150, "billingCode": "B002", "date": "2024-01-10"}
                ]
            }
        ]
    }
    patient_id = "P001"  # Patient ID to find claims for
    n_days = 365  # Number of days to consider
    solution = Solution()  # Create an instance of the Solution class
    max_amount = solution.get_max_claim_amount_in_days(data, patient_id, n_days)  # Call the function
    print(max_amount)  # Expected output: 200

if __name__ == "__main__":
    main()
