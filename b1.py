#test for student
try: #khối lệnh có thể xảy ra lỗi 
   print('nhập vào a')
   a = int(input())
   print('nhập vào b')
   b = int(input())
   c = a + b 
   print('Tổng của a và b là:', c)
except: # khối lệnh đcc thực thi khi lỗi xảy ra .
    print('Đã xảy ra lỗi khi nhập dữ liệu. Vui lòng thử lại.')
