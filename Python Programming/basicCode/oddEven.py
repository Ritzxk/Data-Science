# finding whether number is odd or even
test = int(input("test cases : "))
for i in range(test):
    num = int(input("number : "))
    def checkOdd (num):
        if num % 2 != 0:
            return True
        else:
            return False
        
    if checkOdd(num):
        print("odd")
    else:
        print('even')
