# This is your Python script for student data
# It uses a custom simulated dataset, handles cleaning/transformation, and
# ensures specific output column names, including Student Name and Phone Number,
# with actual Department Names, not numerical encodings.
# StudentID is an integer and is not scaled.
# Phone numbers' missing values are handled by replacing with '0'.
# StudentID and GPA's missing values are handled via mean imputation.


# ---Part 1: Setup and Loading Data & Global Configuration---
# 1. Import necessary tools (libraries)
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import random

print("Hello! Starting our data pipeline for Task 1 with your custom student dataset..")
print("----------------------------------------------------------------------")

# Define global configuration variables for columns
target_column = 'GPA'
# These are columns that we want to keep in the final output, but not necessarily transform
# or use as direct features for ML models (e.g., identifiers, constant values).
columns_to_retain_identifiers = ['StudentName', 'PhoneNumber', 'College']

# 2. Create our custom simulated dataset with 50 students and specific department counts
num_students = 50
# List of common names to pick from
names = [
    "Rahul", "Priya", "Amit", "Sneha", "Vikram", "Anjali", "Saurabh", "Divya",
    "Arjun", "Kavya", "Mohit", "Nisha", "Rohan", "Shruti", "Gaurav", "Pooja",
    "Deepak", "Aisha", "Vishal", "Meena", "Sameer", "Rekha", "Tarun", "Shweta",
    "Anil", "Geeta", "Manish", "Sunita", "Rajesh", "Seema", "Alok", "Madhu",
    "Sanjay", "Uma", "Vikas", "Rita", "Navin", "Preeti", "Kunal", "Swati",
    "Bharat", "Arti", "Jatin", "Megha", "Kapil", "Neha", "Dhruv", "Radha",
    "Pranav", "Supriya", "Vimal", "Sarita", "Ajay", "Chandana", "Harish", "Smita",
    "Pramod", "Kiran", "Nitin", "Lata", "Yogesh", "Jyoti", "Ashish", "Pinky"
]
student_names = random.choices(names, k=num_students)

# Generate Student IDs without duplicates or NaNs initially
student_ids = list(range(1, num_students + 1)) 
# IDs from 1 to 50, unique and consecutive

phone_numbers = [f"98765{np.random.randint(10000, 99999)}" for _ in range(num_students)]
missing_phone_indices = np.random.choice(num_students, 5, replace=False)
for idx in missing_phone_indices:
    phone_numbers[idx] = np.nan # Introduce NaNs for phone numbers

# Generating MCADepartment with fixed order directly
mca_specializations_fixed_order = []
mca_specializations_fixed_order.extend(['General'] * 15) # First 15 students
mca_specializations_fixed_order.extend(['SCT'] * 10)     # Next 10 students
mca_specializations_fixed_order.extend(['ISMS'] * 10)     # Next 10 students
mca_specializations_fixed_order.extend(['AIML'] * 15)     # Last 15 students

gpa_scores = np.round(np.random.uniform(2.5, 4.0, num_students), 2).tolist()
# MODIFIED: Introduce some Nones into GPA scores for demonstration of imputation
missing_gpa_indices = np.random.choice(num_students, 3, replace=False)
for idx in missing_gpa_indices:
    gpa_scores[idx] = np.nan


# Create the DataFrame with adjusted columns
data = {
    'StudentName': student_names,
    'StudentID': student_ids,
    'PhoneNumber': phone_numbers,
    'MCADepartment': mca_specializations_fixed_order, 
    'College': ['Jain'] * num_students,
    'GPA': gpa_scores
}
my_data_table = pd.DataFrame(data)

# NOTE: We still add one duplicate row *after* initial creation for demonstration
# of the drop_duplicates step, as it's a common data cleaning task.
duplicate_row_index = np.random.randint(0, num_students)
my_data_table = pd.concat([my_data_table, my_data_table.iloc[[duplicate_row_index]]], ignore_index=True)

# 3. Look at the first few rows of our data
print("\n--- Here's what our ORIGINAL custom data looks like (first 10 rows) ---")
print(my_data_table.head(10))

# 4. Get a quick summary of our data's structure
print("\n--- Summary of our ORIGINAL custom data (info()) ---")
my_data_table.info()

# 5. Check for any missing values (empty cells)
print("\n--- Missing values BEFORE handling ---")
print(my_data_table.isnull().sum())

# 6. Check for duplicate rows
print("\n--- Number of duplicate rows found BEFORE handling ---")
print(f"There are {my_data_table.duplicated().sum()} duplicate rows.")

print("\n--- Data Loading and Initial Check Finished! ---")
print("----------------------------------------------------------------------")



# --- Part 2: Data Cleaning (Preprocessing) ---
print("\n--- Starting Data Cleaning ---")

# 1. Handle Duplicate Rows
rows_before_duplicates = my_data_table.shape[0]
my_data_table.drop_duplicates(inplace=True)
rows_after_duplicates = my_data_table.shape[0]
print(f"Removed {rows_before_duplicates - rows_after_duplicates} duplicate rows.")
print("\n--- Data After Removing Duplicates (first 10 rows) ---")
print(my_data_table.head(10))

