def repeat_string(string,number):
    print(string * number)
# მაგალითი
repeat_string("hello",5)
# output: hellohellohellohellohello

def print_if_true(condition, string):
    if condition:
        print(string)
# მაგალითები
print_if_true(True, "GOA")    #output:GOA
print_if_true(False, "GOA")    #output: (არაფერი დაიბეჭდება)

def print_cube(number):
    print(number ** 3)
# მაგალითი
print_cube(5)
#output: 125

def is_prime(number):
    if number < 2:
        print(False)
        return
    for i in range(2, int(number ** 0.5) + 1):
        if number % i ==0:
            print(False)
            return
        print(True)
# მაგალითები
is_prime(7)    # output:True
is_prime(8)    # output:False        