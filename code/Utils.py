# necessary packages
import csv

# load csv data
def read_csv(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)

        # save data as list
        data = list(reader)
        header = data[0]
        main_data = data[1:]

        # convert str to int for column 4:
        for row in main_data:
            for j in [4, 5, 6, 7, 8]:
                row[j] = float(row[j])
        return main_data


# calculate the average
class Score:
    def __init__(self, score):
        self.score = score

    # calculate the average score
    def average(self):
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
    def information(self):
        data = self.score
        dic = {}
        for i in range(len(data)):
            key = data[i][-1]
            dic[key] = [data[i][1], data[i][2], data[i][4]]
        return dic
    
 
# sorting data
class Sort:
    def __init__(self,data):
        self.data = data
        
    # # create tuple (name, average)
    def get_sorted_data(self):
        data2 = []
        for item in range(len(self.data)):
            data2.append((self.data[item][1], self.data[item][-1]))
        # sort data based on average
        data2.sort(key=lambda x: x[1])
        return data2
    
    # print Top 3 of the list
    def Top_three(self):
        sorted_data = self.get_sorted_data()
        print("Top 3 Entries: ")
        for name , score in sorted_data[-3:]:
            print(f"Name: {name}, score: {score}")

    # print last 3 student
    def last_three(self):
        sorted_data = self.get_sorted_data()
        print("The three lowest averages")
        for item in sorted_data[:3]:
            print(item[1])

    def average_grades(self):
        data = self.get_sorted_data()
        average = sum([row[1] for row in data])/ len(data)
        print(f"the average of grades is {round(average, 2)}")
        

    




