


passwords = {
    'google': "nathypapa21",
    'github': "password123"
    
}
while True:
    print("1. Add password ")
    print("2. View Password ")
    print("3. Search Password ")
    print("4. Delete Password ")
    print("5. Exit")
    
    choice = input("Enter your choice:")

    if choice == '1':
        website = input("Enter the website:")
        password = input("Enter the password:")
        passwords[website] = password
        print("Password added successfully")
 
    elif choice == '2':
         if not passwords:
             print("No Passwords saved")
         else:
             print("Saved passwords")
             for website, password in enumerate(passwords):
                 print(f"Website: {website} | password: {password}")     
    elif choice == "3":
        website = input("Enter the name of the website to check it's password:")
        if  website in passwords:
            print(f"{website} : {passwords[website]}")
        else:
            print("Website not found")
        
    elif choice == '4':
         website = input('Enter the name of website:') 
         
         if website in passwords:
             del passwords[website]
         else:
            print(f"the is no website called {website}")
             