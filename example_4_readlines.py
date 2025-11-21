file_obj = open("data1.txt", "r")
lines = file_obj.readlines()

#this line prints 21, because lines is a list
#method 'readlines()' returns a list
print(len(lines))

#We can use for loop to print all lines, and line number
# First, a Varible of line number 
line_no = 1
for line in lines:
    print(f"Line {line_no}: {line}")
    line_no += 1 # self increase after printing every line