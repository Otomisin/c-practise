# Loop through to check if a result is not equal to zero
for i in range(2, 21):
    if (i % 2) != 0:
        print('i= ', i)

# Float number
float_num = input('what\'s your float number? ')

# Convert float number to integer
float_num = float(float_num)
print('Rounded to 2 decimals: {:.2f}'.format(float_num))