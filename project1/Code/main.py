# necessary packages
import csv
import os

'''
Here is a code  that reads a CSV file with columns for name, age, nationality, city, and scores, 
calculates each person's average score, sorts them in ascending order based on the average
and then displays the top three and last three averages and print the name, age, nationality for each averages.
'''

# function for loading csv data
def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)

        # save data as list
        data = list(reader)
        header = data[0]
        # extract main data (except header)
        main_data = data[1:]

        for row in main_data:
            for j in [4, 5, 6, 7, 8]:
                row[j] = float(row[j])
        return main_data


class Dataset:
    def __init__ (self,data):
        self.data = data
    def average_data(self):
        try:
            for row in range(len(self.data)):
                mean = sum(self.data[row][5:]) / len(self.data[row][5:])
                mean_round = round(mean, 2)
                self.data[row].append(mean_round)
            return self.data
        except ZeroDivisionError:
            print("there is no lesson ")
            return 0
    
    # show name, country, age and average
    def information(self):
        dic = {}
        for i in range(len(self.data)):
            key = self.data[i][-1]
            dic[key] = [self.data[i][1], self.data[i][2], self.data[i][4]]
        return dic
      
    # # # create tuple (name, average) and sort the data based on average
    def get_sorted_data(self):
        data2 = []
        for item in range(len(self.data)):
            data2.append((self.data[item][1], self.data[item][-1]))
        # sort data based on average
        data2.sort(key=lambda x: x[1])
        self.sorted_data = data2
        return data2
    
    # # print Top 3 of the grade's list
    def Top_three_grades(self):
        print("Top 3 Entries: ")
        for name , score in self.sorted_data[-3:]:
            print(f"Name: {name}, score: {score}")

    # # # print last 3 student in grades
    def last_three_grades(self):
        print("The three lowest averages")
        for item in self.sorted_data[:3]:
            print(item[1])
    
    # # # print the averages of grade
    def average_grades(self):
        average = sum([row[1] for row in self.sorted_data])/ len(self.sorted_data)
        print(f"the average of grades is {round(average, 2)}")

    def main(self):
        total_data =self.average_data()
        print(total_data) 
        information = self.information()
        print(information)
        sorted_data = self.get_sorted_data()
        print(sorted_data)
        self.Top_three_grades()
        self.last_three_grades()
        self.average_grades()
    

# # load data
# Get the directory of the script (where main.py is located)
current_directory = os.path.dirname(__file__)  

# Create the relative path to student.csv
relative_filepath = os.path.join(current_directory, "..", "data", "student-dataset.csv") 

# Read the CSV data
data = read_csv(relative_filepath)

# call Class 
process = Dataset(data)
process.main()
