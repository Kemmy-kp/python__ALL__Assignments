
status=True
def main():

    a=input("enter python E-note generator name:")
    b=input("enter python E-note Title:")
    c=input("enter python E-note content")
    
while status:
    print("\nwelcome to python e-note book")
    print("press 1 for Generate Note")
    print("press 2 for View Note")
    print("press 4 for Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        main()
    elif choice == '2':
        main()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
