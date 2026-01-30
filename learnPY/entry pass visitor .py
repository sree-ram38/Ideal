participants = [] 
limit = 5              
while True:
    print("\n====== MENU ======")
    print("1. ENTRY PASS")
    print("2. REPORT")
    print("3. EXIT")
    option = int(input("Enter your option: "))
    if option == 1:
        if len(participants) >= limit:
            print("Participant limit reached. HOUSE FULL!")
            continue
        name = input("Enter Name: ")
        place = input("Enter Place: ")
        category = input("Enter category (Student / Employee / Unemployed): ")
        category = category.capitalize()
        if category != "Student" and category != "Employee" and category != "Unemployed":
            print("Invalid category! Try again.")
            continue
        participant = {
            "name": name,
            "place": place,
            "category": category
        }
        participants.append(participant)
        num = len(participants)
        print("\n----- ENTRY PASS -----")
        print("Data Science Program")
        print("Organised by Google")
        print("Serial No :",num)
        print("Name      :",name)
        print("Place     :",place)
        print("Category  :",category)
    elif option == 2:
        total = len(participants)
        students = 0
        employees = 0
        unemployed = 0
        for p in participants:
            if p["category"] == "Student":
                students = students + 1
            elif p["category"] == "Employee":
                employees = employees + 1
            else:
                unemployed = unemployed + 1
        print("\n----- REPORT -----")
        print("Data Science Program")
        print("Organised by Google")
        print("Total Participants :",total)
        print("No of Students     :",students)
        print("No of Employees    :",employees)
        print("No of Unemployed   :",unemployed)
    elif option == 3:
        print("Thank you! Program exited.")
        break
    else:
        print("Invalid option! Please try again.")
