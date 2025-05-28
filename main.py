import csv
from datetime import datetime

def csv_file_reader(filename):
    global read
    reader_list = []
    with open(f"{filename}.csv","r") as fh: 
        read = csv.reader(fh)
        for row in read :
            reader_list.append(row)
    return reader_list
def csv_file_writer(filename,list):
    
    with open(f"{filename}.csv","a") as fh:
        c_obj = csv.writer(fh)
        c_obj.writerow(list)
def csv_file_checker(filename):
    try:
        with open(f"{filename}.csv","r") as fh: 
            pass
    except:
        with open(f"{filename}.csv","w") as fh:
            pass
def user_login():
    global read
    global state
    global user
    while True:
        username = input("Enter username :- ")
        password = input("Enter password :- ")
        csv_file_reader("user_details")
        
        reader_list = csv_file_reader("user_details")
        for row in reader_list:
            if row:
                if username == row[0] and password == row[1]:
                    print("-------------------------------")
                    print("    succesfully logged in !    ")
                    print("-------------------------------")
                    user = username
                    state = "menu"
                    return
        if [username,password] not in reader_list:
            print("-----------------------------")
            print("      No account found!      ")
            print(" Check username or password! ")
            print("-----------------------------")
            ans = input("Want to one more try? (yes/no) :- ")
            if ans.capitalize() == "Yes":
                continue
            if ans.capitalize() == "No":
                user_register()
                break
            
def user_register():
    global c_obj
    global state
    global user
    while True:
        
        username = input("Enter username to register :- ")
    
        password = input("Enter password to register :- ")
        if username.isspace() or password.isspace():
            print("-----------------------------")
            print("  Don't just type a blank !  ")
            print("-----------------------------")
            continue
        reader_list = csv_file_reader("user_details")
        
        
        names = [name[0] for name in reader_list if name != []]
        
        if username in names :
            print("---------------------------------------")
            print("  username not available , try again!  ")
            print("---------------------------------------")
            continue
            
        else:
            print("--------------------------------")
            print("    succesfully registered !    ")
            print("--------------------------------")
            csv_file_writer("user_details",[username,password])
            state = "menu"
            user = username
            return
def creating_blog():
    
    
    reader_list = csv_file_reader("users_blogs")
    check_users = {row[0] for row in reader_list if row}
    
    if  user not in  check_users :   
        print("-------------------------------------")
        print("  Amanzing! Create your first Blog!  ")
        print("-------------------------------------")
    while True: 
        title = input("Enter the title (limit : 40 letters) :- ")
        if len(title) > 40 :
            print("-----------------------------")
            print("    Be in your limits! :)    ")
            print("-----------------------------")
            continue
        blog = input("Write a  Blog (limit : 150 words) :- ")
        status = "private"
        if len(blog.split()) > 150 :
            print("-----------------------------")
            print("    Be in your limits! :)    ")
            print("-----------------------------")
            continue
        
        date = datetime.now().strftime("%d-%m-%Y")
        csv_file_writer("users_blogs",[user,title,blog,status,date])
        ans = input("Want to write more (yes/no) :- ")
        if ans.capitalize() == "Yes":
            continue
        if ans.capitalize() == "No":
            break
            
        
    
def editing_blog():
    global editing_index
    global action
    global state
    editing_action = None
    action = None
    
    
    while True:
        print("you're options are :-")
        print("1> Title")
        print("2> blog")
        print("3> Go back to menu")
        try : 
            editing_action = int(input("Choose a number to select :- "))
        except:
            print("------------------------------")
            print("   Enter a valid selection!   ")
            print("------------------------------")
            continue
        if editing_action == 1 :
            editing_blog_options("title")
            
            ans = input("Want to edit more (yes/no) :- ")
        
            if ans.capitalize() == "Yes":
                continue
            if ans.capitalize() == "No":
                break 
                 
        elif editing_action == 2 :
            editing_blog_options("blog")
            ans = input("Want to edit more (yes/no) :- ")
        
            if ans.capitalize() == "Yes":
                continue
            if ans.capitalize() == "No":
                break 
        elif editing_action == 3:
            state = "menu"
            break
        else:
            print("------------------------------")
            print(" Enter the number in options! ")
            print("------------------------------")
            continue
            
        
                    
                
        
    
