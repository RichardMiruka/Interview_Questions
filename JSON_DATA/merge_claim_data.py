# Part A:
# Write a function to merge claims for a specific patient and
# with the same billing code. Return the merged claim data as a JSON object.

class Solution:
    def merge_claims(self, data, patient_id, billing_code):
        """
        Merge claims for a specific patient and with the same billing code.

        Args:
            data (dict): JSON data containing patients and their claims.
            patient_id (str): The ID of the patient whose claims you want to merge.
            billing_code (str): The billing code to filter claims for merging.

        Returns:
            dict: A JSON object representing the merged claims data.
        """
        # Initialize an empty dictionary to store the merged claims
        merged_claim = {
            "patientId": patient_id,
            "billingCode": billing_code,
            "totalAmount": 0,
            "claimCount": 0,
            "claims": []
        }

        # Find the patient with the given ID
        for patient in data["patients"]:
            if patient["id"] == patient_id:
                # Find claims with the same billing code and add them to the merged claim data
                for claim in patient["claims"]:
                    if claim["billingCode"] == billing_code:
                        merged_claim["totalAmount"] += claim["amount"]  # Add the claim amount to the total amount
                        merged_claim["claimCount"] += 1                 # Increment the claim count
                        merged_claim["claims"].append(claim)            # Add the claim to the merged claim data

        # Return the merged claim data as a JSON object
        return merged_claim

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
    patient_id = "P001"                 # Patient ID to find claims for
    billing_code = "B001"               # Billing code to filter claims for merging
    solution = Solution()               # Create an instance of the Solution class
    merged_data = solution.merge_claims(data, patient_id, billing_code)  # Call the function
    print(merged_data)                  # Expected output: merged claim data

if __name__ == "__main__":             # Check if the script is being run directly
    main()                             # Call the main function
