"""
    Isomorphic string .
"""

def isomorphic_string(string_1, string_2):
    
    if len(string_1) == len(string_2):
        mapping = {}
        mapped_character =  set()
        
        for i in range(0, len(string_1)):
            
            if string_1[i] not in mapping :
                if string_2[i] in mapped_character :
                    return False
                mapping[string_1[i]] = string_2[i]
                mapped_character.add(string_2[i])
                
            else:
                if mapping[string_1[i]] != string_2[i] :
                    return False
        
        return True
    else:
        return False


if __name__ == "__main__" :
    print(isomorphic_string("egg", "add"))  # True
    print(isomorphic_string("foo", "bar"))  # False
    print(isomorphic_string("paper", "title"))  # True