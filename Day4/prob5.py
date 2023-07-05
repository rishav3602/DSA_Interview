## Reverse a string without using indexing or any function

def rev_str(str):
    str = str.lower().replace(" ","")
    str_list = list(str)
    start = 0
    end = len(str_list) - 1
    
    while start < end :
        str_list[start] , str_list[end] = str[end] , str[start]
        start += 1
        end -= 1

    reversed_str = " ".join(str_list)
    return reversed_str

string = "My name is rishav kumar and  I am a final year student"
output =rev_str(string)
print(f"Your reversed string is : {output}")