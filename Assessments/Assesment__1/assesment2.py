import datetime

status = True

def main():
    while True:
        a = input("Enter python E-note generator name: ")

        if a.isdigit():
            print("Invalid input.")
            continue
        b = input("Enter python E-note Title: ")
        if b.isdigit():
            print("Invalid input.")
            continue
        c = input("Enter python E-note content: ")
        if c.isdigit():
            print("Invalid input.")
            continue
        return a, b, c

log_file = open("log.txt", "a") 

while status:
    print("\nWelcome to python e-note book")
    print("Press 1 for Generate Note")
    print("Press 2 for View Note")
    print("Press 4 for Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        generator_name, note_title, note_content = main()
        if not generator_name or not note_title or not note_content:
            print("Invalid input. Please provide all details.")
            continue

        now = datetime.datetime.now()
        timestamp = now.strftime("%y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Generated Note by {generator_name}: Title - {note_title}, Content - {note_content}\n"
        log_file.write(log_entry)
        print("Note generated successfully!")

    elif choice == '2':
        pass
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    confirmation = input("Press Enter to continue...")
    print("\n" + confirmation)

log_file.close() 
