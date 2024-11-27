import re
def extract_email(text):
    email_pattern=r'[a-zA-z0-9%+-]+@[a-zA-z0-9%+-]+\.[a-zA-z]{2,}'
    return re.findall(email_pattern,text)
sample_text="please contact us at support @example.com or sales@example.org."
emails=extract_email(sample_text)
print("extracted emails:",emails)
