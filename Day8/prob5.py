## Generate fibonacci series

def gen_fibo(n):
    fibo_list = [0,1]

    while len(fibo_list) < n:
        next_element = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(next_element)

    return fibo_list

n = 15
output = gen_fibo(n)
print(f"Your fibonacci series with {n} elements is : {output}")