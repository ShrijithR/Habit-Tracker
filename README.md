# **Habit-Tracker**

![Image of HT](https://media.giphy.com/media/Zr9FfobRExF6FuRsJr/giphy.gif)    

> Change starts with awareness.
  
## Description
 What is it?  
 _A simple, no-nonsense habit tracker to track habits onto an Excel worksheet and perform calculations on the data to inspect progress._  
 What does it do?    
  _For a specific habit or all habits; For a specific date/date range or date ranges:_  
  * _Analyse total number of hits and misses._  
  * _Compare analysis data to check progress._  
  * _Check if the goals have been reached._  
  * _Update the results of the day onto the tracker._  
  
## Table Of Contents
 FILENAME | DESCRIPTION 
  :---:|--- 
[__Requirements File__](docs/HabitTracker-Requirements.txt)| Modules to be installed.
[\_\___main\_\_.py__](__main__.py)| Main program to run the application.
[__Habit Tracker Template__](docs/Habit%20Tracker-10_7.xlsx)| Tracker file, from Aug 10 till Oct 7.
[__Habit Tracker\(Example file used\)__](docs/Habit%20Tracker-Template.xlsx)| Tracker file template.
[__Habit Goals file__](src/HabitGoalsFile.py)| A dictionary in the format 'Dict:{keyA :{keyB :Values}, ...}' where KeyA= Habit Names, KeyB= 'Goals', and Values= Return values from the function, UpdateGoals. 
[__Habit List File__](src/HabitListFile.py)| A list having its elements as habit names created by parsing the habit(second) column of the active sheet. 
[__Habit Functions__](src/HabitTrackerMainFunctions.py)| Module containing the functions used by the main program and the functions used to simplify the code within the module itself. 
[__Datetime module of Python 3.8__](src/Datetime38.py)| Datetime module of python 3.8 imported to use the attribute 'fromisocalendar' since the IDE has its limit to python 3.6.
 __README.md__ | Document being read.
[__Notes.md__](docs/Notes.md)| Information on the working of the program.  

## Installation
* Install the modules in the HabitTracker-Requirements.txt file using pip.
* Follow the format in the Tracker template to edit the Excel accordingly.
* Keep all the files in the same folder. 
* Open \_\_main.py\_\_ to run the program. 
* Check [notes](docs/Notes.md) for more information on the working. 

### Good Luck!
