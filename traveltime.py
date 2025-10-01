from dotenv import load_dotenv
import os
import googlemaps
from datetime import datetime

#loads environment file
def configure():
    load_dotenv()

#Grabs apikey from .env file and uses google distance matrix to find travel time
def find_distance(origin, destination, departure_time=None):
    apikey = os.getenv('api_key')
    if not apikey:
        raise ValueError("API key not found in .env file")
    
    gmaps = googlemaps.Client(key=apikey)

    if departure_time is None:
        departure_time = datetime.now()
    
    gmapsresult = gmaps.distance_matrix(origin, destination , mode='driving', units='imperial', departure_time=departure_time)
    
    
    duration_in_traffic = gmapsresult["rows"][0]["elements"][0]["duration_in_traffic"]["text"]
    distance_to_destination = gmapsresult["rows"][0]["elements"][0]["distance"]["text"]

    print(f" Origin: {origin} , Destination: {destination} , Duration: {duration_in_traffic}, Distance: {distance_to_destination} , TimeofDay: {departure_time}")



def main():
    configure()
    find_distance('301 Sparkman Dr NW, Huntsville, AL 35899', '4122 Rideout Rd, Huntsville, AL 35808')

main()