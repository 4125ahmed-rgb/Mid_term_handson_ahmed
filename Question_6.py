class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # initialize base class
        self.student_id = student_id

    def displayDetails(self):
        print(f"Name: {self.name}")
        # Access private variable using _ClassName__attribute
        print(f"Age: {self._Person__age}")
        print(f"Student ID: {self.student_id}")

# Create an object
s1 = Student("Alice", 20, "S101")

# Change s1's age to 25
s1._Person__age = 25  # modifying private attribute safely

def checkAge():
    if s1._Person__age > 18:
        print("Age is above 18")
    else:
        print("Age is 18 or below")

# Call the functions
s1.displayDetails()
checkAge()
