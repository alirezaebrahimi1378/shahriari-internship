>## **Description:**

This code is designed to process a CSV file containing students information, including name, age, nationality, city, math scores, and other scores. It calculates the average score for each student and provides insightful statistics based on the data.


>## **Read_csv function**

The **read_csv** provides functionality to read student data from a CSV file. 

- **How the function works**:

    - Opens a CSV file with the given filename.
    - Reads the contents using Python's built-in csv module.
    - Saves the header and main data separately.
    - Converts age and score columns (4, 5, 6, 7, and 8) from strings to floats to facilitate numerical operations.
    
    Example:
    ````python
    dir = os.path.dirname(__file__)
    path = os.path.join(current_directory, "..", "data", "student-dataset.csv") 
    data = read_csv(path)
    ````

>## **class Dataset**

The **Dataset** class is responsible for managing and processing student score data. It provides methods to calculate average scores, informations and showing the best three students in average and lowest average and calcualte the average of grades.
    
**Methods**

1. **__init__**
    (self, data)

    Initialize **Dataset** object.

    - **parameters**:
        - `data` (list): A list of students data


2. **average_data**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - This method calculate average scores of each student and appends this average to their data entry.

        Returns: Returns a modified list of student's data with their average scores. If a student has no score, it prints a message and returns **0**


3. **information**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - This method Compiles a dictionary that the key is student's average score and the values of each key are the lists containing name, nationality, age.

        Returns: A dictionary the key = student's name and value = [name, nationality, age].


4. **get_sorted_data**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to

    - **How the function works**:

        - This method Creates a new list data2, where each entry is a tuple of the student's name and average score.
        Sorts this list using the average scores as the key.

         Returns: A list of tuples containing student names and their average scores, sorted in ascending order based on average scores.


5. **Top_three_grades**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to.
    
    - **How the function works**:

        - This method Retrieves the sorted data using the **self.sorted_data** that is the output of **get_sorted_data()** and prints the top three students with the highest average scores.

        Returns: Print The top three averages with names.


6. **last_three_grades**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to.
    
    - **How the function works**:

        - This method Retrieves the sorted data using the **self.sorted_data** that is the output of **get_sorted_data()** and prints the lowest three averages.

        Returns: Print The lowest three averages without names.


7. **average_grades**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - This method calculate the overall averages of students' average score based on  **self.sorted_data** that is the output of **get_sorted_data()**.

        Returns: Print the overall average.


8. **main**

    - **Parameters**:
        This method does not take any parameters directly but relies on the class attributes.


    - **How the function works**:

        The main method serves as the entry point for the program. it includes getting data, calculating the average, create dictionary based on the average, sort data based on the average, show the highest 3 averages and lowest and finally calcualte the overall average.

        Destail Steps:

        1. **calculate average**:
            
            - calls the **average_data** method and then display the calculated data.

        2. **Display information dictionary**:

            - calls **information** method that gave the output of **average_data** and then display the dictionary which key average and the value of each key is [name, nationality, age].

        3. **Display sorted data**:

            - calls **get_sorted_data** method that sort data by average ascending then show the name and averages in tuple

        4. **Display Top three grades**:

            - calls **Top_three_grades** method to display the three highest grades with the name.

        5. **Display last three grades**:

            - calls **last_three_grades** method to display three lowest grades.

        6. **Calculates Average Grades**:

            - callls the **average_grades** method that calcualtes the overall average.

            Example:
            ````python
            process = Dataset(data)
            process.main()
            ````

## **Usage**

To run the code:
- Make sure to provide the correct path as the filepath.



        
