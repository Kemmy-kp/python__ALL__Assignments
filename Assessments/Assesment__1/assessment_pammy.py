import datetime



def main_menu():
    menu="""
            Welcome To Python E-Notebook

                press 1 for Generate Note
                press 2 for View Note
                press 3 for Exit
        """
    return menu

def generate_note():
    name=input("Enter Python E-Note Generator Name : ")
    title=input("Enter Python E-Note Title : ")
    content=input("Enter E-Note Content : ")

    f=open("Python_E-note.txt",'a')
    f.write("================================\n")
    now = datetime.datetime.now()
    f.write(f"{now}\n")
    f.write(f"E-Note Title : {title}\n")
    f.write(f"E-Note Description : {content}\n")
    f.write(f"               E-Note Generator : {name}\n")
    
    f.close()


def view_notes():
    
        f = open("python_E-note.txt", "r")
        print(f.read())
    


status=True
while status:
    print(main_menu())
    choice=input("Enter Your Choice : ")

    if choice=='1':
        generate_note()
        status=False

    elif choice=='2':
        view_notes()
        pass
    elif choice=='3':
        print("Thank You")
        break
    else:
        status=True
        print("Please Enter Valid Choice !!! ") 
