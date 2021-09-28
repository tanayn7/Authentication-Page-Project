from tkinter import *


count = 0
def register_user():
    global count
    username_info = username.get()
    password_info = password.get()
    
    file = open("Id_Pass.txt", 'a')
    file.write(username_info + "\t | \t")
    file.write(password_info)
    file.write("\n")
    file.close()

    #print("Username : ", username_info)
    #print("Password : ", password_info)

    count= count+1
    if(count ==1):
        Label(screen1, text="Registered Successfully", fg="green").pack()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(text="Registered Done", fg="green").pack()



def register():
    global screen1
    screen1 = Toplevel(screen)

    width=400
    height=400
    screen_width = screen1.winfo_screenwidth()
    screen_height = screen1.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen1.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    screen1.configure(bg="#2d2e30")
    screen1.title("Register")

    Label(screen1, text = "Please Enter Details Below", bg="orange", font=("Arial", 15), height="2", width="200").pack()
    Label(screen1, text = "", bg="#2d2e30").pack()

    global username
    global password
    username = StringVar()
    password = StringVar()

    global username_entry
    global password_entry
    Label(screen1, text = "Username", font=("Arial", 15), fg="white", bg="#2d2e30", width="200", height="2").pack()
    username_entry = Entry(screen1, font=20, textvariable = username)
    username_entry.pack(ipady=9, ipadx=9)
    
    Label(screen1, text = "Password", font=("Arial", 15), fg="white", bg="#2d2e30", width="200", height="2").pack()
    password_entry = Entry(screen1, font=20,  textvariable = password)
    password_entry.pack(ipady=9, ipadx=9)
    
    Label(screen1, text = "", bg="#2d2e30").pack()
    Button(screen1, text="Register", width="15", height="1", bg="#008502", font=5, command= register_user).pack()

    exitbutton = Button(screen1, text="Exit", bg="#ff0000", width="15", height="1", font=5, command=screen1.destroy)
    exitbutton.pack()




def delete1():
    screen3.destroy()
    screen2.destroy()
    global screen6
    screen6 = Toplevel(screen)

    width=500
    height=500
    screen_width = screen6.winfo_screenwidth()
    screen_height = screen6.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen6.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    screen6.title("Weather App")

    Label(screen6, text="Welcome to Weather App", font=("calibri", 20)).pack()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    
    width=120
    height=60
    screen_width = screen3.winfo_screenwidth()
    screen_height = screen3.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen3.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    Label(screen3, text="Login Success", bg="black", fg="white").pack()
    Button(screen3, text="OK", bg="gold3", command=delete1).pack()



def delete2():
    screen4.destroy()


def password_not_found():
    global screen4
    screen4 = Toplevel(screen) 

    width=120
    height=60
    screen_width = screen4.winfo_screenwidth()
    screen_height = screen4.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen4.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    
    Label(screen4, text="Incorrect Password ", bg="black", fg="white").pack()
    Button(screen4, text="OK", bg="#d60909", height=1, command=delete2).pack()



def delete3():
    screen5.destroy()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    
    width=120
    height=60
    screen_width = screen5.winfo_screenwidth()
    screen_height = screen5.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen5.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    screen5.title("Not Found")
    Label(screen5, text="Not Found", bg="black", fg="white").pack()
    Button(screen5, text="OK", bg="#d60909", command=delete3).pack()




def login_user():
    username_login_info = username_login.get()
    password_login_info = password_login.get()
    
    login_info = StringVar()
    file_info = StringVar()
    counter = 0
    file = open("Id_Pass.txt", 'r')
    for line in file:
        file_info = line.rstrip("\n")
        list_of_file_info = file_info.split("\t")
        #print(list_of_file_info)
        if (username_login_info == list_of_file_info[0]):
            if (password_login_info == list_of_file_info[2]):
                counter= counter + 1
                login_success()

            if (password_login_info != list_of_file_info[2]):
                counter= counter + 1
                password_not_found()
    
    
    if(counter == 0):    
        user_not_found()




def login():
    global screen2
    screen2 = Toplevel(screen)

    width=400
    height=400
    screen_width = screen2.winfo_screenwidth()
    screen_height = screen2.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen2.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
    screen2.configure(bg="#2d2e30")
    screen2.title("Login")

    Label(screen2, text = "Please Enter Details Below", bg="orange", font=("Arial", 15), height="2", width="200").pack()
    Label(screen2, text = "", bg="#2d2e30").pack()
    
    global username_login
    global password_login
    username_login = StringVar()
    password_login = StringVar()    

    Label(screen2, text = "Username", font=("Arial", 15), fg="white", bg="#2d2e30", width="200", height="2").pack()
    username_entry_login = Entry(screen2, font=20, textvariable = username_login)
    username_entry_login.pack(ipady=9, ipadx=9)

    Label(screen2, text = "Password", font=("Arial", 15), fg="white", bg="#2d2e30", width="200", height="2").pack()
    password_entry_login = Entry(screen2, font=20, textvariable = password_login)
    password_entry_login.pack(ipady=9, ipadx=9)

    Label(screen2, text = "", bg="#2d2e30").pack()
    Button(screen2, text="Login", width="15", height="1", bg="#008502", font=5, command= login_user).pack()

    exitbutton = Button(screen2, text="Exit", bg="#ff0000", width="15", height="1", font=5, command=screen2.destroy)
    exitbutton.pack()



#Main Function
def main_screen():
    global screen
    screen = Tk()

    width=400
    height=400
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
    x = (screen_width/2) -(width/2)
    y = (screen_height/2) - (height/2)
    screen.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    screen.title("SignIn and SignUp")
    screen.configure(bg="#2a5ad4")

    L1 = Label( text = "Registration Window", width="300", height="4", fg="white", bg = "#575ab5", font = ("Calibri", 15))
    L1.pack()
    Label( text = "", bg="#2a5ad4").pack()
    Label( text = "", bg="#2a5ad4").pack()
    Button( text = "Login", width="13", font=("Arial",30), height="1", fg="White", bg="black", command=login).pack()
    Label( text = "", bg="#2a5ad4").pack()
    Label( text = "", bg="#2a5ad4").pack()
    Button( text = "Register", width="13", font=("Arial",30) , height="1",fg="white", bg="black", command=register).pack()  #font=("Calibri",13) 
    screen.mainloop()


main_screen()