# 2. Handle Missing Values
print("\n--- Handling Missing Values ---")

# Include GPA in numerical_cols_for_imputation
numerical_cols_for_imputation = ['StudentID', 'GPA']
for col in numerical_cols_for_imputation:
    my_data_table[col] = pd.to_numeric(my_data_table[col], errors='coerce')
num_imputer = SimpleImputer(strategy='mean')
my_data_table[numerical_cols_for_imputation] = num_imputer.fit_transform(my_data_table[numerical_cols_for_imputation])

# Convert StudentID to int after imputation (GPA can remain float as it's a score)
my_data_table['StudentID'] = my_data_table['StudentID'].astype(int)
print("Converted 'StudentID' column to integer type.")

# *** NEW FIX: Round GPA to 2 decimal places after imputation ***
my_data_table['GPA'] = my_data_table['GPA'].round(2)
print("Rounded 'GPA' column to 2 decimal places after imputation.")

categorical_cols_for_imputation = ['MCADepartment']
cat_imputer = SimpleImputer(strategy='most_frequent')
my_data_table[categorical_cols_for_imputation] = cat_imputer.fit_transform(my_data_table[categorical_cols_for_imputation])

# Handle missing 'PhoneNumber' by replacing with 0 and converting to int
my_data_table['PhoneNumber'] = pd.to_numeric(my_data_table['PhoneNumber'], errors='coerce')
my_data_table['PhoneNumber'].fillna(0, inplace=True)
my_data_table['PhoneNumber'] = my_data_table['PhoneNumber'].astype(int)
print("Handled missing 'PhoneNumber' values by replacing with '0' and converting to integer.")

# This will show 0 for all columns, confirming no NaNs
print("\n--- Missing values AFTER handling (should all be 0 now) ---")
print(my_data_table.isnull().sum()) 

print("\n--- Data Cleaning Finished! ---")
print("----------------------------------------------------------------------")



# --- Part 3: Data Transformation ---
print("\n--- Starting Data Transformation ---")

# Label Encoding is now optional, not for the final output column
label_encoder = LabelEncoder()
print("\n--- Label Encoding for 'MCADepartment' (if needed for ML) mapping: ---")
label_encoder.fit(my_data_table['MCADepartment']) # Fit the encoder to get the classes
for i, name in enumerate(label_encoder.classes_):
    print(f"  {name}: {i}")
print("Note: The numerical encoding is shown above, but the output CSV will have names directly.")

numerical_features_to_scale = [] # StudentID is not scaled

# Define columns to pass through. This explicitly lists all columns that should NOT be scaled.
# We want to keep 'MCADepartment' as is.
features_to_passthrough = [col for col in my_data_table.columns if col not in numerical_features_to_scale + [target_column]]

preprocessor = ColumnTransformer(
    transformers=[
        # No numerical features to scale here
    ],
    remainder='passthrough' # This will pass through ALL columns if no transformers are defined for them
)

# Apply the transformations to the entire my_data_table
transformed_array_with_remainder = preprocessor.fit_transform(my_data_table)
# Reconstruct the DataFrame after transformation
original_columns_in_df = my_data_table.columns.tolist()

scaled_cols_in_output = []
passthrough_cols_in_output = original_columns_in_df

ordered_output_columns = scaled_cols_in_output + passthrough_cols_in_output

processed_data_transformed_df = pd.DataFrame(transformed_array_with_remainder,
                                     columns=ordered_output_columns)

# Separate features from target (GPA) after transformation
processed_features_df = processed_data_transformed_df.drop(columns=[target_column])
target_y = processed_data_transformed_df[target_column]

print("\n--- First few rows of our PROCESSED Features ---")
print(processed_features_df.head())

print("\n--- Data Transformation Finished! ---")
print("----------------------------------------------------------------------")



# --- Part 4: Data Loading (Saving the Processed Data) ---
print("\n--- Starting Data Loading (Saving) ---")

# 1. Combine the processed features and the target (y) back into one clean table.
final_processed_data = pd.concat([processed_features_df, target_y.reset_index(drop=True)], axis=1)

# 2. Rename columns as requested for the final output CSV
rename_mapping = {
    'StudentName': 'name',
    'StudentID': 'id',
    'PhoneNumber': 'phone number',
    'MCADepartment': 'department',
    'GPA': 'grade'
}
final_processed_data.rename(columns=rename_mapping, inplace=True)

# Reorder columns to match your desired output sequence
final_column_order = [
    'name', 'id', 'phone number', 'department', 'College', 'grade'
]
# Ensure all columns exist before reordering to prevent errors and filter out any accidental extras
final_column_order = [col for col in final_column_order if col in final_processed_data.columns]
final_processed_data = final_processed_data[final_column_order]

# 3. Define the name for your new, clean data file.
output_filename = 'processed student data.csv'

# 4. Save the final clean data table to a new CSV file.
final_processed_data.to_csv(output_filename, index=False)

print(f"\n--- Data Pipeline COMPLETE! ---")
print(f"Your cleaned and transformed data is saved to: E:\\intproject\\{output_filename}")
print("\n--- Here's what your final processed data looks like (first 5 rows) ---")
print(final_processed_data.head())
print("----------------------------------------------------------------------")