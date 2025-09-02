num = int(input("Please enter a number: "))
count = 1 if num == 0 else 0
num = (num)

while num > 0:
    num //= 10
    count += 1
    
print("The number of digits is:", count)