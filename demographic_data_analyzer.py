import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races_list = df["race"].tolist()
    races_dict = {}

    for race in races_list:
      races_dict[race] = races_dict.get(race, 0) + 1

    race_count = pd.Series(races_dict)

    # What is the average age of men?
    age_data = df["age"][df["sex"] == "Male"]
    average_age_men = round(age_data.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    education_data = df[df["education"] == "Bachelors"]
    percentage_bachelors = round((len(education_data) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate")]
    high_education_length = len(higher_education)

    lower_education = df[(df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")]
    lower_education_length = len(lower_education)

    # percentage with salary >50K
    higher_education_rich_length = len(higher_education[higher_education["salary"] == ">50K"])
    higher_education_rich = round((higher_education_rich_length / high_education_length) * 100, 1)

    lower_education_rich_length = len(lower_education[lower_education["salary"] == ">50K"])
    lower_education_rich = round((lower_education_rich_length / lower_education_length) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours_data = df["hours-per-week"].min()
    min_work_hours = min_work_hours_data

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    num_min_workers = len(df[df["hours-per-week"] == 1])
    num_rich_min_workers = len(df[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")])
    rich_percentage = (num_rich_min_workers / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    countries = df["native-country"].values.tolist()
    countries_rich = df["native-country"][df["salary"] == ">50K"].values.tolist()
    countries_dict = {}
    countries_rich_dict = {}
    countries_rich_percentage_dict = {}

    # get all country list
    for country in countries:
        countries_dict[country] = countries_dict.get(country, 0) + 1

    # filter rich country
    for country_rich in countries_rich:
        countries_rich_dict[country_rich] = countries_rich_dict.get(country_rich, 0) + 1

    # loop to calculate percentage
    for key, value in countries_dict.items():
      if key in countries_rich_dict:
        percentage = (countries_rich_dict[key] / value) * 100
        countries_rich_percentage_dict[key] = countries_rich_percentage_dict.get(key, percentage)

    # get get the highest country name and percentage
    highest_earning_country = max(countries_rich_percentage_dict, key=countries_rich_percentage_dict.get)
    highest_earning_country_percentage = round(pd.Series(countries_rich_percentage_dict).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation_list = df["occupation"][(df["native-country"] == "India") & (df["salary"] == ">50K")].tolist()
    top_IN_occupation_dict = {}

    for occupation in top_IN_occupation_list:
      top_IN_occupation_dict[occupation] = top_IN_occupation_dict.get(occupation, 0) + 1
    
    top_IN_occupation = max(top_IN_occupation_dict, key=top_IN_occupation_dict.get)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
