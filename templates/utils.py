import pandas as pd
import numpy as np

def int_fixer(column):
    """Converts a column of strings with commas to integers."""
    return column.str.replace(',', '').astype(int)

def percent_fixer(column):
    """Converts a column of percentage strings to floats by removing '%' and '*' characters."""
    column = column.str.replace('%', '0')
    column = column.str.replace('*', '0')
    return column.astype(float)

def master_update(df, col, func):
    """Applies a function to a specified column in the DataFrame and updates it."""
    df[col] = func(df[col])
    return df

def divide_district(value):
    """Calculates the percentage of a given value relative to 936 and formats it as a string."""
    return f"{round((value / 936) * 100, 1)}%"

def divide_county(value):
    """Calculates the percentage of a given value relative to 58 and formats it as a string."""
    return f"{round((value / 58) * 100, 1)}%"

def analyze(master, respective_cols, years, thresholds, data_focus, district_or_county):
    """Analyzes the master DataFrame for the number of districts/counties exceeding specified thresholds over given years."""
    avg_data = []

    for i, col in enumerate(respective_cols):
        col_data = []
        for threshold in thresholds:
            num_districts = master[master.iloc[:, col] > threshold].shape[0]
            print(f"{num_districts} {district_or_county} are expected to experience at least {threshold} days over {data_focus} by {years[i]}.")
            col_data.append(num_districts)
        avg_data.append(col_data)

    avg_data = np.array(avg_data)  # Transpose to align with the DataFrame format
    
    df = pd.DataFrame({
        f'{data_focus}({district_or_county})': [f'{t} days' for t in thresholds],
        '2025': avg_data[0],
        '2035': avg_data[1],
        '2045': avg_data[2],
        '2055': avg_data[3]
    })
    
    return df

def analyze_students_or_school(master, respective_cols, years, thresholds, data_focus, student_or_school):
    """Analyzes student or school data for the number exceeding specified thresholds over given years."""
    avg_data = []

    if student_or_school == "students":
        for i, col in enumerate(respective_cols):
            col_data = []
            for threshold in thresholds:
                students_above_30_days = np.sum(master[master.iloc[:, col] > threshold]["Student Enrollment"])
                print(f"{students_above_30_days} students are expected to experience at least {threshold} days over {data_focus} by {years[i]}.")
                col_data.append(students_above_30_days)
            avg_data.append(col_data)
        avg_data = np.array(avg_data)

        df = pd.DataFrame({
            f'{data_focus}(students)': [f'{t} days' for t in thresholds],
            '2025': avg_data[0],
            '2035': avg_data[1],
            '2045': avg_data[2],
            '2055': avg_data[3]
        })
    else:
        for i, col in enumerate(respective_cols):
            col_data = []
            for threshold in thresholds:
                schools_above_30_days = np.sum(master[master.iloc[:, col] > threshold]["Number of Schools"])
                print(f"{schools_above_30_days} schools are expected to experience at least {threshold} days over {data_focus} by {years[i]}.")
                col_data.append(schools_above_30_days)
            avg_data.append(col_data)
        avg_data = np.array(avg_data)
    
        df = pd.DataFrame({
            f'{data_focus}(schools)': [f'{t} days' for t in thresholds],
            '2025': avg_data[0],
            '2035': avg_data[1],
            '2045': avg_data[2],
            '2055': avg_data[3]
        })
    
    return df
