from re import fullmatch
import sys
import os
import re

f = open("question6.txt", "r")
r = f.read()
# converts the list of lists into a lists of strings as list_String
list_String = []
list_String = r.split( )

java_While = False
java_If = False
# Java while statement

nextToken = None
IF_code = "if"
WHILE_code = "while"
LEFT_PAREN = "("
RIGHT_PAREN = ")"
ELSE_CODE = "else"


for i in list_String:
    if(re.fullmatch("([\w]|[+]|[=]|[\==]|[-]|[\]|[\\]|[\/]|[*]|[++]|[--]|[%]|[&&]|[||]|[!=]|[(]|[)]|[{]|[}])*", i)):
        print(i + ": " + "Non-Alphanumeric")
    else:
        nextToken+=1
# RDA for Mathematical Assignment Statement
def math_expr():
# checks nextToken for a variable
    if((re.fullmatch("[a-zA-Z0-9]", nextToken))):
        return var()
    else:
        return error()
    # uses Regex to see if the nextToken is a assignment operator
    if((re.fullmatch("([\w]|[+]|[=]|[\==]|[-]|[\]|[\\]|[\/]|[*]|[++]|[--]|[%]|[&&]|[||]|[!=]|[(]|[)]|[{]|[}])*", nextToken))):
        return error()
    else:
        return 
    if((re.fullmatch("[a-zA-Z0-9]", nextToken))):
        return error()
    else:
        return var()

# RDA for Mathematical Expression Statement
def math_assign():
    # checks to see if the variable is a variable
    if(re.fullmatch("[a-zA-Z0-9]", nextToken)):
        return var()
    else:
        return error()
    # checks the nextToken if it is an assignment operator
    if(re.fullmatch("[==]", nextToken)):
        return expr()
    else:
        return error()
    # checks next token to see if it is a variable
    if(re.fullmatch("[a-zA-Z0-9]", nextToken)):
        return lex()
        return statement()
    else:
        return error()


# RDA for Java While statement
def while_stmt():
    # checks to see if first token is 'while'
    if (nextToken != WHILE_code):
        return error()
    else: 
        return lex()
    # checks for first left parenthesis 
    if (nextToken != LEFT_PAREN):
        return error()
    else: 
    # parses the Boolean expression
        boolexpr()
    if (nextToken != RIGHT_PAREN):
        return error()
    else:
        return statement()

# RDA  for Java If statement
def if_stmt():
    # checks to see if the first token is 'if'
    if (nextToken != IF_code):
        return error()
    else: 
        return lex()
    # check for the first left parenthesis
    if (nextToken != LEFT_PAREN):
        return error()
    else: 
    # parses the Boolean expression
        boolexpr()
    # checks for the first right parenthesis
    if (nextToken != RIGHT_PAREN):
        return error()
    else:
        return statement()
    # if an else is net, parse the else clause
    if (nextToken == ELSE_CODE):
        return lex()
        return statement()
