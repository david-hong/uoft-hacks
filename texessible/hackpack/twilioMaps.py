import googlemaps
import time
from datetime import datetime
from datetime import timedelta
import re

class Directions:
    #address only street & number, stat is province, country
    def __init__(self, start = "", endAddress = ""):
        self.startPoint = start
        self.endLoc = endAddress

    def getDirections(self):
        gmaps = googlemaps.Client(key='#')
        geocode_result = gmaps.geocode(self.startPoint)
        now = datetime.now()
        directions_result = gmaps.directions(self.startPoint,
                                             self.endLoc,
                                             mode="driving", departure_time=now)
        return directions_result[0]['legs'][0]['steps']

    def parseDirections(self, directions):
        result = re.sub(r'<[^<]*?>', "", str(directions))
        return result

    def printDirections(self):
        direc = Directions(self.startPoint, self.endLoc)
        result = direc.getDirections()
        string = ""
        for i in range (0, len(result)):
            string += (str(i) + ": " + \
            direc.parseDirections(result[i]['html_instructions'])) + "\n"
        return string
