# Get sum of all elements in the integer array getsum

def get_sum(numbers:int)->int:

# i am assuming the sum is zero

    sum = 0

    # we take list of number and we need to iterat the each number to add so using for loop

    for number in numbers:

# all elemnt are adding on one varibale 

        sum = sum + number
    
    return sum

# invocation code

number = [1,2,3,4]

sum_of_numbers = get_sum(number)

print(f"sum of numbers = {sum_of_numbers}")


# OR

def getsumv2(numbers1)-> int:

    sum = 0

    length = len(numbers1)

    for index in range(0, length, 1):

        sum = sum + numbers1[index]

    return sum

# invocatoin code

numbers1 = [1,2,3]

sum_of_number1 = getsumv2(numbers1)

print(f"sum of numbers1 = {sum_of_number1}")