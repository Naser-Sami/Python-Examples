# Use the requests module to make the HTTP requests to the web API.
import requests

# Prompt the user for first name and last name strings and store them into these
# variables to be used as values in our request to the API
# first_name = input("First Name: ")
# last_name = input("Last Name: ")

# The url (endpoint) for the Chuck Norris random joke API as specified by
# the API documentation.
# url = "http://api.icndb.com/jokes/random"
url = "https://official-joke-api.appspot.com/random_joke"

# Set the request parameters according to the API documentation such that
# we limit the jokes to "nerdy" category jokes, and customize the subject
# of the joke such that the joke is about a person with the first name and
# last name that the user entered when prompted.
# params = {"limitTo" : "[nerdy]",
        #   "firstName" : first_name,
        #   "lastName" : last_name}

# Make the request to the API using the url and params we've set above, we'll
# use response to deal with the response object.
# response = requests.get(url, params)

# The API returns JSON formatted data, we use the .json() method to get back
# a Python dictionary representation of this JSON data, and then we access
# the value at the key value followed by the key joke.  We know that the joke
# is at this location due to looking at the format of the response from
# the API.
# joke = response.json()["value"]["joke"]

# Output the joke to the terminal
# print(joke)

response = requests.get(url)
print(response.text)
# {
#   "type":"general",
#   "setup":"What do ghosts call their true love?",
#   "punchline":"Their ghoul-friend",
#   "id":103
# }

joke_q = response.json()['setup']
joke_a = response.json()['punchline']
print(joke_q)
print(joke_a)
