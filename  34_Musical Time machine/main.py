from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = "YOUR-CLIENT-ID"
CLIENT_SECRET = "YOUR-CLIENT_SECRET_KEY"

# User input for the travel date
date = input("Which Year do you want to travel to? Enter the date in YYYY-MM-DD format:")
print("Fetching Billboard Hot 100 songs for:", date)

# Define headers to mimic a request from a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"
}

# Construct the URL for the given date on the Billboard website
url = f"https://www.billboard.com/charts/hot-100/{date}"

# Requesting and parsing the Billboard Hot 100 page
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for successful response

    # Parse the page to extract song titles
    soup = BeautifulSoup(response.text, "html.parser")
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    print("Top Songs:", song_names)
except requests.exceptions.RequestException as e:
    print("An error occurred while fetching the Billboard Hot 100 songs:", e)
    song_names = []  # Initialize as empty in case of failure

# Initialize Spotify client with OAuth
try:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    # Fetching the current user ID
    user_id = sp.current_user()["id"]
    print("User ID:", user_id)
except Exception as e:
    print("An error occurred during Spotify authorization or user retrieval:", e)
    user_id = None

# Proceed if user ID and song names were successfully fetched
if user_id and song_names:
    song_uris = []
    year = date.split("-")[0]  # Extract the year for Spotify search

    # Search Spotify for each song title
    for song in song_names:
        try:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            print(f"Searching for song: {song}")

            # Attempt to get the URI of the first search result
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"Found {song} on Spotify: {uri}")
        except IndexError:
            print(f"{song} does not exist on Spotify. Skipping.")
        except Exception as e:
            print(f"An error occurred while searching for {song}: {e}")

    # Create a new private playlist if songs were found
    try:
        playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
        print("Playlist created:", playlist["name"], playlist["id"])

        # Add songs to the playlist
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
        print("Songs added to the playlist successfully.")
    except Exception as e:
        print("An error occurred while creating the playlist or adding songs:", e)
else:
    print("Could not proceed with playlist creation due to missing data.")
