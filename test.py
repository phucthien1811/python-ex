class First:
    def getClass(self):
        print("Class Fist")

class Second:
    def getClass(self):
        print("Class Second")
        
class Third(First, Second):
    def getClass(self):
        super().getClass()

third = Third()
third.getClass()

# Kết Quả:
# Class Fist