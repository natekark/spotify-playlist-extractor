# Spotify Playlist Extractor 🎵  

A simple Python script that extracts song titles from a Spotify playlist using the Spotipy library.  

## 🚀 Features  
- Fetches all tracks from a Spotify playlist  
- Displays the song titles in the console  
- Uses Spotipy for Spotify API integration  

## 📦 Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/natekark/spotify-playlist-extractor.git
   cd spotify-playlist-extractor
Install dependencies:
bash
Copy
Edit
pip install spotipy
🔑 API Setup
Create a Spotify Developer account at Spotify Developer Dashboard.
Create an app and get your Client ID and Client Secret.
Replace the placeholders in extract_playlist.py with your credentials:
python
Copy
Edit
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
🛠️ Usage
Run the script:

bash
Copy
Edit
python extract_playlist.py
Modify the playlist_id variable to extract songs from a different playlist.

📌 Example Output
markdown
Copy
Edit
1. Song Title 1  
2. Song Title 2  
3. Song Title 3  
...
📋 Requirements
Python 3.7+
Spotipy (pip install spotipy)
⚖️ License
This project is for educational purposes. Feel free to modify and use it!
