dict = {
    "BATECH 165": ["fall", "winter", "spring", "summer"],
    "BUS 120": ["fall", "winter", "spring", "summer"],
    "DEV 108": ["fall", "winter", "spring", "summer"],
    "BUS& 101": ["fall", "winter", "spring", "summer"],
    "ENGL& 101": ["fall", "winter", "spring", "summer"],
    "MATH 138": ["fall", "winter", "spring", "summer"],
    "ECON& 201": ["fall", "winter", "spring", "summer"],
    "PHIL 260 or CMST 250": ["fall", "winter", "spring", "summer"],
    "ACCT 320": ["spring"],
    "BUS 300": ["fall", "winter"],
    "BUS 310": ["winter"],
    "BUS 355": ["fall", "winter", "spring"],
    "BUS 400": ["spring"],
    "BUS 490": ["fall", "spring"],
    "BUSIT 103": ["fall", "winter", "spring", "summer"],
    "CMST 340": ["fall", "winter", "summer"],
    "DEV 312": ["fall", "winter", "spring"],
    "ECON& 202": ["fall", "winter", "spring", "summer"],
    "ENGL 201 or ENGL 271 or ENGL 235": ["fall", "winter", "spring", "summer"],
    "PHIL 360 or PHIL 375": ["fall", "winter", "spring", "summer"],
    "MKTG 200 or MKTG 261 or MKTG 262": ["fall", "winter", "spring"],
    "BATECH 268": ["fall", "spring"],
    "BUS 450": ["fall"],
    "DEV 300 or DEV 160": ["fall", "winter", "spring"],
    "MKTG 461 or MKTG 462 or DATA 331 or DATA 333": ["fall", "winter", "spring"],
    "BATECH 389 or IT 330": ["winter", "spring", "summer"],
}
def newinput(prompt):
    user_input = input(prompt).lower()
    if user_input == "exit":
        print("\nHave a nice day")
        exit()
    return user_input