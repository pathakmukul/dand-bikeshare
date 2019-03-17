import time
import pandas as pd
import numpy as np
import calendar
import datetime



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city':  'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """

    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to app ly no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! and welcome to explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Please enter the name of the city from available city names for which you would like to see the data. Available cities are : chicago, new york city and washington ").lower()
    while True:
        if city not in ['chicago','new york city','washington']:
            city = input('Something is wrong. Please input city name again. Input either '
                  'Chicago, New York, or Washington. ').lower()
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Now, please select the month to check data from. Options : all, january, february,..., december. : ").lower()
    while True:
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']:
            month = input('Something is wrong. Please input month again . Options : all, january, february,..., december. : ').lower()
        else:
            break
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Now, please enter the day of the week to check the data from. Options : all, monday, tuesday,... sunday. :  ").lower()
    while True:
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input('Something is wrong. Please input day again. Options : all, monday, tuesday,... sunday. : ').lower()
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
    df = pd.read_csv(CITY_DATA[city])
     #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    trips_by_month = df.groupby(['month'])['Start Time'].count()
    print('The most common month was : ', calendar.month_name[int(trips_by_month.sort_values(ascending=False).index[0])])

    # TO DO: display the most common day of week
    #trips_by_day = df.groupby('day')['Start Time'].count()
    trips_by_day=trips_by_month
    print('The most common day was : ', calendar.day_name[int(trips_by_day.sort_values(ascending=False).index[0])])


    # TO DO: display the most common start hour         
    trips_by_hour_of_day = df.groupby(['Start Time'])['Start Time'].count()
    most_pop_hour_int = trips_by_hour_of_day.sort_values(ascending=False).index[0]
    d = datetime.datetime.strptime(str(most_pop_hour_int), "%Y-%m-%d %H:%M:%S")
    print("Most popular hour of the day for start time: " + d.strftime("%I %p"))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df.groupby(['Start Station'])['Start Station'].count()
    common_start_station_int = common_start_station.sort_values(ascending=False).index[0]
    print("Most commom station: " + common_start_station_int)
    
    # TO DO: display most commonly used end station
    common_end_station = df.groupby(['End Station'])['End Station'].count()
    common_end_station_int = common_end_station.sort_values(ascending=False).index[0]
    print("Most commom trip ending station: " + common_end_station_int)    

    # TO DO: display most frequent combination of start station and end station trip
    df['journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_pop_trip = df['journey'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time : " + str(total_travel_time))    

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time : " + str(mean_travel_time))   
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
#     subscribers = df.query('User Type == "Subscriber"').count()
#     customers = df.query('User Type == "Customer"').count()
#     print('Total number of user types are :- \n  Subscribers {} and \n Customers {}.'.format(subscribers, customers))

    counts = df['User Type'].value_counts()
    print("User counts are : ")
    print(counts)


    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print("Data on genders are : ")
    print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    latest = int(df['Birth Year'].max())
    mode = int(df['Birth Year'].mode())
    print('Year of Birth of the earliest user is:  {}.\n Year of Birth of the most recent user is: {}.'
          '\n The most common Year of Birth is: {}.'.format(earliest, latest, mode))


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

