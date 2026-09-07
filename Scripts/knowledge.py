# Load school information from the TXT file
def load_school_info():
    # Open the file with school information
    with open("Scripts/school_info.txt", "r", encoding="utf-8") as file: 
        # Read all text from the file
        school_info = file.read()
    
    # Split the text into separate lines
    return school_info.splitlines()