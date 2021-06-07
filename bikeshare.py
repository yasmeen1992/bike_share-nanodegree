import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input ("Enter name of city(chicago, new york city, washington) :")
        if city not  in CITY_DATA:
            print("Not an appropriate choice.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month=input ("Enter input for month using (all, january, february, ... , june) :")
        if month not  in months and month!='all':
            print("Not an appropriate choice.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day=input ("Enter input for day of week using (all, monday, tuesday, ... sunday) :")
        if day not  in days and day!='all':
            print("Not an appropriate choice.")
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
   # print(df['month'] )
    #print(df['day_of_week'] )

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month']==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #print(df['month'])
    popular_month=df['month'].mode()[0]
    popular_month_name=months[popular_month-1]
    # TO DO: display the most common month
    print("The most common month:", popular_month_name)
    # TO DO: display the most common day of week
    #print(df['day_of_week'])
    popular_day_of_week=df['day_of_week'].mode()[0]
    print("The most common day of week:", popular_day_of_week)
    # TO DO: display the most common start hour
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['hour'] =  df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour:", popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print("The most common used start station:", popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print("The most common used end station:", popular_end_station)
     # TO DO: display most frequent combination of start station and end station trip
    print("The most common used start station is {0} and end sattion is {1} in trip".format(popular_start_station, popular_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print(" total travel time:",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print(" mean travel time:",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("count of user types: \n ",user_types)
    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("count of gender: \n ",gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth_year=df['Birth Year'].min()
    recent_birth_year=df['Birth Year'].max()
    popular_birth_year=df['Birth Year'].mode()[0]
    print("The earliest year of birth is {0} ,the most recent year of birth is {1} and most common year of birth is {2} ".format(str(earliest_birth_year), str(recent_birth_year),str(popular_birth_year)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
