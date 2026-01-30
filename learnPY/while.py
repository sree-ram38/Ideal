# i = 11
# while i>=10:
#     print(i)
#     i = i+1
#     break

# i = 6
# while i>=1:
#     print('*' * i)
#     i = i - 1

# i = 1
# while i<=5:
#     print('*' * i)
#     i = i + 1

# secret = 10
# limit = 0
# while limit < 3:
#      find = int(input("Guess : "))
#      limit += 1
#      if find == secret:
#         print("You won")
#         break
# else:
#     print("Sorry, Try again")



# command = ""
# while command != "quit":
#     command = input("Type : ").lower()
#     if command == "start":
#         print("Car started")
#     elif command == "stop":
#         print("Car stopped")
#     elif command == "help":
#         print("""
#         start - start the car
#         stop - stop the car
#         quit - to quit
#          """)
#     elif command == "quit":
#         break
# else:
#     print("I can't understand what you are saying")

command = ""
started = False
while True:
    command = input("Type : ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
        print("Car started")
    elif command == "stop":
        if not started:
            print("Car stopped already")
        else:
            started = False
        print("Car stopped")
    elif command == "help":
        print("""
        start - start the car
        stop - stop the car
        quit - to quit
         """)
    elif command == "quit":
        break
else:
    print("I can't understand what you are saying")