from dotenv import load_dotenv
import os
import googlemaps
from datetime import datetime

#loads environment file
def configure():
    load_dotenv()

#Grabs apikey from .env file and uses google distance matrix to find travel time
def find_dist():
    morning = datetime(2025, 9, 29, 7, 30)
    apikey = os.getenv('api_key')
    gmaps = googlemaps.Client(key=apikey)
    distance = gmaps.distance_matrix('301 Sparkman Dr NW, Huntsville, AL 35899' , '4122 Rideout Rd, Huntsville, AL 35808' , mode='driving', units='imperial', departure_time=morning)
    print(distance)

def main():
    configure()
    find_dist()

main()