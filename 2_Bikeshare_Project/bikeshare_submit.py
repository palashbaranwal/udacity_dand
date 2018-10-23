## TODO: import all necessary packages and functions
import csv
import time
import pandas as pd
import numpy as np
import datetime

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    return city
    # TODO: handle raw input and complete function


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    return time_period
    # TODO: handle raw input and complete function


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    return month

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?\n')
    # TODO: handle raw input and complete function
    return day

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)
    
    month_name=city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))
    
    all_months=city_df.groupby(month_name)['Start Time'].agg(['count'])
    
    popular_month=all_months['count'].idxmax()
    
    return(popular_month)



def popular_day(city_file,time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)
    
    if time_period == 'none':
        
        day_name=city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))
    
        all_days=city_df.groupby(day_name)['Start Time'].agg(['count'])
    
        popular_day=all_days['count'].idxmax()
    
    if time_period == 'month':
        
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]
        
        day_name=period_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))
    
        all_days=city_df.groupby(day_name)['Start Time'].agg(['count'])
        
        popular_day=all_days['count'].idxmax()
    

    return(popular_day)



def popular_hour(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"

    city_df = pd.read_csv(filename)

    if time_period == 'none':

        popular_hour=return_popular_hour(city_df)
    
    if time_period == 'month':

        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]

        popular_hour=return_popular_hour(period_df)

    if time_period == 'day':

        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]
        
        popular_hour=return_popular_hour(period_df)

    return(popular_hour)

def return_popular_hour(raw_df):
    hour_name=raw_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%H"))

    all_hours=raw_df.groupby(hour_name)['Start Time'].agg(['count'])

    popular_hour=all_hours['count'].idxmax()
    return(popular_hour) 

def trip_duration(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"

    city_df = pd.read_csv(filename)
    
    if time_period == 'none':
    
        totalTime,average_time=return_trip_duration(city_df)        
    
    if time_period == 'month':
        
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]
        
        totalTime,average_time=return_trip_duration(period_df)        
    
    if time_period == 'day':
        
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]
        
        totalTime,average_time=return_trip_duration(period_df)        

    return(totalTime,average_time)

def return_trip_duration(raw_df):

    count=0
    
    totalTime=0
    
    for i in range(len(raw_df)):
    
        sTime=datetime.datetime.strptime(raw_df['Start Time'].values[i],"%Y-%m-%d %H:%M:%S")

        eTime=datetime.datetime.strptime(raw_df['End Time'].values[i],"%Y-%m-%d %H:%M:%S")

        timeDiff=eTime-sTime

        totalTime=totalTime+timeDiff.total_seconds()

        count+=1
    
        average_time=totalTime/count

    return(totalTime,average_time)


def popular_stations(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)

    if time_period == 'none':
        pStartStation=city_df.groupby(['Start Station']).size().idxmax()
        
        pEndStation=city_df.groupby(['End Station']).size().idxmax()
    
    if time_period == 'month':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]
        
        pStartStation=period_df.groupby(['Start Station']).size().idxmax()
        
        pEndStation=period_df.groupby(['End Station']).size().idxmax()
        
    if time_period == 'day':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]
        
        pStartStation=period_df.groupby(['Start Station']).size().idxmax()
        
        pEndStation=period_df.groupby(['End Station']).size().idxmax()

    return(pStartStation,pEndStation)
    

def popular_trip(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)

    if time_period == 'none':
        pTrip=city_df.groupby(['Start Station','End Station']).size().idxmax()
    
    if time_period == 'month':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]
        
        pTrip=period_df.groupby(['Start Station','End Station']).size().idxmax()
    
    if time_period == 'day':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]
        
        pTrip=period_df.groupby(['Start Station','End Station']).size().idxmax()

    return(pTrip)


def users(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)

    if time_period == 'none':
        userType=city_df.groupby(['User Type']).size()#.reset_index()

    if time_period == 'month':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]
        
        userType=period_df.groupby(['User Type']).size()#.reset_index()
    
    if time_period == 'day':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]
        
        userType=period_df.groupby(['User Type']).size()#.reset_index()
    
    print(userType)


