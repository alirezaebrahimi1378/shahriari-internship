>## **Description:**

This code is designed to process a CSV file containing student information, including name, age, nationality, city, math scores, and other scores. It calculates the average score for each student and provides insightful statistics based on the data.


>## **read_csv function**

The **read_csv** provides functionality to read student data from a CSV file. 

- **How the function works**:

    - Opens a CSV file with the given filename.
    - Reads the contents using Python's built-in csv module.
    - Saves the header and main data separately.
    - Converts age and score columns (4, 5, 6, 7, and 8) from strings to floats to facilitate numerical operations.
    

>## **class Score**

The **Score** class is responsible for managing and processing student score data. It provides methods to calculate average scores and informations.
    
**Methods**

1. **__init__**
    (self, score)

    Initializes the **Score** object with a given list of scores.

    - **parameters**:
        - `score` (list): A list of student data


2. **average**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - This method calculate average score of each student and appends this average to their respective data entry.

        Returns: Returns a modified list of students' data with their average scores. If a student has no score, it prints a message and returns **0**

        Example:
        ```python
        # Example data: [id, name, nationality, city, age, english.grade, other scores...]
        data = [
        [0, "Kiana Lor", "China", "Suzhou", 22, 3.5, 3.7, 3.1, 1],
        [1, "Joshua Lonaker", "United States of America","Santa Clarita", 22, 2.9, 3.2, 3.6, 5]
        ]
        average_score = Score(data)
        data = average_score.average()
        ```


3. **information**

    - **Parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - This method Compiles a dictionary that maps each student's average score to their relevant details (name, nationality, age).

        Returns: A dictionary where the keys are the average scores, and the values are lists containing the corresponding student's name, nationality, and age.

        Example:
        ```python
        student_info = average_score.information()
        ```


>## **class Sort**

The **Sort** class is designed to handle sorting and displaying student score data based on average scores. It provides functionality to retrieve sorted data, as well as to display the top and bottom entries in the dataset.

**Methods**

1. **__init__**
    (self, data)

    Initializes the **Sort** object with a given list of scores.

    - **parameters**:
        - `data` (list): A list of student data

2. **get_sorted_data**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to

    - **How the function works**:

        - This method Creates a new list data2, where each entry is a tuple of the student's name and average score.
        Sorts this list using the average scores as the key.

         Returns: A list of tuples containing student names and their average scores, sorted in ascending order based on average scores.

3. **Top_three**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to.
    
    - **How the function works**:

        - This method Retrieves the sorted data using **get_sorted_data()** and prints the top three students with the highest average scores.

        Returns: Print The top three averages with names.

4. **last_three**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to.
    
    - **How the function works**:

        - This method Retrieves the sorted data using **get_sorted_data** and prints the lowest three averages.

        Returns: Print The lowest three averages without names.

5. **average_grades**

    - **parameters**:
        - `self`: Refers to the instance of the class this method belongs to.

    - **How the function works**:

        - This method calculate the overall averages of students' average score.

        Returns: Print the average

## **Usage**

To run the code:
- Make sure to provide the correct path as the filepath.



        
