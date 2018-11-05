
def simple_function():
    print("Hello World")

def simple_function_2():
    print("Hello World 2")

def complex_function():
    for i in range(10):
        print("Hello World 3")

def complex_function_2(number_of_times):
    for i in range(number_of_times):
        print("Hello World 4 - ", i)

def do_addition(a, b):
    total = a + b
    return total

def do_addition_and_multiplication(a, b, d):
    result = a + b
    result = result * d
    return result

def do_rectangle_area(a, b):
    result = a * b
    return result

def do_rectangle_perimeter(a, b):
    result = 2*a + 2*b # 2*(a+b)
    return result


c = do_rectangle_area(1,3)
print("Result=", c)

c = do_rectangle_perimeter(10,7)
print("Result=", c)



# simple_function()
# simple_function_2()
# complex_function()
# complex_function_2(20)