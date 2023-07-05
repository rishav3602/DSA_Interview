## Tell the number of occurance of a character in a given string

def chr_count(str,chr):
    str = str.lower().replace(" ","")
    count = str.count(chr)
    return count

string = "Hello my name is rishav kumar"
chr = "a"
output = chr_count(string, chr)
print(f"{chr} appread {output} times")
