# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in student_heights:
     student_heights[n]=int(student_heights[n])
# 🚨 Don't change the code above 👆

# 12 12 23 14 12 4 45
#Write your code below this row 👇
total_height = 0
for heights in student_heights:
     total_height += heights
print(heights)
     