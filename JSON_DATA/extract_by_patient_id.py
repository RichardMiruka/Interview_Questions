# Write a function to extract all claims related to a given patient ID from the provided JSON data.
# Return a list of related claim IDs.

class Solution:
    def extract_claims_by_patient(self, data, patient_id):
        """
        Extract all claims related to a given patient ID from the provided JSON data.

        Args:
            data (dict): JSON data containing patients and their claims.
            patient_id (str): The ID of the patient to find claims for.

        Returns:
            list[str]: A list of claim IDs associated with the given patient ID.
            Returns an empty list if no claims are found for the patient.
        """
        for patient in data['patients']:
            if patient['id'] == patient_id:  # Check if the patient ID matches the given patient ID
                return [claim['id'] for claim in patient['claims']]  # Return all claim IDs for this patient

        return []  # Return an empty list if no matching patient ID is found

# Test the solution with the sample data
def main():
    data = {
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
    patient_id = "P001"
    solution = Solution()
    related_claims = solution.extract_claims_by_patient(data, patient_id)
    print(related_claims)  # Expected output: ['C001', 'C002', 'C003']

if __name__ == "__main__":
    main()
