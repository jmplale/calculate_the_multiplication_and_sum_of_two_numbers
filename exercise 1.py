# let's make a def function
def solving(num_one, num_two):
    multiply = num_one * num_two
    addition = num_one + num_two

    if multiply > 1000:
        return addition
    else:
        return multiply
    
given_one = solving(20, 30)
print("The result is:", str(given_one))