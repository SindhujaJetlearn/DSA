# Class User to explain the concept of hidden attribute - cant be accessed by object directly

class User:

    # hidden variable
    __password = "Abc@123"

    def __init__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username
        
    def getPassword(self):
        return self.__password

    def setPassword(self):
        old_password = input("Enter your old password - ")
        if old_password == self.__password:
          new_password = input("Enter your new password - ")
          self.__password = new_password

        else:
          print("Please enter the correct password.")

# Concept of hidden variable
pulkit = User("Pulkit", "pulkit.jetlearn@gmail.com", "major_pulkit")
# attribute is accessible from code
print(pulkit.name)
# hidden password is not accessible
#print(pulkit.__password)
print(pulkit.getPassword())
pulkit.setPassword()