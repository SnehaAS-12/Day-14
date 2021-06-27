#Design a simple calculator app with try and except for all use cases
def calculate():
   try:
        def add(num1, num2): 
            return num1 + num2 
        def subtract(num1, num2): 
            return num1 - num2 
        def multiply(num1, num2): 
            return num1 * num2 
        def divide(num1, num2): 
            return num1 / num2 
        print("Please select operation -\n" , "1. Add\n" , "2. Subtract\n" ,"3. Multiply\n",  "4. Divide\n")
        select = int(input("Select operations form 1, 2, 3, 4 :"))
        number_1 = int(input("Enter first number: ")) 
        number_2 = int(input("Enter second number: ")) 
        if select == 1: 
           print(number_1, "+", number_2, "=", add(number_1, number_2)) 
        elif select == 2: 
           print(number_1, "-", number_2, "=",     subtract(number_1, number_2)) 
        elif select == 3: 
           print(number_1, "*", number_2, "=", multiply(number_1, number_2)) 
        elif select == 4: 
           print(number_1, "/", number_2, "=", divide(number_1, number_2)) 
        else: 
           print("Invalid input") 
   except Exception as e:
           print(e)
calculate()


#print one message if the try block raises a NameError and another for other errors
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
 print("Something else went wrong")
  
  
#When try-except scenario is not required?

#A try statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:

except (RuntimeError, TypeError, NameError):
       pass
#A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class). For example, the following code will print B, C, D in that order:

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
#Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.

#The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution, since it is easy to mask a real programming error in this way! It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well):

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
#The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()     
        
              
#Try getting an input inside the try catch block
try:
   roll_no=int(input('Enter your roll_no: '))
except:
    print ('You have entered an invalid value.')