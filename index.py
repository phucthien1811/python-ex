with open("testfile.txt", "r") as f:
    lines = f.readlines()

n = lines[0].strip()

n = int(n)  # Convert the first line to an integer

if n < 0:
    print('dữ liệu trong file ko hợp lệ')
else :
   for i in range(1,n+1):
       numbers = lines[i].split()    # ???  bước này sẽ ra gì
       a , b = map(int, numbers)  # ???  thử in ra xem
       print(f'tích của hàng {i} là {a*b}')
       
             
    
   
   
    
    

