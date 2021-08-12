import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

travel_date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# travel_date = "2005-11-10"

url = f"https://www.billboard.com/charts/hot-100/{travel_date}"

response = requests.get(url)
top_songs_page = response.text

soup = BeautifulSoup(top_songs_page, 'html.parser')

all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

SPOTIFY_ID = "da2e4b6bfe6e438ea7fc474c743fd03b"
SPOTIFY_SECRET = "b2d20024a2b9413ab8aacae08d1643ef"
SPOTIFY_REDIRECT = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_REDIRECT,
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# for title in all_songs:
#     song_uris.append(title.getText())

song_uris = []
year = travel_date.split("-")[0]
for song in all_songs:
    result = sp.search(q=f"track:{song.getText()} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
