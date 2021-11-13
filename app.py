import requests


response = requests.get("https://swapi.dev/api/films")

api = response.json()

api_results = api['results']

data = {}

for film in api_results:
    vehicles = film['vehicles']
    for vehicle in vehicles:
        if vehicle not in data:
            data[vehicle] = 1
        else:
            data[vehicle] += 1

print(data)

# for film in api_results:
#     characters = film['characters']
#     for character in characters:
#         if character == "https://swapi.dev/api/people/2/":
#              print(film['title'])
