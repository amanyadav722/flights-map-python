"""
Classe Airport :

class Airport:
    def __init__(self, name, code, lat, long):
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

Classe Flight :

class Flight:
    def __init__(self, src_code, dst_code, duration):
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

Classe FlightMap :

class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []

    def import_airports(self, csv_file):
        # Load CSV file
        data = load_csv(csv_file)
        # Parse data and create airport objects
        for row in data:
            self.airports.append(Airport(row[0], row[1], float(row[2]), float(row[3])))

    def import_flights(self, csv_file):
        # Load CSV file
        data = load_csv(csv_file)
        # Parse data and create flight objects
        for row in data:
            self.flights.append(Flight(row[0], row[1], float(row[2])))

    def airports(self):
        return self.airports

    def flights(self):
        return self.flights

    def airport_find(self, airport_code):
        for airport in self.airports:
            if airport.code == airport_code:
                return airport
        return None

    def flight_exist(self, src_airport_code, dst_airport_code):
        for flight in self.flights:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
        return False

    def flights_where(self, airport_code):
        flights = []
        for flight in self.flights:
            if flight.src_code == airport_code or flight.dst_code == airport_code:
                flights.append(flight)
        return flights

    def airports_from(self, airport_code):
        airports = []
        for flight in self.flights_where(airport_code):
            if flight.src_code == airport_code:
                airports.append(self.airport_find(flight.dst_code))
            elif flight.dst_code == airport_code:
                airports.append(self.airport_find(flight.src_code))
        return airports

    def paths(self, src_airport_code, dst_airport_code):
        paths = []
        airports_not_visited = self.airports[:]
        airports_future = self.airports_from(src_airport_code)
        airports_visited = [self.airport_find(src_airport_code)]
        while len(airports_not_visited) > 0 and len(airports_future) > 0:
            airport_current = airports_future.pop(0)
            airports_visited.append(airport_current)
            airports_not_visited.remove(airport_current)
            if airport_current.code == dst_airport_code:
                paths.append(FlightPath(src_airport_code, airports_visited))
            else:
                for airport in self.airports_from(airport_current.code):
                    if airport not in airports_visited:
                        airports_future.append(airport)
        return paths

    def paths_shortest_length(self, src_airport_code, dst_airport_code):
        paths = self.paths(src_airport_code, dst_airport_code)
        shortest_paths = []
        shortest_length = float('inf')
        for path in paths:
            if path.steps() < shortest_length:
                shortest_length = path.steps()
                shortest_paths = [path]
            elif path.steps() == shortest_length:
                shortest_paths.append(path)
        return shortest_paths

    def paths_shortest_duration(self, src_airport_code, dst_airport_code):
        paths = self.paths(src_airport_code, dst_airport_code)
        shortest_paths = []
        shortest_duration = float('inf')
        for path in paths:
            if path.duration() < shortest_duration:
                shortest_duration = path.duration()
                shortest_paths = [path]
            elif path.duration() == shortest_duration:
                shortest_paths.append(path)
        return shortest_paths

    def paths_via(self, src_airport_code, dst_airport_code, via_airport_code):
        paths = self.paths(src_airport_code, dst_airport_code)
        via_paths = []
        for path in paths:
            if via_airport_code in [airport.code for airport in path.airports()]:
                via_paths.append(path)
        return via_paths

    def paths_via_multi(self, src_airport_code, dst_airport_code, via_airports_codes):
        paths = self.paths(src_airport_code, dst_airport_code)
        via_paths = []
        for path in paths:
            airports_codes = [airport.code for airport in path.airports()]
            if set(via_airports_codes).issubset(set(airports_codes)):
                via_paths.append(path)
        return via_paths


Classe FlightPathBroken :

class FlightPathBroken(Exception):
    pass


Classe FlightPathDuplicate :

class FlightPathDuplicate(Exception):
    pass


Classe FlightPath :

class FlightPath:
    def __init__(self, src_airport, airports):
        self.src_airport = src_airport
        self.airports = airports
        self.flights = []

    def add(self, dst_airport, via_flight):
        if self.airports[-1].code != via_flight.src_code:
            raise FlightPathBroken
        if self.airports.count(dst_airport) > 0:
            raise FlightPathDuplicate
        self.airports.append(dst_airport)
        self.flights.append(via_flight)

    def flights(self):
        return self.flights

    def airports(self):
        return self.airports

    def steps(self):
        return len(self.flights)

    def duration(self):
        return sum([flight.duration for flight in self.flights])

"""