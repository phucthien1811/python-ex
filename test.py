class First:
    def getFirst(self):
        print("Class Fist")
        
class Second:
    def getSecond(self):
        print("Class Second")

class Third(First, Second):
    def getThird(self):
        print("Class Third")

third = Third()
third.getFirst()
third.getSecond()
third.getThird()

# Kết Quả:
# Class Fist
# Class Second
# Class Thirds