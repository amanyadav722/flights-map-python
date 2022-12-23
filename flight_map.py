import csv
from flight import Flight
from airport import Airport
from flight_path import FlightPath


class FlightMap:
    def __init__(self):
        self.__airports = []
        self.__flights = []

    def import_airports(self, csv_file : str):
        airports = []
        with open("./aeroports.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name, code, lat, long = row
                airport = Airport(name, code, float(lat), float(long))
                airports.append(airport)
        self.airports = airports

    def import_flights(self, csv_file : str):
        flights = []
        with open("./flights.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                src_code, dst_code, duration = row
                flight = Flight(src_code, dst_code, float(duration))
                flights.append(flight)
        self.flights = flights

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


"""
import csv
from airport import Airport
from flight import Flight


class FlightMap:
    def __init__(self):
        self.__airports = []
        self.__flights = []

    def import_airports(self, csv_file: str):
        airports = []
        with open("./aeroports.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name, code, lat, long = row
                airport = Airport(name, code, float(lat), float(long))
                airports.append(airport)
        self.airports = airports

    def import_flights(self, csv_file: str):
        flights = []
        with open("./flights.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                src_code, dst_code, duration = row
                flight = Flight(src_code, dst_code, float(duration))
                flights.append(flight)
        self.flights = flights

    def airports(self):
        return self.airports

    def flights(self):
        return self.flights

    def airport_find(self, airport_code: str):
        for airport in self.airports:
            if airport.code == airport_code:
                return airport
        return None

    def flight_exist(self, src_airport_code: str, dst_airport_code: str):
        for flight in self.flights:
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
                return True
            else:
                return False

    def flights_where(self, airport_code: str):
        flights = []
        for flight in self.flights:
            if flight.src_code == airport_code or flight.dst_code == airport_code:
                flights.append(flight)
        return flights

    def airports_from(self, airport_code: str):
        airports = []
        for flight in self.flights:
            if flight.src_code == airport_code:
                airports.append(self.airport_find(flight.dst_code))
        return airports

"""
