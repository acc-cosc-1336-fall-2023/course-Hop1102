def test_config():
    return True

val3 = 5

def is_number_odd(num):
    return num % 2 == 1 

def local_function_variable(val):
    val = 100
    val2 = 10

def global_variable():
    val3 = 10
    print(val3) 

def global_variable_1():
    global val3
    val3 = 10
    print(val3)

def global_variable_2():
    print(val3)

def get_random_number(min, max):
    
