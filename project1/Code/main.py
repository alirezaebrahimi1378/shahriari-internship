# Importing utility functions: `read_csv` to load data from CSV, and `Score` class to calculate average scores
from Utils import *

# load data
filepath = "D:/work/mahbod/project1/shariari-internship/data/student-dataset.csv"
data = read_csv(filepath)

# calculate average
average_score = Score(data)
data = average_score.average()

# # sorting data based on average
sorter = Sort(data)
sorter_score = sorter.get_sorted_data()

# # print the top_three
sorter.Top_three()

# # print The three lowest averages
sorter.last_three()

# # print the average of grade
sorter.average_grades()

# for the last part
last_part = average_score.information()
print(last_part)