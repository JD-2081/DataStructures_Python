class Student:
    rnoll=123           # Instance variables Creation
    name="sai"
    branch="IT"
    def read(self):
        print("Reading...")
        print("branch =",self.branch)     # Aceesing the instance variables inside the function we use the self 
    def write(self):
        print("Writing...")
# Object Creation
s1=Student()
# Acessing the functions using the object
s1.read()
# Acessing the data using the object name
print("rnoll =",s1.rnoll)
# Aceesing the data using the class name
print("name =",Student.name)
# Acessing the function using the class name
s1.write()
s1.name="mani"
print("name =",s1.name)

