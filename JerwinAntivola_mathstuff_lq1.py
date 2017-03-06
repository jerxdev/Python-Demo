def print_number(numbers):
    print("Numbers : ")
    for i in numbers:
        print(i)
    print_name()
        
def print_cube(numbers):
    print("Cube : ")
    for i in numbers:
        print(i, " - ", pow(i,3))
    print_name()
        
def print_total(numbers):
    total = 0
    for i in numbers:
        total += i
    print("Total :", total)
    print_name()
    
def print_product(numbers):
    total = 1
    for i in numbers:
        total *= i
    print("Product :", total)
    print_name()

def print_name():
    print("Jerwin Antivola")

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print_number(xs)
print_cube(xs)
print_total(xs)
print_product(xs)
