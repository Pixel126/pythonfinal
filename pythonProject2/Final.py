# Import modules
import csv
import course_dictionary as cd


# Main function
def main():
    # Intro to the user
    print("Hello user, you are using Course Chatbot.")
    print("This chat bot will help you figure out which courses you still need to take for a Bellevue College Bachelor of Applied Science (BAS) degree in Business Management & Technology (BMT) for a specified quarter")

    # Asks if the user needs help
    proceed = cd.newinput("Would you like help with course recommendations:")
    proceedcheck(proceed)
    user_info()


# Function to gather user information
def user_info():
    # Read and assign variables from CSV files
    comp_courses = read_csv("completed_courses.csv")
    core_courses = read_csv("core_courses.csv")
    need_courses = read_csv("core_courses.csv")

    # Remove completed courses from needed courses
    for tempcourse in comp_courses:
        for course in core_courses:
            if tempcourse in course:
                need_courses.remove(course)

    # Gather user information
    print("")
    print("=" * 60)
    userName = cd.newinput("Enter your full name:")
    nameVerify(userName)

    userEmail = cd.newinput("Enter email:")
    emailVerify(userEmail)

    userID = cd.newinput("Enter student ID:")
    idVerify(userID)
    print("=" * 60)

    # Display greeting and recommendations
    greeting(comp_courses, core_courses, userName)
    print("")
    quarter = seasoninput(need_courses)
    rec_course(userName, userEmail, userID, quarter, need_courses)
    print("")


# Function to input the quarter
def seasoninput(need_courses):
    season = ["fall", "winter", "spring", "summer"]
    while True:
        quarter = cd.newinput("Which quarter are you planning for:").lower()
        if quarter in season:
            return quarter
        else:
            print("Invalid season, try again")


# Function to check if the user wants to proceed
def proceedcheck(proceed):
    options = ["yes", "no"]
    if proceed not in options:
        print("Invalid input, try again")
        main()
    elif proceed == "no":
        exit()
    else:
        pass


# Function to continue recommendations for the next quarter
def continue_rec(userName, userEmail, userID, quarter, need_courses):
    print("=" * 60)
    userInput = cd.newinput("Would you like to see recommendations for the next quarter:").lower()
    options = ["yes", "no"]
    season_options = ["spring", "summer", "fall", "winter"]
    if userInput not in options:
        print("Invalid input, try again")
        continue_rec(userName, userEmail, userID, quarter, need_courses)
    elif userInput == "yes":
        index = season_options.index(quarter)
        index = (index + 1) % 4
        current_season = season_options[index]
        rec_course(userName, userEmail, userID, current_season, need_courses)
    elif userInput == "no":
        exit()
    else:
        print("How did you get here")
        continue_rec(userName, userEmail, userID, quarter, need_courses)


# Function to recommend courses for the quarter
def rec_course(userName, userEmail, userID, quarter, need_courses):
    season_course = []
    rec_course = []
    recs = []
    option=["yes","no"]
    for course in need_courses:
        season = cd.dict[course]
        season.insert(0, course)
        season_course.append(season)
    for item in season_course:
        for course in item:
            if quarter in course:
                rec_course.append(item)
                continue
    print("In %s, you could take:\n" % (quarter))
    for item in rec_course:
        if len(item) > 2:
            offered = "Multiple quarters"
        elif len(item) == 2:
            offered = "Only this quarter"
        else:
            print("How are you here")
            offered = "Error please rerun the code"
        course = item[0]
        print(course + "  |  The course is offered: %s" % (offered))
        recs.append(course)
    print("")
    write_recommendations_to_csv(userName, userEmail, userID, quarter, recs)
    print("Your information along with the reccomended courses have been put into a .csv file")
    bool=input("Would you like to see the file:").lower()
    while bool not in option:
        bool=input("Invalid input, try again:").lower()
    if bool == "yes":
        print("")
        print(read_info("%s_recommendations.csv"%(quarter)))
    print("")
    continue_rec(userName, userEmail, userID, quarter, need_courses)


# Function to write recommendations to CSV
def write_recommendations_to_csv(userName, userEmail, userID, quarter, recs):
    with open('%s_recommendations.csv' % (quarter), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([userName, userEmail, userID, quarter, ", ".join(recs)])


# Function to greet the user and display completed courses
def greeting(comp_courses, core_courses, userName):
    core = 0
    complete = 0
    for course in core_courses:
        core += 1
    for course in comp_courses:
        complete += 1
    display = ""
    for item in comp_courses:
        display += item + ", "
    print("")
    print("=" * 60)
    print("Hi %s\nThe courses you have taken are: %s \nYou have completed: %s percent of the required course" % (
    userName, display, round(complete / core * 100, 2)))
    print("=" * 60)


# Function to validate email
def emailVerify(userEmail):
    if "@bellevuecollege.edu" not in userEmail:
        print("Invalid email, try again")
        user_info()
    else:
        before = userEmail.replace("@bellevuecollege.edu", "")
        count = 0
        for char in before:
            count += 1
        if count < 2:
            print("Too less characters, try again")
            user_info()


# Function to validate name
def nameVerify(userName):
    if " " not in userName:
        print("Invalid name, try again")
        user_info()


# Function to validate student ID
def idVerify(userID):
    if userID.isdigit():
        digits = 0
        for number in userID:
            digits += 1
        if digits < 9:
            print("Not enough numbers, try again")
            user_info()
        elif digits > 9:
            print("Too many numbers, try again")
            user_info()
    if not userID.isdigit():
        print("Non-numberical values are detected, try again")
        user_info()


# Function to read the courses CSV file
def read_csv(filename):
    courses = []
    list_courses = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            courses.append(row)
    for course in courses:
        list_courses.append(course[0])
    return list_courses
#Function to read (quarter)_reccomendations.csv files
def read_info(filename):
    courses = []
    list_courses = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            courses.append(row)
    for course in courses:
        for item in course:
            list_courses.append(item)
    return list_courses

# Innitializes the program
if __name__ == "__main__":
    main()