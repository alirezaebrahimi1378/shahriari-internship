# necessary packages
import csv
import os

# function for loading csv data
def read_csv(filename):
    '''
    reading csv file and save the data except header into the list 
    '''
    with open(filename, "r") as file:
        reader = csv.reader(file)

        # save data as list
        data = list(reader)
        header = data[0]
        # extract main data (except header)
        main_data = data[1:]

        '''
        convert the column of math.grade and other grades from str to int
        
        Returns: 
        list
        '''
        for row in main_data:
            for j in [4, 5, 6, 7, 8]:
                row[j] = float(row[j])
        return main_data


class Score:
    '''
    a class that calculate average of grade and sorting data based on average and ...
    '''
    def average(self, score):
        '''
        this method get the list of data and calculate the average for each person

        Returns: the new list that include average.
        '''
        self.score = score
        try:
            for row in range(len(self.score)):
                mean = sum(self.score[row][5:]) / len(self.score[row][5:])
                mean_round = round(mean, 2)
                self.score[row].append(mean_round)
            return self.score
        except ZeroDivisionError:
            print("there is no lesson ")
            return 0
    
    # show name, country, age and average
    def information(self, data):
        '''
        this method give the list and create dictionary based on average

        Returns: the dictionary with key of average and value of that is a list 
        include name, country, age of each person.
        '''
        self.data = data
        dic = {}
        for i in range(len(self.data)):
            key = self.data[i][-1]
            dic[key] = [self.data[i][1], self.data[i][2], self.data[i][4]]
        return dic
      
    # # # create tuple (name, average)
    def get_sorted_data(self, data):
        '''
        this method sort data based the average

        Returns: a list of sorted data that argument1 is name and argument2 is the average
        '''
        self.data = data
        data2 = []
        for item in range(len(self.data)):
            data2.append((self.data[item][1], self.data[item][-1]))
        # sort data based on average
        data2.sort(key=lambda x: x[1])
        return data2
    
    # # print Top 3 of the list
    def Top_three(self,data):
        '''
        this method get the sorted data and print top three averages with name

        '''
        self.data = data
        print("Top 3 Entries: ")
        for name , score in self.data[-3:]:
            print(f"Name: {name}, score: {score}")

    # # # print last 3 student
    def last_three(self, data):
        '''
        this method get the sorted data and print the lowest three averages without name
        '''
        self.data= data
        print("The three lowest averages")
        for item in self.data[:3]:
            print(item[1])

    def average_grades(self, data):
        '''
        this method calculate the average of list

        Returns: the average of whole class
        '''
        self.data = data
        average = sum([row[1] for row in self.data])/ len(self.data)
        print(f"the average of grades is {round(average, 2)}")
        

# # load data
# Get the directory of the script (where main.py is located)
current_directory = os.path.dirname(__file__)  

# Create the relative path to student.csv
relative_filepath = os.path.join(current_directory, "..", "data", "student-dataset.csv") 

# Read the CSV data
data = read_csv(relative_filepath)

# calculate average
average_score = Score()
total_data = average_score.average(data)

# # sorting data based on average
sorter_score = average_score.get_sorted_data(total_data)
print(sorter_score)

# # # # print the top_three
average_score.Top_three(sorter_score)

# # # # print The three lowest averages
average_score.last_three(sorter_score)

# # # # print the average of grade
average_score.average_grades(sorter_score)

# # # # for the last part
last_part = average_score.information(total_data)
print(last_part)