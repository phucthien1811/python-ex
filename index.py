n = input("Nhập số nguyên: ")
stack = []

# Push từng ký tự vào stack
for ch in n:
    stack.append(ch)

# Pop ra -> in ngược
print("Số đảo ngược:", end=" ")
while stack:
    print(stack.pop(), end="")
