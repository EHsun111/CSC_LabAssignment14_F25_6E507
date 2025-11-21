#create a file object of file "data.txt", with mode "r" which is "read"
file_object= open("data.txt", "r")
print(file_object)

# You will see and error "FileNotFoundError" Since file "Data101.txt" Not exist

file_object_error = open("data101.txt", "r")
print(file_object_error)