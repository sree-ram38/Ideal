import os
max = 2 
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