import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up authentication
client_id = 'YOUR_CLIENT_ID'  # Replace with your actual client ID
client_secret = 'YOUR_CLIENT_SECRET'  # Replace with your actual client secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Specify the playlist URL or ID
playlist_id = 'YOUR_PLAYLIST_ID'  # Replace with your actual playlist ID

# Fetch the playlist data
results = sp.playlist_tracks(playlist_id)

# Print out the song titles
for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx + 1}. {track['name']}")

