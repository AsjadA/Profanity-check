import urllib 

def read_text(file_path):
    str_file_path = str(file_path)
    file = open(str_file_path, "r")
    file_contents = file.read()
    print(file_contents)
    check_profanity(file_contents)
    
def check_profanity(text):
    text_to_check = text.replace(" ", "%20")
    website = "http://www.purgomalum.com/service/containsprofanity?text="
    with urllib.request.urlopen(website + text_to_check) as response:
        output = response.read()
    print(output)
        
# Always add r before the file_path to avoid unicode error
# Example: 
# readtext(r"\Users\Pynkiss\Desktop\Asjad.txt")