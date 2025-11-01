
class Expression:
    # Constructor
    def __init__(self, expression):
        self.expression = expression
        print("Expression object created.")

    def evaluate(self):
        try:
            # Evaluating
            result = eval(self.expression)
            return result
        except Exception as e:
            print(f"Error evaluating expression: {e}")
            return None

    # Using method
    def display_result(self):
        result = self.evaluate()
        if result is not None:
            print(f"The result of '{self.expression}' is: {result}")
        else:
            print("Could not compute the result.")

    # Destructor
    def __del__(self):
        print("Expression object deleted.")


if __name__ == "__main__":
    print("Welcome to the Expression Solver!")
    expr_input = input("Enter a mathematical expression (e.g., 5 + 3 * 2): ")

    # Creating object
    expr = Expression(expr_input)


    expr.display_result()

    # Deleting object
    del expr
