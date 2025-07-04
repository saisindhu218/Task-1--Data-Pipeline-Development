
# TASK-1--DATA-PIPELINE-DEVELOPMENT

*Company*   : CODTECH IT SOLUTIONS

*Name*      : Rachabattuni Sai Sindhu

*Intern ID* : CT06DG1263

*Domain*    : Data Science

*Duration*  : 6 Weeks

*Mentor*    : Neela Santosh

Hey there! This repository is part of my journey through the CODTECH Data Science Internship, and it's all about **Task 1: Data Pipeline Development**. As an MCA student diving deeper into data science, this task gave me a great opportunity to experience what it’s really like to work with raw data and transform it into something structured, clean, and ready to be used for analysis. The task focused on building an ETL pipeline. In simple terms, I had to take in raw data (with errors and inconsistencies), clean and reshape it, and export the final version. I used a simulated student dataset as the working base, and I ran everything inside a custom virtual environment named Datascience_env to manage dependencies cleanly.I used VS Code as my code editor for this task, it made writing, testing, and organizing code much easier with its extensions and integrated terminal.

## Project Workflow
#### 1. Created a Sample Dataset
To begin, I manually created a synthetic dataset named student_data.csv with fields like:
* StudentName
* StudentID
* PhoneNumber
* MCADepartment
* College
* GPA
To mimic real-world data, I intentionally added missing values in columns like StudentID, PhoneNumber, and GPA, and also introduced some duplicate rows.

#### 2. Data Cleaning
The next step was to clean the dataset. Here’s how I tackled it:
* **Removed duplicate entries** so every student record is unique.
* **Imputed missing values** based on the type of data:
  * StudentID and GPA were filled using their column mean.
  * PhoneNumber was filled with 0 and then converted into integers for consistency.
  * MCADepartment was filled using the most frequent department value found in the data.
This step helped ensure that the dataset had no null or misleading values.

#### 3. Data Transformation
Once the data was cleaned, I worked on transforming it for readability and usability:
* I rounded GPA values to two decimal places after imputation for clarity and neatness.
* I kept department names like "General", "SCT", "ISMS", "AIML" as they were not encoded to retain human readability.
* I **renamed columns** for simplicity:
  * StudentName to name
  * StudentID to id
  * PhoneNumber to phone number
  * MCADepartment to department
  * GPA to grade
* I also **reordered the columns** for better organization and logical flow.

#### 4️. Data Export
Finally, I exported the clean and processed data into a new file called **processed student data.csv**. This file represents the polished version of the original student_data.csv now cleaned, transformed, and ready for analysis or integration into future projects.

## Tools and Technologies Used
* **Python**:My main programming language throughout the project.
* **Pandas**:Super useful for data manipulation and working with CSV files.
* **NumPy**:Helped me handle numerical operations and `NaN` values.
* **Scikit-learn**:I used SimpleImputer for imputing missing values and ColumnTransformer to apply different transformations.
* **VS Code**:My go to code editor. It really helped with managing files, running Python scripts, and organizing everything through its extensions.
* **Datascience_env**:A virtual environment I created to isolate my dependencies and keep the project clean.

## What I Learned
This task was a major confidence booster. As an MCA student who’s still learning the practical side of data science, I gained a lot from this experience. Here are some things I personally learned:
* **Handling messy data is unavoidable**, but with the right tools, it becomes manageable. I now understand the importance of cleaning data before doing any kind of analysis.
* **Different data types need different treatment**. For example, IDs shouldn’t be scaled like numerical values, and missing categories can’t just be guessed they need a smart strategy like filling with the mode.
* I learned how to **design data pipelines step-by-step**, which is super useful for real-world projects.
* I now feel more confident using **pandas**, **NumPy**, and **scikit-learn** for data processing.
* I also realized the **value of virtual environments** like Datascience_env in keeping dependencies clean and avoiding project conflicts.
* Finally, working in **VS Code** made the development process smooth and well-organized.

## Conclusion
Completing this task gave me a strong foundation in understanding how raw data is handled in real-world data science workflows. I now realize that before we can perform any kind of meaningful analysis, data must be cleaned, structured, and reliable. Building the ETL pipeline from scratch — right from creating messy data to exporting a clean, well-organized dataset — gave me practical experience in every essential step of data preprocessing.
As a beginner, this hands-on task showed me that data wrangling is not just a technical step, but a critical thinking process that requires understanding the data, the problem context, and how to prepare it for analysis or modeling. This task also taught me how to work with Python libraries like pandas, NumPy, and scikit-learn in a structured and efficient way, and I now feel much more confident tackling similar tasks in future projects.
Overall, this was an enriching experience that made me appreciate how important clean data is to every data science solution, and how even basic tasks like imputing missing values or renaming columns contribute to the success of a project. It has definitely set the stage for me to take on more complex challenges in this field with confidence.


Result of Task Complition:

Finally adter ETL Process the data is shown in csv file

![Image](https://github.com/user-attachments/assets/3f833811-eeab-4329-9edd-9572ac20d30f)



This is the trminal view after compilation

![Image](https://github.com/user-attachments/assets/f16ebfb5-e0e9-4378-ba73-256ea5b2f3df)


