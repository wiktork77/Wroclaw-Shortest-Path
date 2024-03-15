class Stop:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return (self.name, self.latitude, self.longitude) == (other.name, other.latitude, other.longitude)

    def __hash__(self):
        return hash((self.name, self.latitude, self.longitude))

    def __repr__(self):
        return f"{self.name}: {self.latitude, self.longitude}"


class Connection:
    def __init__(self, start_stop, end_stop, executions):
        self.start_stop = start_stop
        self.end_stop = end_stop
        self.executions = executions

    def __eq__(self, other):
        return (self.start_stop, self.end_stop) == (other.start_stop, other.end_stop)


class Execution:
    def __init__(self, company, line, departure_time, arrival_time):
        self.company = company
        self.line = line
        self.departure_time = departure_time
        self.arrival_time = arrival_time


def model_stops(row):
    stop1 = Stop(row.start_stop, row.start_stop_lat, row.start_stop_lon)
    stop2 = Stop(row.end_stop, row.end_stop_lat, row.end_stop_lon)
    return stop1, stop2


def model_connection(row):
    stop1, stop2 = model_stops(row)





def model_data(df):
    # byc moze lepiej na poczatku zbudowac strukture, ktora bedzie zawierala polaczenia, a pozniej na podstawie tych
    # polaczen zbudowac zbior unikalnych wierzcholkow (przystankow)
    connections = []
    for row in df.itertuples():
        stop1, stop2 = model_stops(row)
        pass


# zastanowic sie
def model_connections(df)
    pass



def model_data_itertuples(df):
    stops = model_stops(df)


def model_data_iterrows(df):
    for row in df.iterrows():
        pass



