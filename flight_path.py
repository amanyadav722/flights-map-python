from flight_path_broken import FlightPathBroken
from flight_path_duplicate import FlightPathDuplicate
from flight import Flight
from airport import Airport


class FlightPath:
    def __init__(self, src_airport: Airport, airports):
        self.src_airport = src_airport
        self.airports = airports
        self.flights = []

    def add(self, dst_airport: Airport, via_flight: Flight):
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
