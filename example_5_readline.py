file_obj = open("data1.txt", "r")

# Method readline() would remember the position that has been read
# next readlines() would not return the same line
first_line = file_obj.readline() #first line of the file
second_line = file_obj.readline() #second of the file
Third_line =  file_obj.readline() # Third line of the file

print(first_line)
print(second_line) # The second line is empty
print(Third_line)
