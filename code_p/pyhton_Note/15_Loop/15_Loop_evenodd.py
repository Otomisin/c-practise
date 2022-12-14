"""
LEARN TO PROGRAM 2
https://www.youtube.com/watch?v=swQEbZ6ez1I&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=2&ab_channel=DerekBanas

"""
i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 19:
        break
    print('Your odd values are: ', i)
    i += 1
