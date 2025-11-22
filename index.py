class Expression:

    # Constructor
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("Expression object created.")

    # Method
    def calculate_sum(self):
        return self.a + self.b + self.c

    # DEstructor
    def __del__(self):
        print("Expression object deleted.")


# Object Creation
obj = Expression(10, 20, 30)

# Calling method
result = obj.calculate_sum()
print("The sum of the expression is:", result)

# Deleting object
del obj
