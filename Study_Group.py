users=[]
usernames=set()
groups={}

#about user registration
def register_user():
    name=input("Enter your username: ")
    if name.lower() in usernames:
        print("user already exists , try another username")
        return
    batch_year=input("Enter your batch year: ")
    learn_skills=input("Enter the skills you want to learn: ").lower().split(",")
    teach_skills=input("Enter the skills you can teach: ").lower().split(",")
    user={
        "name":name,
        "batch_year":batch_year,
        "learn_skills":[skill.strip() for skill in learn_skills],
        "teach_skills":[skill.strip() for skill in teach_skills],
        "groups":[],
        "rating":[]
    }
    users.append(user)
    usernames.add(name.lower())
    print(f"User'{name}' registered successfully!\n")

#about creating groups
def create_group(user,group_name):
    skill=group_name.strip().lower()
    if skill not in groups:
        groups[skill]=[]
        if user['name'] not in groups[skill]:
            groups[skill].append(user["name"])
            user["groups"].append(skill)
            print(f"Group '{skill}' is created by {user['name']}\n")
        else:
            print(f"{user['name']} already a member of this group\n")

#about viewing groups 
def view_group():
    if not groups:
        print("No groups available")
    else:
        print("Existing groups: ")
        for group_name in groups:
            print(f"-> {group_name}")

#about joining group
def join_group(user):
    if not groups:
        print("No groups available to join\n")
        return
    print("Available groups: ")
    for group_name in groups:
        print(f"-{group_name}")
    selected_group= input("Enter the group name you want to join: ").strip().lower()
    if selected_group in groups:
        if user["name"] not in groups[selected_group]:
            groups[selected_group].append(user["name"])
            user["groups"].append(selected_group)
            print(f"{user['name']} joined group '{selected_group}' \n")
        else:
            print(f"{user['name']} is already a member of '{selected_group}' \n")
    else:
        print("Group not found\n")

#about viewing member profile
def view_profile():
    if not users:
        print("no members registred yet\n")
        return
    for user in users:
        print(f"Name: {user['name']}")
        print(f"Batch: {user['batch_year']}")
        print(f"skills to learn: {','.join(user['learn_skills'])}")
        print(f"skills to teach: {','.join(user['teach_skills'])}")
        print(f"Groups: {','.join(user['groups'])}")
        print(f"Rating: {user['rating']}")
        print("\n")
#rating
def add_rating(user_name,Rating):
    for user in users:
        if user["name"].lower()==user_name.lower():
            user["rating"].append({"Rating":Rating})
            print(f"Rating added for {user_name}\n")
            return
    print(f"user not found\n")

#to iterate over user list
def user_list(name):
    for user in users:
        if user["name"].lower() == name.lower():
            return user
    return None
    
#main
def main():
    while True:
        print("\n---WELCOME TO STUDY GROUP---")
        print("\n1. Register users")
        print("\n2. Create group")
        print("\n3. View groups")
        print("\n4. Join group")
        print("\n5. View member profiles")
        print("\n6. Add rating")
        print("\n7. Exit")
        choice = input("choose an option: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            name=input("Enter your name: ")
            user= user_list(name)
            if user:
                group_name = input("Enter the name of the group you want to create: ")
                create_group(user, group_name)
            else:
                print("User not found\n")

        elif choice =="3":
            view_group()
        
        elif choice=="4":
            name=input("Enter your name: ")
            user= user_list(name)
            if user:
                join_group(user)
            else:
                print("User not found\n")

        elif choice=="5":
            view_profile()

        elif choice=="6":
            name=input("Enter the user's name to Rate: ")
            Rating=int(input("Enter Rating (1-10): "))
            if Rating>=1 and Rating<=10:
                add_rating(name,Rating)
            else:
                print("Invalid rating, rate between (1-10)")
        
        elif choice=="7":
            print("Have a good day!")
            break
        else:
            print("Invalid option, Try again")

main()
