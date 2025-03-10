import re 

def input_title_validation(title):
    if not title or not title.strip():
        return "Your title is empty. Please, check."
    
    title_pattern = r'^[A-Za-z0-9\s\.,!?\'"-]{1,255}$'

    if not re.fullmatch(title_pattern, title):
        return "Invalid title. Please, check for allowed characters (A-Z, 0-9, spaces, and specific punctuation)."

    return True 