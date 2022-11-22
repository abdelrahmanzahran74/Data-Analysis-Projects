# list of Dictionaries (Courses)

Courses = [{"id": 1, "name": "python", "price": 350, "Author_ID": 1},
           {"id": 2, "name": "SQL", "price": 400, "Author_ID": 2},
           {"id": 3, "name": "POWER BI", "price": 250, "Author_ID": 3},
           {"id": 4, "name": "DATABASE", "price": 450, "Author_ID": 2},
           {"id": 5, "name": "XML", "price": 300, "Author_ID": 1}]

# list of Dictionaries (Authors)
Authors = [{"id": 1, "name": "Mohamed Saleh"},
           {"id": 2, "name": "Ahmed Hassan"},
           {"id": 3, "name": "Khaled zaki"}]

# list of Dictionaries (Users)
Users = [{"id": 1, "name": "abdelrhaman"},
         {"id": 2, "name": "mohamed"},
         {"id": 3, "name": "emad"},
         {"id": 4, "name": "mostafa"},
         {"id": 5, "name": "mahmoud"},
         {"id": 6, "name": "ali"},
         {"id": 7, "name": "youseef"}]

# list of Dictionaries (Subscribtion)
subscribtion = [{"user_id": 1, "course_id": [1, 2, 3]},
                {"user_id": 2, "course_id": [1, 4]},
                {"user_id": 3, "course_id": [3, 5]},
                {"user_id": 4, "course_id": [2, 5]},
                {"user_id": 5, "course_id": [1, 2, 5]},
                {"user_id": 6, "course_id": [1, 2, 4]},
                {"user_id": 7, "course_id": [2]}]

names = []
# Function to show


def show(list):
    for key, value in enumerate(list):
        print(value)

# show(Courses)

# def function to add course


def add_course():
    id = Courses[-1]["id"] + 1
    name = str(input("enter name: "))
    price = int(input("enter price: "))
    author_ID = int(input("enter Author_ID: "))
    dictt = {"id": id, "name": name,
             "price": price, "Author_ID": author_ID}
    Courses.append(dictt)
    print("Your Cousre is updated\n")
    show(Courses)

# add_course(Courses)


def remove(list):
    show(list)
    n = int(input("Enter ID of Course/Author you want to remove \n"))
    del(list[n - 1])
    print("your selected Course is deleted\n")
    show(list)

# remove(Courses)

# show authors #done


def add_author():
    id = Authors[-1]["id"] + 1
    name = str(input("enter name: "))
    dictt = {"id": id, "name": name}
    Authors.append(dictt)
    print("Your Author is updated\n")
    show(Authors)

# add_author()
# remove(Authors)


def show_author_crs():
    show(Authors)
    x = int(input("enter author ID: \n"))
    for key, value in enumerate(Courses):
        if (x == Courses[key]["Author_ID"]):
            print(Courses[key]["name"])

# show_author_crs()

# showing user
# show(Users)

# def Function to add new user


def add_user():
    id = Users[-1]["id"] + 1
    name = str(input("enter name: "))
    dictt = {"id": id, "name": name}
    Users.append(dictt)
    print("Your User is updated\n")
    show(Users)

# add_user()

# Function to subscribe


def subscribe():
    show(Users)
    x = int(input("enter user ID: \n"))
    show(Courses)
    y = int(input("Enter Course ID to subscribe: \n"))
    for key, value in enumerate(subscribtion):
        if (x == subscribtion[key]["user_id"]):
            subscribtion[key]['course_id'].append(y)
    print("Your Subscribution is done\n ")
    show(subscribtion)

# subscribe()

# def get_courses to show user's courses


def get_user_crs():
    y = []
    show(Users)
    x = int(input("enter user ID: \n"))
    for key, value in enumerate(subscribtion):
        if (x == subscribtion[key]["user_id"]):
            y = subscribtion[key]["course_id"]
    for i in y:
        for key, value in enumerate(Courses):
            if (i == Courses[key]["id"]):
                print(Courses[key]["name"])

# get_user_crs()


while True:
    a = int(input(
        "For Courses enter 1\nfor Authors enter 2 \nfor Users enter 3\nfor exit program enter 4\n"))
    if a == 1:
        print("For Show Courses enter 1\nfor Add Cousre enter 2\nfor Remove Course enter 3\nfor back to Meun click 4")
        b = int(input("enter number: \n"))
        if b == 1:
            show(Courses)
        elif b == 2:
            add_course()
        elif b == 3:
            remove(Courses)
        elif b == 4:
            continue

    elif a == 2:
        print("For Show Authors enter 1\nfor Add Author enter 2\nfor Remove Author enter 3\nfor show author's courses enter 4\n for back to Meun click 5\n")
        b2 = int(input("enter number: \n"))
        if b2 == 1:
            show(Authors)
        elif b2 == 2:
            add_author()
        elif b2 == 3:
            remove(Authors)
        elif b2 == 4:
            show_author_crs()
        elif b2 == 5:
            continue

    elif a == 3:
        print("For Show User enter 1\nto Add User enter 2\nfor Subscribe enter 3\nto get Courses enter 4\nfor back to Meun click 5\n")
        b3 = int(input("enter number: \n"))
        if b3 == 1:
            show(Users)
        elif b3 == 2:
            add_user()
        elif b3 == 3:
            subscribe()
        elif b3 == 4:
            get_user_crs()
        elif b3 == 5:
            continue
    elif a == 4:
        break
