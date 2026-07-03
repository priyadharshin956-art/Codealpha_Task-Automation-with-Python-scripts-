import re

text = """
abc@gmail.com
support@yahoo.com
test123@gmail.com
"""

emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

print("Email Addresses:")
for email in emails:
    print(email)