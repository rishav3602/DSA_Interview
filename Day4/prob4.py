## Tell the number of occurance of all the characters in a given string

def ech_chr_count(str):
    str = str.lower().replace(" ","")
    dict = {}
    for chrs in str:
        count = str.count(chrs)
        dict[chrs] = count
    return dict

string = "hello my name is Rishav kumar and I am a student of BCA"
output = ech_chr_count(string)
print(output)
