## Reverse a string

string = "My name is Rishav kumar and I am pursuing BCA"
rev_str = string[::-1]
print(rev_str)


def rev_str(strng):
    list_str = list(strng)
    start = 0
    end = len(str) - 1
    while start < end :
        list_str[start] , list_str[end] = list_str[end] , list_str[start]
        start += 1
        end -= 1

    rev_string = "" .join(list_str)
    return rev_string

str = "Hey, Nice to meet you take care bye...."
output = rev_str(str)
print(f"your reversed string is :\n {output}")