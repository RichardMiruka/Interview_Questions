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

# Task 1: Extract Related Claims
# Part A:
# Write a function to extract all claims related to a given claim
# ID from the provided JSON data. Return a list of related claim
# IDs. A related claim is one that has the same billing code as the given claim.

class Solution:
    def extract_related_claims(self, data, claim_id):
        """
        Extract all claims related to a given claim ID from the provided JSON data.
        
        Args:
            data(dict): JSON data containing patients and their claims.
            claim_id(str): The ID of the claim to find related claims for.
        
        Returns:
            list[str]: A list of related claim IDs with the same billing code,
            including the original claim ID.
            Returns an empty list if no related claims are found.
        """
        billing_code = None                                        # Initialize the billing code to None
        related_claims = []                                        # Initialize an empty list to store related claim IDs

        # Find the billing code for the given claim ID
        for patient in data['patients']:                           # Loop through each patient
            for claim in patient['claims']:                        # Loop through each claim of the patient
                if claim['id'] == claim_id:                        # Check if the claim ID matches the given claim ID
                    billing_code = claim['billingCode']            # Get the billing code for the claim
                    break                                          # break the inner loop if billing code is found
            if billing_code:                                       # Check if billing code is found
                break                                              # break the outer loop if billing code is found

        # If found, get all claims with the same billing code
        if billing_code:                                           # Check if billing code is found for the given claim ID
            for patient in data['patients']:                       # Loop through each patient
                for claim in patient['claims']:                    # Loop through each claim of the patient
                    if claim['billingCode'] == billing_code:       # Check if the billing code matches the billing code of the given claim
                        related_claims.append(claim['id'])         # Add the claim ID to the list of related claims

        return list(set(related_claims))                           # Return a list of unique related claim IDs

def main():                                                        # Main function to test the solution
    data = {                                                       # Sample JSON data
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
    claim_id = "C002"                                                       # Claim ID to find related claims for
    solution = Solution()                                                   # Create an instance of the Solution class
    related_claims = solution.extract_related_claims(data, claim_id)        # Call the extract_related_claims function
    print(related_claims)                                                   # Expected output: ['C001', 'C002']

if __name__ == "__main__":                                                  # Check if the script is run directly
    main()                                                                  # Call the main function
