
from sodapy import Socrata
import pandas as pd

# Named constants
# Cities
CALGARY = 'calgary'
EDMONTON = 'edmonton'

# Data types
FIRE = 'fire'
EDUCATION = 'education'
AIRQUALITY = 'air quality'
AIRQUALITY_COLS = 'air quality columns' # Name of columns we use for air quality data

# Data urls for each city
calgary = {
    FIRE : "https://data.calgary.ca/resource/mqii-992y.csv",
    EDUCATION : "https://data.calgary.ca/resource/gddc-smf3.csv",
    AIRQUALITY : "https://data.calgary.ca/resource/88iq-yi9x.csv",
    AIRQUALITY_COLS : ["station_name", "parameter", "date", "average_daily_value"]
}

edmonton = {
    FIRE : "https://data.edmonton.ca/resource/hpqc-zvnm.csv"
}

# Cities dict
cities = {
    CALGARY : calgary,
    EDMONTON : edmonton
}


class API_Caller:

    def get_data(self, city, type):
        # Main function for fetching data directly
        # returns a panda dataframe
        try:
            url = cities[city][type]
            df = pd.read_csv(url)
        except KeyError:
            print("%s data link doesn't exist for %s" %(type, city))
            return

        df = self.clean_df(df, city, type)

        return df

    def clean_df(self, df, city, type):
        try:
            if type == AIRQUALITY:
                columns = df.columns
                columns_keep = cities[city][AIRQUALITY_COLS]
                columns_del  = [c for c in columns if c not in columns_keep]
                df = df.drop(columns_del, axis=1)
        except KeyError:
            print("The key for data clean up does not match the data set")

        return df



if __name__ == '__main__':
    print("Started testing")
    caller = API_Caller()
    df = caller.get_data(CALGARY, AIRQUALITY)
    if df is not None:
        print(df.head(5))


