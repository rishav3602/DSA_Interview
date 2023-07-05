## check if the given string is plaindrome or not


def plaindrome(str):
    rev_str = str[::-1]
    if rev_str == str:
        return True
    
    return False


string = "Rishhsi"
output = plaindrome(string)
print(output)