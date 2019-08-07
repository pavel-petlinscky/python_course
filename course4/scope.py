
# Local scope

def scoped_function(arg):
    value = arg * 10
    print(value)

scoped_function(2)








# Returning something

def return_some(input_value):
    calc = input_value - 7
    print(calc)
    return calc

print(return_some(4))


# Global scope (run this in pythontutor.com)



def print_var():
    print(SOME_VAR1)


SOME_VAR1 = 'value'
print_var()


SOME_VAR = 'value'
def print_var():
    SOME_VAR = 0    # Local vars redefine names, and shadows names in outer scope!
    print(SOME_VAR)

print_var()


# Global name after function def, but before function call

def print_var():
    SOME_VAR = 0    # Local vars redefine names, and shadows names in outer scope!
    print(SOME_VAR, ANOTHER_VAR)

ANOTHER_VAR = 5

print_var()


# Global name after function def and after function call

def print_var():
    SOME_VAR = 0    # Local vars redefine names, and shadows names in outer scope!
    print(SOME_VAR, ANOTHER_VAR_2)

print_var()
ANOTHER_VAR_2 = 5



# You can not modify global scope

def modify_var():
    try:
        SOME_VAR += '_extra'
    except UnboundLocalError as e:
        print('Error', e)

modify_var()
print(SOME_VAR)


# BUT if you really want....
def modify_var():
    global SOME_VAR
    try:
        SOME_VAR += '_extra'  # Do not do this. REALLY, JUST DO NOT THIS!!!
    except UnboundLocalError as e:
        print('Error', e)

modify_var()
print(SOME_VAR)

# But you can mutate it

GLOBAL_LIST = []

def append_to_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)

append_to_list(1)
append_to_list(2)
print(GLOBAL_LIST)


# free and bounded vars
Z = 5


def bar(y):  # y - bounded
    x = 1      # x - bounded

    print(y)
    print(Z)   # Z - free

    def foo():
        print(x + y + Z)  # x, y, z - free here

    foo()

print(x)








