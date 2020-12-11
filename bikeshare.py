import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# fghaiati: imported calendar library to use month_name , day_name methods. 
import calendar
# refrences: https://stackoverflow.com/questions/6557553/get-month-name-from-number.
#            https://docs.python.org/2/library/calendar.html
months_names = ['all' if idx==0 else calendar.month_name[idx].lower() for idx in range(13)] # this generator produces an list of months

# fghaiati: get user input for day of week (all, monday, tuesday, ... sunday)
# fghaiati: imported calendar library to use day_name method 
days_names = ['all' if idx==-1 else calendar.day_name[idx].lower() for idx in range(-1,7,1)] # this generator produces an list of days

    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week        
        to filter by, or "all" to apply n """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # fghaiati: while loop to get input (value) of a variable name from provied list of values. 
    # fghaiati: while loop to handle invalid inputs
    def input_loop(var_name , var_list):
        #selected_var = '' # no need to initalize in python
        while 1:
            #use tuple to place () and replace ' to be as per assignment
            selected_var = input('Please input {} as value from {}:'.format(var_name, str(tuple(var_list)).replace("'",'')) ) 
            if selected_var not in var_list:
                print('[X] Invalid {}, please enter a valid {} as provided in the list.'.format(var_name,var_name))
            else:
                print ('[Ok] Selected {}: {}\n'.format(var_name,selected_var))
                break
        return selected_var
    
    # TO DO: get user input for month (all, january, february, ... , june)
    # fghaiati: get user input for city (chicago, new york city, washington)
    city = input_loop('city' , CITY_DATA.keys())
    
    # fghaiati: get user input for month (all, january, february, ... , june)
    month = input_loop('month' , months_names)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_loop('day' , days_names)


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'], df['End Time'] = pd.to_datetime(df['Start Time']), pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name() #dayofweek
    #debug:print(df['Month'].unique())
    #debug:print(df['Day of Week'].unique())

    # filter by month if required
    if month != 'all':
        # filter df by month
        df = df[df['Month'] == months_names.index(month)] #df.query('Month=={}'.format(months_names.index(month)))

    # filter by day of week if required
    if day != 'all':
        # filter df by day of week
        df = df[df['Day of Week'] == day.title()] 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common Month: {}'.format(months_names[df['Month'].mode()[0]].title()))

    # TO DO: display the most common day of week
    print('The most common Day of Week: {}'.format(df['Day of Week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common Start Hour: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    # TO DO: display most commonly used start station
    print('The most common used user start station: {}'.format(df['Start Station'].mode()[0]))
    

    # TO DO: display most commonly used end station
    print('The most common used user end station: {}'.format(df['End Station'].mode()[0]))


    #print('{}'.format(('FROM: ' + df['Start Station'] + ' TO: ' + df['End Station']).value_counts()))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most common used user end station: {}'.format(('FROM: ' + df['Start Station'] + ' TO: ' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time: {}'.format((df['End Time'] - df['Start Time']).sum()) )


    # TO DO: display mean travel time
    print('The mean travel time: {}'.format((df['End Time'] - df['Start Time']).mean()) )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        print('The counts of user types:\n{}\n'.format(pd.DataFrame(df['User Type'].value_counts())))
    else:
        print('Hint selected city file has no User Type column.')


    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('The counts of Gender:\n{}\n'.format( pd.DataFrame(df['Gender'].value_counts()) ))
    else:
        print('Hint selected city file has no Gender column.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df:
        print('The earliest, most recent and most common year of birth: {}, {}, {}'.format(int(df['Birth Year'].min()), 
                                                                                           int(df['Birth Year'].max()), 
                                                                                           int(df['Birth Year'].mode()[0])))
    else:
        print('Hint selected city file has no Birth Year column.')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data_view(df):
    """Displays selected data in pages of 5 rows each."""

    rows_no = df.size
    pages_no = (rows_no//5) + (0 if rows_no%5==0 else 1) 
    if rows_no == 0:
        print('\nYour filter returned 0 rows in selected city.')
    else:
        view_page = str(input('\nFiltered Data has {} rows, would you like to view data 5 rows each time? Enter no to exit.\n'.format(rows_no))).lower()
        page_no = 0
        while view_page!='no':
            print(df[page_no*5:(page_no+1)*5])
            view_page = str(input('\nView next 5 rows? Enter no to exit.\n')).lower()
            page_no +=1
            if page_no>pages_no:
                break
   
def main():
    while True:
        city, month, day = get_filters() #test:'chicago', 'may', 'saturday'
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        data_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
