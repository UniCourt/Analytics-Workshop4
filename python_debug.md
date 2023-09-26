# Python Debugging


## Introduction to Debugging in Python

Debugging in Python is the process of identifying and resolving errors, bugs, or unexpected behavior in your Python code. It's an essential skill for any programmer. Debugging helps you track down and fix these issues, making your code more reliable and efficient.

1. **Types of Errors:**
   - **Syntax Errors:** These are errors that occur when your code violates the Python syntax rules. They are typically easy to spot as Python will raise a "SyntaxError" with a specific message pointing to the problematic line.
       
   Code:  
         
         def print_message()
               print("Hello, world!")
         
         print_message()
   
   Error:
         
         File "example.py", line 1
             def print_message()
                               ^
         SyntaxError: invalid syntax


   - **Runtime Errors (Exceptions):** These errors occur during the execution of your code. Python raises exceptions when it encounters an issue, such as trying to divide by zero (ZeroDivisionError) or accessing an index that doesn't exist in a list (IndexError).

   Code:
 
      numerator = 10
      denominator = 0
      
      result = numerator / denominator

   Error:
      
      ZeroDivisionError: division by zero


   - **Logical Errors (Bugs):** These are the trickiest to identify because they don't produce errors or exceptions but lead to incorrect program behavior. Debugging these errors often involves inspecting the code's logic and data flow.

   Code:
      
      def calculate_average(numbers):
          total = sum(numbers)
          average = total / len(numbers)
          return average

      numbers = [10, 20, 30, 40, 50]
      average = calculate_average(numbers)
      print("The average is:", average)



In this example, we're trying to calculate the average of a list of numbers. However, there's a logical error in the code. When you run it, you won't get a syntax error or exception, but the result will be incorrect. The issue is that we're dividing by the length of the list, which should be the count of numbers, not the sum of numbers.


2. **Debugging Tools:**
   - **Print Statements:** One of the simplest debugging techniques is to add print statements in your code to display variable values, control flow, and messages at specific points. This helps you trace the program's execution.

   - **Debugger:** Python comes with a built-in debugger module called "pdb." You can set breakpoints, step through code, inspect variables, and more using the debugger. To use it, import the `pdb` module and insert `pdb.set_trace()` at the point where you want to start debugging.

   - **IDEs and Code Editors:** Integrated Development Environments (IDEs) like PyCharm, Visual Studio Code, and Jupyter Notebook have built-in debugging tools that provide a graphical interface for debugging, making the process more user-friendly.


3. **Common Debugging Techniques:**
   - **Inspect Variable Values:** Use print statements or the debugger to check the values of variables at different points in your code. This can help you identify incorrect values or unexpected behavior.

   - **Isolate the Problem:** Divide your code into smaller sections and test each section separately. This can help you pinpoint which part of your code is causing the issue.

   - **Check Inputs and Outputs:** Ensure that the input data and the expected output are as expected. Incorrect inputs or output can lead to unexpected behavior.

   - **Read Error Messages:** Python provides informative error messages when exceptions occur. Read these messages carefully, as they often indicate the location and type of the error.

   - **Documentation and Community Resources:** Refer to Python's official documentation and online communities like Stack Overflow for help with specific error messages or coding challenges.


4. **Practice and Patience:** Debugging can be a time-consuming process, especially for complex issues. It requires patience and persistence. Keep trying different approaches until you find the root cause of the problem.


5. **Version Control:** Using version control systems like Git can help you track changes in your code, making it easier to identify when and where issues were introduced.



## Debugging the code in Python

Exercise
   

Copy the following program to a text file and save it as test_demo.py:

Code:

      print("This is line number 1")

      a = 1
      b = 2
      sum = a + b

      print(f"The sum is {sum}")
      
      for i in range(5):
          sum += 1
      
      print(f"The sum at the end is {sum}")

Now you can debug this file in one of two ways:

1. From the command line.
2. By importing the "pdb" module in the code.


### 1. From the command line.

Run the following command in the command line and you will see the Python Debugger in action:

      python3 -m pdb breakpoint_demo.py

 press q to quit the debugger.


### 2. By importing the "pdb" module in the code.

Now instead of using -m pdb in the Command Line, let us import the pdb module inside the code.

Open your code and add the below two lines in the beginning:
      
      import pdb
      pdb.set_trace()

Now your code should look something like this:

      import pdb
      pdb.set_trace()
      
      print("This is line number 1")
      
      a = 1
      b = 2
      
      sum = a + b
      
      print(f"The sum is {sum}")
      
      for i in range(5):
          sum += 1
      
      print(f"The sum at the end is {sum}")



Now you can run this code in your terminal as follows:

      python3 test_demo.py


 press q to quit the debugger.
 
But for Python versions 3.7 and higher, a new method breakpoint() was introduced.

In your previous code replace both these lines

      import pdb
      pdb.set_trace()
with

      breakpoint()

And run the file:

      python3 test_demo.py

The experience should be similar as while you were using pdb and breakpoint.