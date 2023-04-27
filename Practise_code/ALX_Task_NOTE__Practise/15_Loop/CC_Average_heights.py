# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
print (student_heights)
# Convert the input to int
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

# 12 12 23 14 12 4 45
#Write your code below this row 👇

# Get the total of heights 
total_height = 0
for heights in student_heights:
     total_height += heights
print(f"total = {total_height}\n")

# Get the total number of students
num_of_students = 0
for students in student_heights:
     num_of_students += 1
print(f"The lenghts of students is {num_of_students}\n")

# The Average number is then

print(f"The avarage is {total_height/num_of_students:.2f}")
