import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sree2643",
    database="entry_pass"
)
if conn.is_connected():
    print("Connected to MySQL")

cursor = conn.cursor()

# conn.close()

import os
max = 5

def clear():
    if os.name == "nt":
        os.system("Cls")
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
    print("Chennai".center(50))
    print()
    print("DATA SCIENCE SEMINAR".center(50))
    print("ENTRY PASS".center(50))
    print("-" * 50)
    print("Pass No :", p[0])
    print("Name    :", p[1])
    print("Place   :", p[2])
    print("Category:", p[3])
    print("-" * 50)
    input("Press any key to continue..")

def visitorEntry():
    cursor.execute("SELECT COUNT(*) FROM entry_pass")
    count = cursor.fetchone()[0]

    if count >= max:
        clear()
        print("HOUSE FULL".center(50))
        input("Press any key to continue...")
        return

    clear()
    print("----- New Visitor Entry -----")
    name = input("Name of Visitor : ")
    place = input("Place           : ")
    cat = input("Category S/E/U  : ").upper()

    if cat == "S":
        category = "Student"
    elif cat == "E":
        category = "Employee"
    elif cat == "U":
        category = "Un-Employee"
    else:
        print("Invalid Category")
        input("Press any key...")
        return

    sql = "INSERT INTO entry_pass (name, place, category) VALUES (%s, %s, %s)"
    values = (name, place, category)
    cursor.execute(sql, values)
    conn.commit()

    cursor.execute("SELECT * FROM entry_pass ORDER BY id DESC LIMIT 1")
    participant = cursor.fetchone()

    EntryPass(participant)

def visitorList():
    clear()
    print("DATA SCIENCE SEMINAR".center(60))
    print("Participant List".center(60))
    print("-" * 60)
    print(
        "Sl.No".ljust(6),
        "Name of Participant".ljust(20),
        "Place".ljust(15),
        "Category".ljust(15)
    )
    print("-" * 60)

    cursor.execute("SELECT * FROM entry_pass")
    rows = cursor.fetchall()

    for row in rows:
        print(
            str(row[0]).ljust(6),
            row[1].ljust(20),
            row[2].ljust(15),
            row[3].ljust(15)
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

    cursor.execute("SELECT COUNT(*) FROM entry_pass")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM entry_pass WHERE category='Student'")
    students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM entry_pass WHERE category='Employee'")
    employees = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM entry_pass WHERE category='Un-Employee'")
    unemp = cursor.fetchone()[0]

    print("No of Participants :", total)
    print("No of Students     :", students)
    print("No of Employees    :", employees)
    print("No of Un-Employee  :", unemp)
    print("-" * 50)
    input("Press any key to continue...")

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
        if conn.is_connected():
            conn.close()
        break
    else:
        print("Invalid Option")
        input("Press any key...")

