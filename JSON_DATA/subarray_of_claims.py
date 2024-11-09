# Part B:
# Using the same JSON data, write a function to find the length of
# the longest contiguous subarray of claims with the same billing
# code for a given patient ID.

from datetime import datetime

class Solution:
    def longest_same_billing_code_sequence(self, patient_id, data):
        """
        Find the length of the longest contiguous subarray of claims with the same billing code for a given patient ID.

        Args:
            patient_id (str): The ID of the patient to analyze.
            data (dict): The JSON data containing patients and claims.

        Returns:
            int: The length of the longest contiguous sequence of claims with the same billing code.
        """
        max_length = 0  # To store the maximum sequence length
        current_length = 1  # To track the current sequence length

        # Loop through patients to find the target patient
        for patient in data["patients"]:
            if patient["id"] == patient_id:
                # Sort claims by date to ensure they are in order
                claims = sorted(patient["claims"], key=lambda x: x["date"])
                
                # If the patient has no claims, return 0
                if not claims:
                    return 0
                
                # Initialize with the first claim's billing code
                current_code = claims[0]["billingCode"]

                # Iterate over the claims, starting from the second one
                for i in range(1, len(claims)):
                    # If the billing code matches the current code, increment the length
                    if claims[i]["billingCode"] == current_code:
                        current_length += 1
                    else:
                        # Update max length if the current sequence is the longest so far
                        max_length = max(max_length, current_length)
                        # Reset the length counter and update the billing code to the new one
                        current_length = 1
                        current_code = claims[i]["billingCode"]

                # Ensure the last sequence is accounted for
                max_length = max(max_length, current_length)
        
        return max_length  # Return the longest contiguous sequence length

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
    solution = Solution()
    longest_streak = solution.longest_same_billing_code_sequence(patient_id, data)
    print("Longest contiguous billing code streak:", longest_streak)

if __name__ == '__main__':
    main()
