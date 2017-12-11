# my api keys are in personnel_key file you have to add your key to run this program.
from personnel_key import *
#we import requests package to access get reqeuest
import requests
import tweepy,time

# def get_lat_log(location):
#     address = location
#     api_key = google_api
#     api_response = requests.get(
#         'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
#     api_response_dict = api_response.json()
#     if api_response_dict['status'] == 'OK':
#         latitude = api_response_dict['results'][0]['geometry']['location']['lat']
#         longitude = api_response_dict['results'][0]['geometry']['location']['lng']
#         return latitude,longitude

# this function returns the driving distance from source address to destination address
# requirement : google_distance_matrix_api


def get_distance(orig_address,dest_address):
    reponse = requests.get(
        "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=bus&"
        "language=fr-FR&key={2}".format(orig_address, dest_address, google_distance_api))
    result = reponse.json()
    driving_distance = result['rows'][0]['elements'][0]['distance']['text']
    return driving_distance


# asking user to enter source and destination address
orig_address = raw_input("Enter source address:\n")
dest_address = raw_input("Enter destination address:\n")
driving_distance = get_distance(orig_address,dest_address)

# using tweepy package we are authenticating the application
# requirement : consumer_key, consumer_secret, access_token, access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# this will uptade status on my timeline
api.update_status("Distance between {0} and {1} is {2} #myfirstTweet".format(orig_address,dest_address,driving_distance))
# after updating the status it will go to sleep for about 1 minute
time.sleep(60)
