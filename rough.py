import pandas as pd
from datetime import datetime as dt
from date_methods import day_number_dict
import re

df = pd.read_csv("datasets\habits_2021_test - Copy.csv")

# d = "2021-W1"
# r = dt.strptime(d + '-2', "%Y-W%W-%w")
date_regex = re.compile("[0-9]{0,2}-[0-9]{0,2}-[0-9]{0,4}")
habits_list = list(df['habits'])
habits_list = [i for i in habits_list if i != ""]

class Habit:
    def __init__(self, name) -> None:
        self.name = name
        self.done = self.get_habit_results()
    
    def get_habit_results(self):
        done = {}
        habit_index = habits_list.index(self.name)
        first_row = list(df.iloc[0:0])
        dates_list = [i for i in first_row if re.search(date_regex, i)]
        for date in dates_list:
            habit_result = df[date][habit_index]
            done[date] = habit_result
        return done

habit_object_list = [Habit(h) for h in habits_list]
for i in habit_object_list:
    print(i.name, i.done)
