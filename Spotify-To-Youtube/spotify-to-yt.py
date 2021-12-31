"""Note, this is unfinished and currently not working"""

import spotipy, os, pickle
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

load_dotenv()
credentials = None

print("""---- Welcome to Spotify 2 Youtube ----
        Convert your Spotify playlist 
        into one for Youtube!
      """)

if os.path.exists("Spotify-To-Youtube\\token.pickle"):
    print("Loading Credentials from File...")
    with open("Spotify-To-Youtube\\token.pickle", "rb") as token:
        credentials = pickle.load(token)

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print("Refreshing access token...")
        credentials.refresh(Request())
    else:
        print("Fetching New Tokens...")
        flow = InstalledAppFlow.from_client_secrets_file(
            "Spotify-To-Youtube\client_secrets.json",
            scopes=["https://www.googleapis.com/auth/youtube"],
        )

        flow.run_local_server(
            port=8080, prompt='consent', authorization_prompt_message=""
        )
        credentials = flow.credentials

        with open("Spotify-To-Youtube\\token.pickle", "wb") as f:
            print("Saving Credentials for Future Use...")
            pickle.dump(credentials, f)

spotify_id = os.getenv('SPOTIFY_ID')
spotify_secret = os.getenv('SPOTIFY_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_id,
                                                           client_secret=spotify_secret))

while True:
    try:
        print("Paste your spotify playlist link: ")
        splist = input()
        pl = sp.playlist(splist)
        playlists = sp.playlist_items(splist, limit=100, fields='items')
    except Exception as e:
        if e.code == -1:
            print('Error. Invalid playlist.')
    else:
        break

playlistName = pl['name']
songs = []
for y, x in enumerate(playlists['items']):
    songs.append(x['track']['album']['artists'][0]['name'] + ' - ' + x['track']['name'])
    print('Added to queue:', x['track']['album']['artists'][0]['name'], '-', x['track']['name'])

yt = build("youtube", "v3", credentials=credentials)
request = yt.playlistItems().list(
    part='status', playlistId="PLHMC-NnHBLvNFNJntyYdLqgx0Uk-4C-Gc"
)

response = request.execute()
print(response)
