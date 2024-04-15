"""
Emails
Estimate: 15 minutes
Actual:   25 minutes
"""

def extract_name(email):
    # Extracting name from email by splitting at '@' and taking the first part
    name =  email.split('@')[0]
    
    return name.replace(".", " ")

def main():
    users = {}
    
    email = str(input("Email: ")).strip()
    
    while email != "":
    
        name = extract_name(email)
        confirmation = input(f"Is your name {name.title()}? (Y/n) ").strip().lower()
        if confirmation != 'y':
            name = input("Name: ").strip()
        users[email] = name
        email = str(input("Email: ")).strip()
        
        
    for email, name in users.items():
        print(f"{name.title()} ({email})")

main()

