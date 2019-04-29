file = open("new","w") 
print(file)
file.write("This is first line.") 
file.write("This is second line.")
file.close() 
file = open("new","r") #opening 'new'(filename) in 'read' mode
t = file.read() # reading file
print(t)
file.close()