# list = []
# limit = 5
# while True:
#     print("""====== MENU ======
#             1. ENTRY PASS
#             2. REPORT
#             3. EXIT""")
#     option = int(input("Enter your option: "))

#     if option==1:
#         if len(list)>=limit:
#             print("participant full for the program")
#             continue

#         name = input("Enter Name: ")
#         place = input("Enter Place: ")
#         category = input("Enter Student / Employee / Unemployed: ")
#         category = category.capitalize()

#         if category not in ["Student", "Employee", "Unemployed"]:
#             print("Invalid category! Please enter correctly.")
#             continue
#         data = {
#             "name": name,
#             "place": place,
#             "category": category
#         }

#         list.append(data)
#         serial_no = len(list)

#         print("""            ----- ENTRY PASS -----
#                   Data Science Program
#                   Organised by Google""")
#         print("                Serial No :", serial_no)
#         print("                Name      :", name)
#         print("                Place     :", place)
#         print("                Category  :", category)

#     elif option == 2:

#         total = len(list)
#         students = 0
#         employees = 0
#         unemployed = 0

#         for p in list:
#             if p["category"] == "Student":
#                 students += 1
#             elif p["category"] == "Employee":
#                 employees += 1
#             elif p["category"] == "Unemployed":
#                 unemployed += 1

#         print("----- REPORT -----")
#         print("Data Science Program")
#         print("Organised by Google\n")
#         print("Total Participants :", total)
#         print("No of Students     :", students)
#         print("No of Employees    :", employees)
#         print("No of Unemployed   :", unemployed)

#     elif option == 3:
#         print("Thank you, Program exited")
#         break

#     else:
#         print("Invalid menu option, Try again")














































import os
max = 1  
num = 0

student_count = 0
employee_count = 0
unemployee_count = 0

participants = []

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def menu():
    clear()
    print("DATA SCIENCE IN TAMIL".center(50))
    print("Chennai".center(50))
    print("-" * 50)
    print("1. Visitor Entry")
    print("2. Visitor List")
    print("3. Summary")
    print("4. Exit")
    print("-" * 50)
def EntryPass(p):
    clear()
    print("DATA SCIENCE IN TAMIL".center(50))
    print("Chennai".center(50),"\n")
    print("DATA SCIENCE SEMINAR".center(50))
    print("ENTRY PASS".center(50))
    print("-" * 50)
    print(("Pass No : " + str(p["num"])).ljust(30))
    print(("Name    : " + p["name"]).ljust(30))
    print(("Place   : " + p["place"]).ljust(30))
    print(("Category: " + p["category"]).ljust(30))
    print("-" * 50)
    input("Press any key to continue...")
def visitorEntry():
    global num, student_count, employee_count, unemployee_count
    if num >= max:
        clear()
        print("HOUSE FULL".center(50))
        input("Press any key to continue...")
        return
    clear()
    print("----- New Visitor Entry -----")
    name = input("Name of Visitor : ")
    place = input("Place           : ")
    category = input("Category S/E/U  : ").upper()
    if category == "S":
        category_name = "Student"
        student_count += 1
    elif category == "E":
        category_name = "Employee"
        employee_count += 1
    elif category == "U":
        category_name = "Un-Employee"
        unemployee_count += 1
    else:
        print("Invalid Category")
        input("Press any key to continue...")
        return
    num += 1
    participant = {
        "num": num,
        "name": name,
        "place": place,
        "category": category_name
    }
    participants.append(participant)
    EntryPass(participant)
def visitorList():
    clear()
    print("DATA SCIENCE SEMINAR".center(60))
    print("Participant List".center(60))
    print("-"*60)
    print(
        "Sl.No".ljust(6),
        "Name of Participant".ljust(20),
        "Place".ljust(15),
        "Category".ljust(15)
    )
    print("-" * 60)
    for i, p in enumerate(participants, start=1):
        print(
            str(i).ljust(6),
            p["name"].ljust(20),
            p["place"].ljust(15),
            p["category"].ljust(15)
        )
    print("-" * 60)
    input("Press any key to continue...")
def summary():
    clear()
    print("DATA SCIENCE IN TAMIL".center(50))
    print("Chennai".center(50))
    print()
    print("DATA SCIENCE SEMINAR".center(50))
    print("Summary".center(50))
    print("-" * 50)
    print(("No of Participants : " + str(num)).ljust(40))
    print(("No of Students     : " + str(student_count)).ljust(40))
    print(("No of Employees    : " + str(employee_count)).ljust(40))
    print(("No of Un-Employee  : " + str(unemployee_count)).ljust(40))
    print("-" * 50)
    input("Press any key to continue-")
while True:
    menu()
    choice = input("Enter your choice : ")
    if choice == "1":
        visitorEntry()
    elif choice == "2":
        visitorList()
    elif choice == "3":
        summary()
    elif choice == "4":
        clear()
        break
    else:
        print("Invalid Option")
        input("Press any key to continue...")
        print("end")
