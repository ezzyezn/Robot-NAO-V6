def load_school_info():
    with open("Scripts/school_info.txt", "r", encoding="utf-8") as file: 
        school_info = file.read()
    
    return school_info.splitlines()