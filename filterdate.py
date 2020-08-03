
from secrets import spotify_token
import requests
query = "https://api.spotify.com/v1/me/albums"

response = requests.get(
    query,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(spotify_token)
    }
)
response_json = response.json()
release_date = response_json['items'][0]['album']['release_date']
selectedalbums = [albumentry['album']['name'] for albumentry in response_json['items'] if 1950 <= int(albumentry['album']['release_date'][:4]) <= 1999]
print(selectedalbums)