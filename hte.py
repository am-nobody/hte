import generate
import output
import sys
import os

# Validate Arguments.
args = sys.argv
def deleteArgs(num):
    i = 0
    while (i < num):
        del args[0]
        i += 1
deleteArgs(1)

if (len(args) > 0):
    initialCommand = args[0]
    templateName = "None"
    options = {}
    deleteArgs(1)
    if (initialCommand not in ["help", "gen", "new", "del", "list"]):
        initialCommand = "Invalid"
    else:
        if (initialCommand == "gen"):
            if (len(args) == 1):
                templateName = args[0]
                deleteArgs(len(args))
            elif (len(args) > 1):
                templateName = args[0]
                deleteArgs(1)
                if (len(args) > 0):
                    if (len(args) >= 2):
                        while (len(args) > 0):
                            if (len(args) > 1):
                                if (args[0] == "-o" or args[0] == "-d"):
                                    if (args[0] == "-o"):
                                        if (args[1] == "png" or args[1] == "html" or args[1] == "pdf"):
                                            options[args[0]] = args[1]
                                            deleteArgs(2)
                                        else:
                                            print("\n > Invalid Output Format.\n")
                                            deleteArgs(len(args))
                                            initialCommand = "Invalid"
                                            templateName = "None"
                                    else:
                                        if (os.path.exists(args[1])):
                                            options[args[0]] = args[1]
                                            deleteArgs(2)
                                        else:
                                            print("\n > Invalid Directory.\n")
                                            deleteArgs(len(args))
                                            initialCommand = "Invalid"
                                            templateName = "None"
                                else:
                                    deleteArgs(len(args))
                                    initialCommand = "Invalid"
                                    templateName = "None"
                            else:
                                deleteArgs(len(args))
                                initialCommand = "Invalid"
                                templateName = "None"          
                    else:
                        initialCommand = "Invalid"
                        templateName = "None"
            else:
                initialCommand = "Invalid"
                templateName = "None"
        elif (initialCommand == "new"):
            if not (len(args) == 1):
                initialCommand = "Invalid"
                templateName = "None"
            else:
                templateName = args[0]
                deleteArgs(len(args))
        elif (initialCommand == "del"):
            if not (len(args) == 1):
                initialCommand = "Invalid"
                templateName = "None"
            else:
                templateName = args[0]
                deleteArgs(len(args))
        else: # Help / List commands.
            deleteArgs(len(args))
else:
    initialCommand = "Invalid"
    templateName = "None"
    options = {}

# Input Validation Debug Lines
#    print("Command: " + initialCommand)
#    print("Template: " + templateName)
#    print("Options: " + str(options))

if (initialCommand == "help"):
    print('''
        Commands
        --------

        help - Display this menu.

        list - Display existing templates.

        gen - Generate HTML from a template.
            Options:
            name - Name of the template. (REQUIRED)
            -d dir - The output directory. (OPTIONAL)
            -o format - The output format. (OPTIONAL)
                (png, html, pdf)

        new - Create a new empty template.
            Options:
            name - Name of the template. (REQUIRED)

        del - Delete a template.
            Options:
            name - Name of the template. (REQUIRED)


        Input Modifiers (OPTIONAL)
        ---------------
        (To be put before a input of your desired field.)
        Ex.
            Money: [$][M]5/2 -> 2.50

        [M] - Compute an expression.
        [$] - Output as a dollar amount.
        [#] - Replace character with random digit 0-9.
        [L] - Replace character with random uppercase letter.
        [l] - Replace character with random lowercase letter.
    ''')
elif (initialCommand == "new"):
    response = generate.newTemplate(templateName)
    print("\n > " + response + "\n")
elif (initialCommand == "del"):
    response = generate.deleteTemplate(templateName)
    print("\n > " + response + "\n")
elif (initialCommand == "list"):
    response = generate.getTemplates()
    print("\n")
    for name in response:
        print(" > " + name)
    print("\n")
elif (initialCommand == "gen"):
    outputDir = "./output"
    outputFormat = "html"
    for option in options:
        if (option == "-o"):
            outputFormat = options[option]
        if (option == "-d"):
            outputDir = options[option]

    html = generate.editTemplate(templateName)
    output.output(outputDir, outputFormat, html)
    
else:
    print("\n > Invalid statement. Try 'help'.\n")