# write a program to find out total height , number of students and average height in a list
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total1=0
for total in student_heights:
    total1+=total
average_hight=round(total1/(n+1))

print(f"total height = {total1}")
print(f"number of students = {n+1}")
print(f"average height = {average_hight}")
