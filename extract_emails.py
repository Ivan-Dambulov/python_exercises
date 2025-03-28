import re

# Regular expression pattern for valid emails based on the given criteria
email_pattern = r'\b[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*\b'


# Function to extract emails from a string
def extract_emails(text):
    # Find all emails that match the pattern
    emails = re.findall(email_pattern, text)

    # Print each extracted email on a new line
    for email in emails:
        print(email)


# Input: a single string
text = input()

# Extract and print emails
extract_emails(text)
