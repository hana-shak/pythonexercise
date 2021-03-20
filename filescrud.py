# python has functions for files CRUD

# Open a file => will create it, w writing inside it
myFile = open('myfile.txt','w')

# Get some info .name, closed, mode are properties
# print('Name:', myFile.name)
# print('Is closed:', myFile.closed)
# print('Opening Mode:', myFile.mode)

myFile.write('I love python')
myFile.write('I love laravel')
myFile.close()

# append to it
myFile = open('myfile.txt','a')
myFile.write('I  also like MERN')
myFile.close()

# Read from file, 100 charcter
myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)

