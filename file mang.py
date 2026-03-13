file=open("tops.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File written successfully")

print("*"*50)

file=open("tops.txt","r")
print(file.read())
file.close()

print("*"*50)

file=open("tops1.txt","a")
file.write("\nnow this file is append")
file.close()
print("File appended successfully")

print("*"*50)

file=open("tops2.txt","w+")
file.write("This is file management demo using python.")
print("current File position:",file.tell())
file.seek(10)
print("File Data:",file.read())
file.close()
print("*"*50)

