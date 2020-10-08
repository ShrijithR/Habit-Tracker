# **Habit-Tracker**
_Track and analyse habits_

![Image of HT](https://media.giphy.com/media/Zr9FfobRExF6FuRsJr/giphy.gif)


## Features
 _For a specific habit or all habits; For a specific date/date range or date ranges_
  * Analyse total number of hits and misses
  * Compare analysis data to check progress
  * Check if the goals have been reached 
  * Update the results onto the tracker
  
> Change starts with awareness
  
   A simple no-nonsense habit tracker track habits onto an Excel worksheet and perform calculations on the data to inspect the progress.

 FILENAME | DESCRIPTION 
  :---:|--- 
[__Habit Tracker Template__](Excel__Files/Habit%20Tracker-10_7.xlsx)| Habit tracker Excel file tracked from Aug 10 till Oct 7
[__Habit Tracker\(Example file used\)__](Excel__Files/Habit%20Tracker-Template.xlsx)| Habit tracker Excel file template
[__Habit Goals file__](Modules/HabitGoalsFile.py)| A dictionary. Format: {keyA : {keyB : Values}, ...} KeyA= Habit Names, KeyB= 'Goals', Values= Goals got as input.    
[__Habit List File__](Modules/HabitListFile.py)| A list. Elements=Habit names. Created by parsing the habit(second) column of the Excel sheet. 
[__Habit Functions__](Modules/HabitTrackerFunctions.py)| Functions that are called by the main program and the functions that are used within the program to simplify the code.
[__Datetime module of Python 3.8__](Datetime38.py)| Datetime module of python 3.8 imported to use the attribute fromisocalendar since the IDE had its limit to python 3.6.
[__Requirements File__](Requirements%20File/HabitTracker-Requirements.txt)| Modules to be installed.
 __README.md__ | Document being read.
[ \___main\_\_.py__](__main__.py)| Main program to run the application.
