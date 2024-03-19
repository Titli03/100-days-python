# write a program which will add all the numbers between 0 to 1000
target = int(input()) # Enter a number between 0 and 1000
sum_number=0
for number in range(0, target+1, 2):
  sum_number+=number
print(sum_number)

