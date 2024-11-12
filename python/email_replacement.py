emails = [
    "john@zap.com",
    "jane@zap.com",
    "mike@ezap.org",
    "sara@ezap.org",
    "anna@ezap.org"
]

updated_emails = [email.replace("@zap.com", "@ezap.org") if "@zap.com" in email else email for email in emails]

print("Updated email list:")
for email in updated_emails:
    print(email)
