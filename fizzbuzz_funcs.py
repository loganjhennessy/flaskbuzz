def fizzbuzz_gen(start=1, end=100):
    pass

def fizzbuzz_reg(start=1, end=100):
    output=[]
    for num in range(start, end+1):
        if num % 3 == 0 and num % 5 == 0:
            output.append('fizzbuzz')
        elif num % 3 == 0:
            output.append('fizz')
        elif num % 5 == 0:
            output.append('buzz')
        else:
            output.append(str(num))
    return output
