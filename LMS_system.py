users = {}
user_logged = None

def login_required(func):
    def wrapper(*args, **kwargs):
        if user_logged:
            return func(*args, **kwargs)
        else:
            print("Error: You must be logged in to perform this action.")
    return wrapper
def register_new_user():
    username = input("Enter a new username (lowercase): ").lower()
    if username in users:
        print("Error: Username already exists.")
        return
    while True:
       password = input("Enter a password (min 16 chars, 2 special chars, 2 digits): ")
       if valid_password(username, password):
          users[username] = {'password': password, 'courses': {}}
          print(f"User '{username}' registered successfully!")
          break
       else:
           print("Error Password does not meet the requirements.")

def valid_password(username, password):
    count_digits = 0
    count_char = 0
    for char in password:
        if char.isdigit():
            count_digits += 1
        if not char.isalnum():
            count_char += 1
    return len(password) >= 16 and count_char >= 2 and count_digits >= 2 and username not in password

def login():
    global user_logged
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ")
    if username in users and users[username]['password'] == password:
        user_logged = username
        print(f"User '{username}' logged in successfully!")
    else:
        print("Error: Incorrect username or password .")

def logout():
    global user_logged
    if user_logged:
        print(f"User '{user_logged}' logged out.")
        user_logged = None
    else:
        print("No user is logged in.")

@login_required
def add_new_user_course():
    course = input("Enter the course name: ")
    grade= float(input('enter the course mark '))
    if course not in users[user_logged]['courses']:
        users[user_logged]['courses'][course] = grade
        print(f"Course '{course}' added.")
    else:
        print("Course already exists.")

@login_required
def get_student_courses():
    courses = users[user_logged]['courses']
    if courses:
        print("Registered courses:", courses)
    else:
        print("No courses found.")

@login_required
def calculating_the_average():
    courses = users[user_logged]['courses']
    if courses:
        average = sum(courses.values()) / len(courses)
        print(f"Average grade: {average}")
    else:
        print("No courses to calculate.")

@login_required
def remove_my_account():
    global user_logged
    del users[user_logged]
    print(f"User '{user_logged}' deleted.")
    user_logged = None

def get_number_of_users():
    print(f"Total users: {len(users)}")

def run_the_system():
    while True:
        choice = input("Choose: [1] Register, [2] Login, [3] Exit:  ")
        if choice == "1":
            register_new_user()
        elif choice == "2":
            login()
            while user_logged:
                action = input("Actions: [1] Add Course [2] Get Courses [3] Calculate Average [4] Delete Account [5] Logout : ")
                if action == "1":
                    add_new_user_course()
                elif action == "2":
                    get_student_courses()
                elif action == "3":
                    calculating_the_average()
                elif action == "4":
                    remove_my_account()
                elif action == "5":
                    logout()
                else:
                    print("Invalid action.")
        elif choice == "3":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")

run_the_system()