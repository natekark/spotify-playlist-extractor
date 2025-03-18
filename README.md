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
2. Install dependencies:
    ```bash
    pip install spotipy
## 🔑 API Setup
1. Create a Spotify Developer account at Spotify Developer Dashboard.

2. Create an app and get your Client ID and Client Secret.

3. Replace the placeholders in extract_playlist.py with your credentials:
    ```python
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"
## 🛠️ Usage
Run the script:
    ```bash
    python extract_playlist.py
Modify the playlist_id variable in the script to extract songs from a different playlist.

## 📌 Example Output
    Song Title 1
    Song Title 2
    Song Title 3
    ...
## 📋 Requirements
- Python 3.7+
- Spotipy (pip install spotipy)

## ⚖️ License
This project is for educational purposes. Feel free to modify and use it!
