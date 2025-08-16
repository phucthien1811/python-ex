with open("testfile.txt", "r") as f:
    lines = f.readlines()
line1 = lines[0].strip()
numbers = line1.split()
nums = map(int, numbers)
total = sum(nums)

with open("output.txt", "w") as f1:
    f1.write(f"The sum of the numbers is: {total}\n")
   

             
    
   
   
    
    

