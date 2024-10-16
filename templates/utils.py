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

def calculate_percentage_increase(data, value_col, baseline_col):
    """Calculate the percentage increase based on the value and baseline columns."""
    return (data[value_col] / data[baseline_col]) * 100

def create_combined_score(data, weights, *cols):
    """Create a combined score based on specified columns and their weights."""
    return sum(data[col] * weight for col, weight in zip(cols, weights))

def calculate_thresholds(data, column):
    """Calculate the top and next 25% thresholds for a specified column."""
    min_value = data[column].min()
    max_value = data[column].max()
    top_25_threshold = min_value + (max_value - min_value) * 0.75
    next_25_threshold = min_value + (max_value - min_value) * 0.50
    return top_25_threshold, next_25_threshold

def get_percentile_counties(data, column, lower_threshold, higher_threshold = None, is_top=True):
    """Retrieve counties that fall within the specified threshold."""
    if is_top:
        return data.loc[data[column] >= lower_threshold, 'County']
    else:
        return data.loc[(data[column] < lower_threshold) & (data[column] >= higher_threshold), 'County']

def summarize_grouped_data(grouped_data):
    """Summarize the grouped data for total schools, students, and grade levels."""
    return grouped_data.agg({
        'Number of Schools': 'sum',
        'Student Enrollment ': 'sum',
        'Grade Levels': 'sum'
    })

def analyze_data(data, simplified_table, value_col, baseline_col, data_type):
    """Process the data to calculate increases and summarize results for either precipitation or storm events."""
    
    # Calculate percentage increases
    data[f'% of increase ({data_type})'] = calculate_percentage_increase(data, value_col, baseline_col)

    # Create combined scores
    weights = [0.33, 0.33, 0.33]  # Equal weights for title one, % increase, % Unduplicated
    data['combo'] = create_combined_score(data, weights, 'title one', f'% of increase ({data_type})', '% Unduplicated ')

    # Calculate thresholds
    top_25_threshold, next_25_threshold = calculate_thresholds(data, 'combo')
    top_25_percent = get_percentile_counties(data, 'combo', top_25_threshold, is_top=True)
    next_25_percent = get_percentile_counties(data, 'combo', top_25_threshold, next_25_threshold, is_top=False)

    # Group by county and summarize
    simplified_table = simplified_table.rename({'County Name': 'County'}, axis='columns')
    grouped_tab = simplified_table.groupby('County').agg({
        'Number of Schools': 'sum',
        'Student Enrollment ': 'sum',
        'Grade Levels': 'count',
    }).reset_index()

    # Summarize top 25% and next 25%
    g_top_25 = grouped_tab.loc[grouped_tab['County'].isin(top_25_percent)]
    g_next_25 = grouped_tab.loc[grouped_tab['County'].isin(next_25_percent)]

    top_25_summary = summarize_grouped_data(g_top_25)
    next_25_summary = summarize_grouped_data(g_next_25)

    # Print summaries
    print(f"Number of counties in the top 25%: {len(top_25_percent)}")
    print(top_25_summary)

    print(f"Number of counties in the next 25%: {len(next_25_percent)}")
    print(next_25_summary)

    # Overall totals
    total_schools = top_25_summary['Number of Schools'] + next_25_summary['Number of Schools']
    total_students = top_25_summary['Student Enrollment '] + next_25_summary['Student Enrollment ']
    total_districts = top_25_summary['Grade Levels'] + next_25_summary['Grade Levels']

    print('Num schools: ', total_schools)
    print('Students: ', total_students)
    print('Num districts: ', total_districts)
