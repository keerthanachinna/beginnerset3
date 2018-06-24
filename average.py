n = int(input('How many numbers: '))
total_sum = 0
for n in range(n):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/n
print('Average of ', n, ' numbers is :', avg)
