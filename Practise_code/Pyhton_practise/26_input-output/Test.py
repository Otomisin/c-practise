
with open('test.txt', 'r') as f:
     f_content1 = f.read()
     f_content2 = f.readline() # This reads one line for 
     f_content3 = f.readlines()

     print(f_content1)
     print(f_content2, end=' ') # ' ' would remove the spaces at the end of the print line
     print(f_content3)
     