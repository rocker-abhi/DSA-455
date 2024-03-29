"""
    check whether one string is a rotation of another .
"""

def check_weather_rotate(string_1, string_2):
    substring = string_1 + string_2
    
    if string_2 in substring :
        return True
    else:
        return False
    

if __name__ == '__main__':
    string_1 = "abfyg"
    string_2 =  "gabfy" 
    if check_weather_rotate(string_1, string_2):
        print(True)
    else:
        print(False)