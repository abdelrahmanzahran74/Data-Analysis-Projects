import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("What is the city? chicago, new york city or washington?\n")
    city = city.lower()
    while city not in CITY_DATA:
        city = input("Please enter chicago, new york city or washington\n")
        
         
    # get user input for month (all, january, february, ... , june)
    month = input("what is the month? all, january, february, ... , june?\n")
    month = month.lower()
    while month != 'all' and month != 'january' and month != 'february' and month != 'march'and month != 'april' and month != 'may' and month != 'june':
          month = input("Please enter all, january, february, march, april, may or june\n") 
      

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What is day of week? all, monday, tuesday, ... sunday?\n")
    day = day.lower()
    while day != 'all' and day != 'saturday' and day !='sunday' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday':
                        day = input("Please enter all, saturday, sunday, monday, tuesday, wednesday, thursday or friday\n")
                     
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
    #Loading Data to chosen city
    df = pd.read_csv(CITY_DATA[city])
    #Converting the Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extracting the month, day of week and hour
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    #filtering month
    if month != 'all':
        # using the index of the months
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filtering by month
        df = df[df['month']==month]

    #filtering day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df['month'].mode()[0]
    print('Most common month:', most_month)

    # display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', most_day)

    # display the most common start hour
    most_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_ststation = df['Start Station'].mode()[0]
    print('Most common used start station:', most_ststation)

    # display most commonly used end station
    most_endstation = df['End Station'].mode()[0]
    print('Most common used end station:', most_endstation)

    # display most frequent combination of start station and end station trip
    most_trip = df.groupby(['Start Station', 'End Station'])
    print("the most frequent combination of start station and end station trip:", most_trip.size().sort_values(ascending=False).head(1))  
          
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Most total travel time in seconds:', total_time)
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The Mean of travel time in seconds', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    if city != 'washington':
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)

        # Display earliest, most recent, and most common year of birth
        ear_yr = df['Birth Year'].min()
        print('The earliest year:', ear_yr)

        rec_yr = df['Birth Year'].max()
        print('The earliest year:', rec_yr)

        most_yr = df['Birth Year'].mode()[0]
        print('The most common year of birth:', most_yr)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def read():
    while True:
        read_data = input("Do you like to read an individual trip data for a city?(y/n)\n")
        read_data = read_data.lower()
        
        if read_data == 'y':
            while True:
                city = input("What is the city? chicago, new york city or washington? you want to read data \n")
                city = city.lower()
                if city in CITY_DATA:
                    break
                else:
                    print("Please enter chicago, new york city or washington\n") 
                    
            for i in pd.read_csv(CITY_DATA[city], chunksize=5):
                print(i)
                read_more = input("Would you like to to read more?(y/n)\n")
                read_more = read_more.lower()
                if read_more != 'y':
                    break
        else:
            break
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        read()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
