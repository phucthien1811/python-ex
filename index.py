with open("testfile.txt", "r") as f:
    lines = f.readlines()
line1 = lines[0].strip()
numbers = line1.split()
R = float(numbers[0])
S = R * 3.14 
C = 3.14 * pow(R, 2) 

with open("output.txt", "w") as f1:
    f1.write(f"chu vi: {S}\n")
    f1.write(f"dien tich: {C}\n")
   

             
    
f.close()
f1.close()