def gender(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)

    if time_period == 'none':
        genderType=city_df.groupby(['Gender']).size()#.reset_index()

    if time_period == 'month':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]
        
        genderType=period_df.groupby(['Gender']).size()#.reset_index()

    if time_period == 'day':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]
        
        genderType=period_df.groupby(['Gender']).size()#.reset_index()

    print(genderType)


def birth_years(city_file, time_period,period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)
    
    popularBirthYear=city_df.groupby(['Birth Year']).size().idxmax()

    if time_period == 'none':
        city_df['Birth Year'].replace('', np.nan, inplace=True)
    
        minBirthYear=city_df['Birth Year'].min()
    
        maxBirthYear=city_df['Birth Year'].max()
    
    if time_period == 'month':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%B"))==period]

        period_df['Birth Year'].replace('', np.nan, inplace=True)
    
        minBirthYear=period_df['Birth Year'].min()
    
        maxBirthYear=period_df['Birth Year'].max()

    if time_period == 'day':
        period_df=city_df.loc[city_df['Start Time'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d %H:%M:%S").strftime("%A"))==period]

        period_df['Birth Year'].replace('', np.nan, inplace=True)
    
        minBirthYear=period_df['Birth Year'].min()
    
        maxBirthYear=period_df['Birth Year'].max()

    print("Earliest Birth Year is ",minBirthYear,"\nLatest Birth Year is ",maxBirthYear,"\nMost Popular Birth Year is ",popularBirthYear)        

def display_data(city_file, time_period):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    count=0

    filename = city_file.lower() + ".csv"
    
    city_df = pd.read_csv(filename)

    display = 'yes'
    
    # TODO: handle raw input and complete function
    while display != 'no':
        display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
        count+=1
        print(city_df.iloc[(count-1)*5:count*5])
    
    return 0


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print("Selected city:", city)

    if city.lower() == "new york":
        city="new_york_city"

    if city.lower() == "chicago":
        city="chicago"

    if city.lower() == "washington":
        city="washington"

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    print("Selected time period:", time_period)

    if time_period == 'none':
        period = 'NA'

    if time_period == 'month':
        period = get_month()

    if time_period == 'day':
        period = get_day()

    print('\nCalculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        
        popularMonth = popular_month(city,time_period)
        
        print(popularMonth, "is the most popular month")
        
        print("That took %s seconds." % (time.time() - start_time))
        
        print("\nCalculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        
        popularDay = popular_day(city,time_period,period)
        
        print(popularDay, "is the most popular day")

        print("That took %s seconds." % (time.time() - start_time))
        
        print("\nCalculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popularHour = popular_hour(city,time_period,period)
    
    print(popularHour, "is the most popular hour")

    print("That took %s seconds." % (time.time() - start_time))
    
    print("\nCalculating the next statistic...")
    
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    totalTime,averageTime=trip_duration(city,time_period,period)
    
    print("Total trip time is",totalTime, " and Average Trip Time ",averageTime)

    print("That took %s seconds." % (time.time() - start_time))
    
    print("\nCalculating the next statistic...")
    
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_start_station,popular_end_station=popular_stations(city,time_period,period)
    
    print("Most popular Start Station is ",popular_start_station," and most popular End Station is ",popular_end_station)

    print("That took %s seconds." % (time.time() - start_time))
    
    print("\nCalculating the next statistic...")
    
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    most_popular_trip = popular_trip(city,time_period,period)
    
    print("Most Popular trip is ",most_popular_trip)

    print("That took %s seconds." % (time.time() - start_time))
    
    print("\nCalculating the next statistic...")
    
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city,time_period,period)
    
    print("That took %s seconds." % (time.time() - start_time))
    
    print("\nCalculating the next statistic...")
    
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    if city.lower() != "washington":
        gender(city,time_period,period)
    
        print("That took %s seconds." % (time.time() - start_time))
    
        print("\nCalculating the next statistic...")
    
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    if city.lower() != "washington":
        birth_years(city,time_period,period)

        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city,time_period)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()