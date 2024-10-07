import re
def Checkpasswordvalidity(password):
    if len(password)<8:
        return "password too short"
    elif re.search(r'[A-Z]', password):
        return " Atleast 1 uppercase"
    elif re.search(r'[a-z]', password):
        return " Atleast 1 lowercase"
    elif re.search(r'[0-9]', password):
        return " Atleast 1 digit"
    elif re.search(r'[!!@#$%^&*()_]', password):
        return " Atleast 1 special character"
    else:
        return True
    
    