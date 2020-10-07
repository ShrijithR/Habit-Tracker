#!HABIT TRACKER
#                                           Tracker and analysis of habits

import os, subprocess, HabitTrackerFunctions as HT, importlib
import HabitListFile as HLF
import pyinputplus as pyip

#                                           Keep looping until 'quit' is chosen
while True:
#                                           Run the datefinder function to make use of the attributes
    HT.dateFinder()
    try:
        print("What do you want to do? ", end="")
        functionChoice = pyip.inputMenu(
            ["Analyse", "Compare", "Goal check", "Update Goals", "Update tracker", "Quit"],
            numbered=True,
        )
    #                                           Create a directory for the output files
        os.makedirs("OutputFiles", exist_ok=True)
        if functionChoice == "Analyse":
            habitChoice, dateAObj, dateBObj = HT.infoReq()
    #                                           run the function from from the Habit
            analysisDict = HT.analysis(dateAObj, dateBObj)
            if habitChoice == "all":
                outputFileName = f"Analysis of all habits {dateAObj.day}.{dateAObj.month} - {dateBObj.day}.{dateBObj.month}.txt"
                outputFile = open(
                    os.path.join(os.path.abspath("OutputFiles"), outputFileName), "w"
                )
                outputFile.write(f"{'HABIT'.ljust(20,'-')}{'DONE'.ljust(10,'-')}NOT DONE\n")
                for habit in list(analysisDict.keys()):
                    outputFile.write(
                        habit.ljust(20, " ")
                        + str(analysisDict[habit]["yes"]).ljust(10, " ")
                        + str(analysisDict[habit]["no"])
                        + "\n"
                    )
            else:
                outputFileName = f"Analysis of {habitChoice} {dateAObj.day}.{dateAObj.month} - {dateBObj.day}.{dateBObj.month}.txt"
                outputFile = open(
                    os.path.join(os.path.abspath("OutputFiles"), outputFileName), "w"
                )
                outputFile.write(f"{'HABIT'.ljust(20,'-')}{'DONE'.ljust(10,'-')}NOT DONE\n")
                outputFile.write(
                    habitChoice.ljust(20, " ")
                    + str(analysisDict[habitChoice]["yes"]).ljust(10, " ")
                    + str(analysisDict[habitChoice]["no"])
                    + "\n"
                )
            outputFile.close()
            fileOpenChoice = pyip.inputYesNo(
                prompt="Do you want to open the output text file?\n"
            )
    #                                           Open the output files if the choice is yes
            if fileOpenChoice == "yes":
                subprocess.Popen(
                    [os.path.join(os.path.abspath("OutputFiles"), outputFileName)],
                    shell=True,
                )
        elif functionChoice == "Goal check":
            habitChoice, dateAObj, dateBObj = HT.infoReq()
            HT.goalcheck(habitChoice, (dateAObj, dateBObj))
            fileOpenChoice = pyip.inputYesNo(
                prompt="Do you want to open the output text file?\n"
            )
            if fileOpenChoice == "yes":
                subprocess.Popen(
                    [
                        os.path.join(
                            os.path.abspath("OutputFiles"), HT.goalcheck.outputFileName
                        )
                    ],
                    shell=True,
                )
        elif functionChoice == "Update Goals":
            print("Enter the habit you want to update or choose all ")
            habitChoice = pyip.inputMenu(HLF.habitList + ["all"], numbered=True)
            HT.updateGoals(habitChoice)
        elif functionChoice == "Update tracker":
            HT.update()
            fileOpenChoice = pyip.inputYesNo(prompt="Do you want to open the tracker?\n")
            if fileOpenChoice == "yes":
                subprocess.Popen([HT.update.wbVersion], shell=True)
            importlib.reload(HT)
        elif functionChoice == "Compare":
            print("Select the habit you want to check. ", end="")
            habitChoice = pyip.inputMenu(HLF.habitList + ["all"], numbered=True)
            print("Enter the dates you want to check. ", end="")
            dateList = [
                "Previous week vs Current week",
                "Previous month vs current month",
                "Custom date range",
            ]
            dateChoice = pyip.inputMenu(dateList, numbered=True)
            HT.compare(habitChoice, dateChoice)
            fileOpenChoice = pyip.inputYesNo(
                prompt="Do you want to open the output text file?\n"
            )
            if fileOpenChoice == "yes":
                subprocess.Popen(
                    [
                        os.path.join(
                            os.path.abspath("OutputFiles"), HT.compare.outputFileName
                        )
                    ],
                    shell=True,
                )
        elif functionChoice == "Quit":
            break
    except (KeyboardInterrupt, SystemExit):
        print('You pressed ctrl+c')
        raise
    action = pyip.inputYesNo(prompt="Do you want to perform any other action\n")
    if action == "no":
        break

