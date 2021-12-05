import datetime
from typing import List


class Company:
    def __init__(self, company_id: str, name: str):
        self.__company_id = company_id
        self.__name = name
        self.__planes = None

    def add_plane(self, plane):
        self.__planes.append(plane)


class Airport:
    def __init__(self, city: str):
        self.end_date = None
        self.start_date = None
        self.__city = city
        self.planes = None
        self.scheduled_departures = None
        self.scheduled_arrivals = None

    def add_plane(self, plane):
        self.__planes.append(plane)

    def scheduled_flight(self, destination, datetime):
        pass

    def info(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        print(f"{flight in start_date, end_date}")


class Airplane:
    def __init__(self, airplane_id: int, current_location: Airport, company: Company):
        self.airplane_id = airplane_id
        self.current_location = current_location
        self.company = company
        self.next_flights = None

    def fly(self, destination):
        self.current_location = destination
        self.next_flights.pop(0)

    def location_on_date(self, date):
        for flight in self.next_flights:
            if flight.date == date:
                return flight.origin_airport

    def available_on_date(self, date, location):
        future_location = self.location_on_date(date)
        # if future_location == location:
        #     return True
        # else:
        #     return False
        return future_location == location


class Flight:
    def __init__(self, date: datetime.date, destination: Airport, origin: Airport, plane: Airplane, id: str):
        self.date = date.datetime.Date
        self.destination_airport = destination
        self.origin_airport = origin
        self.plane = plane

    def take_off(self):
        self.plane.current_location = self.origin_airport

    def land(self):
        self.plane.current_location = self.destination_airport


date = datetime.date(2021, 12, 6)

#creating airports
tlv_airport = Airport("TLV")
usa_airport = Airport("USA")

#creating company
alitalia = Company(name="airbus")

#creating flight
usa_12_6 = Flight(date=date, plane=alitalia1, destination=usa_airport, origin=tlv_airport, id="usa_12_6")

#creating airplane
alitalia_1 = Airplane(current_location=tlv_airport, company=alitalia)

alitalia.add_plane(alitalia_1)

print(alitalia.planes)