# # Python program to check whether a given number is an Armstrong number/ narcissistic number or not.
num = int(input("Enter a number : "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

# program that prints all Armstrong numbers in a given range.

t1 = int(input("Enter the minimum value: "))
t2 = int(input("Enter the maximum value: "))
print("Armstrong numbers in the range:")
for num in range(t1, t2 + 1):
    original = num
    sum = 0
    n = len(str(num))
 
    while num > 0:
        digit = num % 10
        sum += digit ** n
        num //= 10
 
    if sum == original:
        print(original)