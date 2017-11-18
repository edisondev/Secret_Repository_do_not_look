
from sodapy import Socrata
import pandas as pd

# Named constants
# Cities
CALGARY = 'calgary'
EDMONTON = 'edmonton'

# Data types
FIRE = 'fire'
EDUCATION = 'education'

# Data urls for each city
calgary = {
    FIRE : "https://data.calgary.ca/resource/mqii-992y.csv",
    EDUCATION : "https://data.calgary.ca/resource/gddc-smf3.csv"
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
            df = None

        return df


if __name__ == '__main__':
    print("Started testing")
    caller = API_Caller()
    df = caller.get_data(EDMONTON, EDUCATION)
    if df is not None:
        print(df.head(5))


