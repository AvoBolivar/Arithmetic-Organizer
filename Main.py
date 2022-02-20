
def organize(l, answr=False):
    # confirms  the amount of problems does not exceed 5
    if len(l) > 5:
        print("Error: Too many problems")
        exit()

    # splits the strings into a list and stores the list
    split = []
    expression = []
    one_exp = []
    for i in l:
        items = i.split()
        split.append(items)

    # converts the numbers into an integer and stores them into smaller lists containing each individual expression
    for exp in split:
        for j in range(len(exp)):
            if j%2 == 0:
                num = exp[j]
                if num.isnumeric():
                    temp = int(exp[j])
                    one_exp.append(temp)
                else:
                    print("error not a number")
                    quit()
            # this would also check if it is multiplication or division
            else:
                if exp[j] == "*":
                    print("Unable to preform multiplication")
                    exit()
                elif exp[j] == "/":
                    print("Unable to preform division")
                    exit()
                else:
                    one_exp.append(exp[j])
            if len(one_exp) == 3:
                expression.append(one_exp)
                one_exp = []

    # this simply gets the answers from each expression
    answrs = []
    for index in expression:
        if index[1] == "+":
            sum = index[0]+index[2]
        else:
            sum = index[0]-index[2]
        answrs.append(sum)

    # sets up the variables that will be printed out
    first_line = []
    second_line = []
    dashes_line = []
    answers_formatted = []
    index = 0
    spacer = "    "
    # for each expression it check for 3 cases and then adjusts the amount of spaces to each given case
    for e in expression:
        # this is to check the numbers do not exceed the length of 4 digits
        if len(str(e[0])) < 5 and len(str(e[2])) < 5:
            # this would be if both top and bottom match
            if len(str(e[0])) == len(str(e[2]))+1:
                first_line.append(str(e[0])+spacer)
                second_line.append(str(e[1])+str(e[2])+spacer)
                dash_length = len(str(e[0]))
                dash = "_"
                dashed_string = ""
                for i in range(dash_length):
                    dashed_string += dash
                dashes_line.append(dashed_string)
                dashes_line.append(spacer)

            # this is when the top number is longer, so the bottom needs spaces
            if len(str(e[0])) > len(str(e[2]))+1:
                difference = len(str(e[0]))-len(str(e[2]))-1
                space = " "
                spaced_string = ""
                for i in range(difference):
                    spaced_string += space
                first_line.append(str(e[0])+spacer)
                second_line.append(e[1])
                second_line.append(spaced_string)
                second_line.append(str(e[2]))
                second_line.append(spacer)
                dash_length = len(str(e[0]))
                dash = "_"
                dashed_string = ""
                for i in range(dash_length):
                    dashed_string += dash
                dashes_line.append(dashed_string)
                dashes_line.append(spacer)

            # this is when the bottom number is longer, so the top needs spaces
            if len(str(e[0])) < len(str(e[2]))+1:
                difference = len(str(e[2])) - len(str(e[0])) + 1
                space = " "
                spaced_string = ""
                for i in range(difference):
                    spaced_string += space
                first_line.append(spaced_string)
                first_line.append(str(e[0]))
                first_line.append(spacer)
                second_line.append(str(e[1])+str(e[2]))
                second_line.append(spacer)
                dash_length = len(str(e[2]))
                dash = "_"
                dashed_string = ""
                for i in range(dash_length+1):
                    dashed_string += dash
                dashes_line.append(dashed_string)
                dashes_line.append(spacer)
        else:
            print("error number too long")
            quit()
        space = " "
        # this would then format the answers  given 2 cases
        if len(str(answrs[index])) == len(dashed_string):
            answers_formatted.append(answrs[index])
            answers_formatted.append(spacer)
        if len(str(answrs[index])) < len(dashed_string):
            d = len(dashed_string)-len(str(answrs[index]))
            a = ""
            for i in range(d):
                a += space
            a += str(answrs[index])
            answers_formatted.append(a)
            answers_formatted.append(spacer)

        index += 1
    # this would then print the result
    for i in first_line:
        print(i, end="")
    print()
    for i in second_line:
        print(i, end="")
    print()
    for i in dashes_line:
        print(i, end="")
    print()
    if answr:
        for i in answers_formatted:
            print(i, end="")


x = [
     "500 + 230",
     "26 + 300",
     "44 - 1",
     "500 + 230",
     "9999 + 9999"
     ]

organize(x, True)
