from pathlib import Path

# Path to the folder with all knowledge files
knowledge_dir = Path(__file__).resolve().parent.parent / "knowledge"

def load_school_info():
    lines = []
    
    # Load every .txt file except the source metadata file
    for file_path in knowledge_dir.glob("*.txt"):
        if file_path.name == "sources.txt":
            continue
        
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
               line =  line.strip()
               
               if line:
                   lines.append(line)
                   
    return(lines)