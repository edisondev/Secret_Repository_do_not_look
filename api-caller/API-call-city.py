
from sodapy import Socrata
import pandas as pd

# Named constants
# Cities
CALGARY = 'calgary'

# Data types
FIRE = 'fire'

# Data urls for each city
calgary = {
    FIRE : "https://data.calgary.ca/resource/mqii-992y.csv"
}

# Cities dict
cities = {
    CALGARY:calgary
}


class API_Caller:

    def get_data(self, city, type):
        # Main function for fetching data directly
        # returns a panda dataframe
        url = cities[city][type]
        df = pd.read_csv(url)
        return df





if __name__ == '__main__':
    print("Started testing")
    caller = API_Caller()
    df = caller.get_data(CALGARY, FIRE)
    print(df.head(5))


