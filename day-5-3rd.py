target = int(input()) # Enter a number between 0 and 1000
sum_number=0
for number in range(0, target+1, 2):
  sum_number+=number
print(sum_number)

