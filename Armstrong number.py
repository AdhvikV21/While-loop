# take input from the user
num = int(input("Please enter a number"))

#initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num 
while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10

#display the result
if num == sum:
    print ("Number is an Armstrong number")
else:
    print("Number is not an Armstrong number")



