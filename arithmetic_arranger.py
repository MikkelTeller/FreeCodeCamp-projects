def arithmetic_arranger(problems, answers = False):
    
    wrong_operands = [":", "/", "•", "*", "%","^"]

    if len(problems) > 5:
        return("Error: Too many problems.")

    lst = []

    for problem in problems:
        lst.append(None)
        for operand in wrong_operands:
            if problem.find(operand) != -1:
                return("Error: Operator must be '+' or '-'.")
    
    num = 0
    class Problem:
        ""

    for problem in problems:
        op = problem.find("+")
        operator = "+"
        if op == -1:
            op = problem.find("-")
            operator = "-"
            if op == -1:
                return("Error: The problem must include '+' or '-'.")
        lst[num] = Problem()

        lst[num].operator = operator
        lst[num].question1 = problem[:op].strip()
        lst[num].question2 = problem[op+1:].strip()
        if operator == "+":
            try:
                lst[num].answer = str(int(lst[num].question1) + int(lst[num].question2))
            except:
                return("Error: Numbers must only contain digits.")
        elif operator == "-":
            try:
                lst[num].answer = str(int(lst[num].question1) - int(lst[num].question2))
            except:
                return("Error: Numbers must only contain digits.")
        lst[num].width = max(len(lst[num].question1), len(lst[num].question2)) + 2

        num = num + 1

#Tester om tallene kun indeholder cifre

    for object in lst:
        if object.question1.isnumeric() and object.question1.isnumeric():
            continue
        else:
            return("Error: Numbers must only contain digits.")

#Tester om tallene maks er 4 cifre lange
    for object in lst:
        if len(object.question1) <= 4 and len(object.question2) <= 4:
            continue
        else:
            return("Error: Numbers cannot be more than four digits.")

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    num = 0

    for object in lst:
        for space in range(object.width-len(object.question1)):
            line1 = line1 + " "
        line1 = line1 + object.question1 + "    "

        line2 = line2 + object.operator
        for space in range(object.width-len(object.question2)-1):
            line2 = line2 + " "
        line2 = line2 + object.question2 + "    "
        
        for space in range(object.width):
            line3 = line3 + "-"
        line3 = line3 + "    "

        if answers == True:
            for space in range(object.width - len(object.answer)):
                line4 = line4 + " "
            line4 = line4 + object.answer + "    "


    if answers == False:
        return(line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip())
    elif answers == True:
        return(line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip())
    else:
        return("Error: The secund input must be either 'True' or 'False'.")
    
print(arithmetic_arranger(["2182+2","443- 54", "22 + 233"], "false"))