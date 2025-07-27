num_string = '12'
num_integer = 23

print("Kiểu dữ liệu của num_string trước khi ép kiểu:", type(num_string))

# Ép kiểu tường minh
num_string = int(num_string)

print("Kiểu dữ liệu của num_string sau khi ép kiểu:", type(num_string))

num_sum = num_integer + num_string
print("Tổng:", num_sum)
print("Kiểu dữ liệu của num_sum:", type(num_sum))

def process_dict(data):
    match data:
        case {"name": name, "age": age}:
            return f"Name: {name}, Age: {age}"
        case {"name": name}:
            return f"Name: {name}, Age: unknown"
        case _:
            return "Unknown structure"

print(process_dict({"name": "Alice", "age": 30}))  # Output: Name: Alice, Age: 30
print(process_dict({"name": "Bob"}))               # Output: Name: Bob, Age: unknown
print(process_dict({"age": 25}))                   # Output: Unknown structure


#------------------------------------------------------------------------------------

class Person:
    __match_args__ = ("name", "age")  #Python không hiểu cú pháp case Person(name, age): vì class Person của bạn không hỗ trợ pattern matching theo kiểu positional.

    def __init__(self, name, age): #Nhưng Python chỉ hiểu pattern như vậy nếu bạn dùng dataclass hoặc __match_args__.
        self.name = name            # Phải dùng python 3.10 cho match case
        self.age = age                #Nếu bạn không muốn dùng dataclass, có thể thêm __match_args__ thủ công. 

def process_person(person):
    match person:
        case Person(name, age):
            return f"Name: {name}, Age: {age}"
        case _:
            return "Unknown structure"

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(process_person(p1))  # Output: Name: Alice, Age: 30
print(process_person(p2))  # Output: Name: Bob, Age: 25
print(process_person("Unknown"))  # Output: Unknown structure

for i in range(10):
    if i == 5:
        break
    print(i)

#------------------------------------------------------------------------------------

print("dưới đây là dùng continue")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)



print(" có bao nhiêu phân tử có phải n +1 không ?")
for i in range(10):
    print(i)
#à vậy là range (10 có 10 phần tử từ 0 đến 9)
print("dưới đây là dùng pass")
for i in range(10):                 
    if i % 2 == 0:
        pass  # Không làm gì cả, chỉ để giữ cấu trúc vòng lặp
    else:
        print(i)  # In ra các số lẻ




print("Dưới đây là ví dụ về vòng lặp for với danh sách")
fruits = ['apple', 'banana', 'cherry'] # có 3 phần tử 
for fruit in fruits:           # fruit = apple in ra apple, sau đó fruit = banana in ra banana, cuối cùng fruit = cherry in ra cherry
    print(fruit)




print("Dưới đây là ví dụ về vòng lặp for với chuỗi")
word = "Python"
for letter in word:
    print(letter)




print("Dưới đây là ví dụ về vòng lặp for với tuple")
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)




print("vòng lặp for với các chỉ số của dãy")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")



print("Dưới đây là ví dụ về vòng lặp for với từ điển")
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")


#------------------------------------------------------------------------------------
print("Sử dụng câu lệnh else với vòng lặp for")
for i in range(5):
    print(i)
else:
    print("Vòng lặp đã kết thúc") 
#Khối lệnh else sẽ được thực thi khi vòng lặp kết thúc mà không gặp phải câu lệnh break:

#------------------------------------------------------------------------------------
#Bạn có thể sử dụng vòng lặp for lồng nhau để lặp qua các dãy phức tạp hơn
print("Vòng lặp for lồng nhau")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
#vòng lặp for bên ngoài lặp qua từng hàng của ma trận, và vòng lặp for bên trong lặp qua từng phần tử trong hàng đó.

print("Dưới đây là ví dụ về list comprehension với for")
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
print("-------------------------------------------------------------------------------------")
for i in range(1, 4):
    print(i)
else:
    print("Vòng lặp đã kết thúc mà không gặp phải câu lệnh break")
print("-------------------------------------------------------------------------------------") 
for i in range(1, 4):
    if i == 2:
        break
    print(i)
else:
    print("Vòng lặp đã kết thúc mà không gặp phải câu lệnh break")
print("-------------------------------------------------------------------------------------") 
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Vòng lặp đã kết thúc mà không gặp phải câu lệnh break")
print("-------------------------------------------------------------------------------------")
i = 1
while i < 4:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("Vòng lặp đã kết thúc mà không gặp phải câu lệnh break")

print("-------------------------------------------------------------------------------------")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
print("-------------------------------------------------------------------------------------")
for i in range(1, 4):
    for j in range(1, 4):
        print(j , end = " ")
    print()
    
print("-------------------------------------------------------------------------------------")

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"i: {i}, j: {j}")
    else:
        print(f"Vòng lặp bên trong đã kết thúc tự nhiên cho i = {i}")
print("-------------------------------------------------------------------------------------")
def contains_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("Danh sách chứa số chẵn")
            break
    else:
        print("Danh sách không chứa số chẵn")

contains_even_number([1, 9, 8])
contains_even_number([1, 3, 5])

print("-------------------------------------------------------------------------------------")
def demo(x):
    print(type(x), x)

demo([1, 2, 3])    # <class 'list'> [1, 2, 3]
demo("abc")        # <class 'str'> abc
demo(42)           # <class 'int'> 42
demo(3.14)        # <class 'float'> 3.14
demo(True)         # <class 'bool'> True

print("-------------------------------------------------------------------------------------")
count = 0
while count < 5:
    print("Số đếm là:", count)
    count += 1

print("--------------------------------------------------------------------------------------")
count = 0
while count < 5:
    print("Số đếm là:", count)
    count += 1
else:
    print("Vòng lặp đã kết thúc.")
print("--------------------------------------------------------------------------------------")
# trên 1 dòng lệnh 
count = 0
while count < 5: print("Số đếm là:", count); count += 1

print("--------------------------------------------------------------------------------------")
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1

print("--------------------------------------------------------------------------------------")
count = 0
while count < 10 and count % 2 == 0:
    print("Số đếm là:", count)
    count += 2
print("--------------------------------------------------------------------------------------")
s = "phuc thien"
for char in s : 
    s = s.replace(char, char.upper(), 1)
print(s)  # In ra: PHuC THIeN
print("--------------------------------------------------------------------------------------")
numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]
no = int(input('Enter a number: '))
for num in numbers:
    if num == no:
        print('Number found in list')
        break
else:
    print('Number not found in list')
print("--------------------------------------------------------------------------------------")