def editing_blog_options(option):
    global state
    reader_list = csv_file_reader("users_blogs")
    check_users = {row[0] for row in reader_list if row}
    editing_options = []
    text = ""
    
    while True:
        
        if user in check_users:
            check_users = [row[0] for row in reader_list if row]
            count = 1 
            if option == "title":
                print(f"Here are all your {option}s :- ")
            else:
                print(f"Here are all your blogs :- ")
            if option == "showing":
                print("--------------------------------------------------")
                print(f"| Username | Title | Blog | Status | Created On |")
                print("--------------------------------------------------")
            for index,row in enumerate(reader_list):
                if row and row[0] == user:
                    
                    if option in ["title","deleting"]:
                        print(f"{count}> {row[1]}")
                    elif option == "blog":
                        print(f"{count}> {row[2]}")
                    elif option == "publishing":
                        print(f"{count}> {row[1]},{row[3]}")
                    elif option == "showing":
                        print(f"{count}> {row}")
                    if row[0] == user:
                        editing_options.append([row,index])
                    editing_action = None
                    count+= 1
        elif user not in check_users :
            while True:
                print("----------------------------")
                print("     You have no blogs!     ")
                print("----------------------------")
                if option in ["title","blog","publishing","showing"]:
                    print("1> Create blogs")
                    print("2> Go back to menu")
                    try:
                        action = int(input("Choose a number to select :- "))
                    except:
                        print("------------------------------")
                        print("   Enter a valid selection!   ")
                        print("------------------------------")
                    if action == 1 :
                        creating_blog()
                        
                        break
                        
                                                
                    elif action == 2:
                        state = "menu"
                        return
                    else:         
                        print("------------------------------")
                        print(" Enter the number in options! ")
                        print("------------------------------")
                        continue
                elif option == "deleting":
                    try:
                        editing_action = input("Wanna go back to menu! (Yes/No):- ")
                    except:
                        print("-----------------------------")
                        print("    Error occured, Retry!    ")
                        print("-----------------------------")
                        continue
                
                    if editing_action.capitalize() == "Yes":
                        state ="menu"
                        return
                    elif editing_action.capitalize() == "No":
                        continue
                    else:
                        print("------------------------------")
                        print("    Please, type (yes/no)!    ")
                        print("------------------------------")
        if option != "showing":
            try :
                
                editing_action = int(input("Choose a number to select :- "))
                
                    
            except:
                print("------------------------------")
                print("   Enter a valid selection!   ")
                print("------------------------------")
                continue
            
            try :
                if option == "title":   
                    text = input("Write the title (limit : 35) :- ")
                    if len(text) > 35 :
                        print("-----------------------------")
                        print("    Be in your limits! :)    ")
                        print("-----------------------------")
                        continue
                elif option == "blog":
                    text = input("Write the blog (limit : 150 words) :- ")
                    if len(text.split()) > 150 :
                        print("-----------------------------")
                        print("    Be in your limits! :)    ")
                        print("-----------------------------")
                        continue
                elif option == "publishing":
                    text = input("Select the status (private,public) :- ")
                    if text.capitalize() not in ["Private","Public"]:
                        print("------------------------------")
                        print("   Enter a valid selection!   ")
                        print("------------------------------")
                        continue
                elif option == "deleting":
                    try : 
                        ans = input("Are you Sure! (yes/no) :- ")
                    except:
                        print("------------------------------")
                        print("   Enter a valid selection!   ")
                        print("------------------------------")
                        continue
                    if ans.capitalize() == "Yes":
                        pass
                    elif ans.capitalize() == "No":
                        print("------------------------------")
                        print("     Redirected to menu !     ")
                        print("------------------------------")
                        state = "menu"
                        return
                    else:
                        print("------------------------------")
                        print("    Please, type (yes/no)!    ")
                        print("------------------------------")
                        continue
            except:
                print("-----------------------------")
                print("    Error occured, Retry!    ")
                print("-----------------------------")
                continue
            with open ("users_blogs.csv","w") as fh :
                w_obj = csv.writer(fh)
                w_obj.writerow(["username","title","blog","status","published_on"])
            with open  ("users_blogs.csv","a") as fh :
                w_obj = csv.writer(fh)
                for index,row in enumerate(reader_list):
                            
                    if row != ["username","title","blog","status","published_on"]:
                        if row:
                            if option in ["title","blog","publishing"] :
                                if index == editing_options[editing_action-1][1]:
                                    if option == "title":
                                        row[1] = text
                                    elif option == "blog":
                                        row[2] = text
                                    elif option == "publishing":
                                        row[3] = text
                                        if text == "private":
                                            print("------------------------------")
                                            print("    Succesfullly Privated!    ")
                                            print("------------------------------")
                                        elif text == "public":
                                            print("-------------------------------")
                                            print("    Succesfullly Published!    ")
                                            print("-------------------------------")
                                        
                                w_obj.writerow(row)
                            else:
                                if index == editing_options[editing_action-1][1]:
                                    pass
                                else:
                                    w_obj.writerow(row)
                return
        else:
            print("------------------------------")
            print("     Redirected to menu !     ")
            print("------------------------------")
            state = "menu"
            return
    
def Deleting_blog():
    editing_blog_options("deleting")        
def publishing_blog():
    editing_blog_options("publishing")
def showing_blogs():
    editing_blog_options("showing")
csv_file_checker("users_blogs")
csv_file_checker("user_details")
state = "login"
action = None
user = None
while True:
    
    if state == "login":
        print("----------------------------------------")
        print("   welcome to blog management system!   ")
        print("----------------------------------------")
        print("you're options are :-")
        print("1> Login")
        print("2> Register")
        try:
            action = int(input("Choose a number to select :- "))
        except:
            print("------------------------------")
            print("   Enter a valid selection!   ")
            print("------------------------------")
            continue
        if action == 1:
            user_login()
            action = None
        elif action == 2:
            user_register()
            action = None
        else:
            print("------------------------------")
            print(" Enter the number in options! ")
            print("------------------------------")
            continue
    if state == "menu":
        print("you're options are :-")
        print("1> Create Blog")
        print("2> Edit Blog")
        print("3> Delete Blog")
        print("4> Status of Blog")
        print("5> Show all Blogs")
        print("6> Exit")
        try:
            action = int(input("Choose a number to select :- "))
        except:
            print("------------------------------")
            print("   Enter a valid selection!   ")
            print("------------------------------")
        if action == 1:
            creating_blog()
            action = None
        elif action == 2:
            editing_blog()
            action = None
        elif action == 3:
            Deleting_blog()
            action = None
        elif action == 4:
            publishing_blog()
            action = None
        elif action == 5:
            showing_blogs()
        elif action == 6:
            print("-----------------------------------------------")
            print("  Thanks for using our blog management system  ")
            print("-----------------------------------------------")
            break
            
        else:
            print("------------------------------")
            print(" Enter the number in options! ")
            print("------------------------------")
            continue
                