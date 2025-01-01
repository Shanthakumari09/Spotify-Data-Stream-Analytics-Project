import os
from dotenv import load_dotenv
from spotify_utils import SpotifyUtils  # Adjust the import as per your file structure

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get credentials from environment variables
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    artist_id = "06HL4z0CvFAxyc27GXpf02"
    playlist_uri = ["spotify:playlist:37i9dQZF1DXcBWIGoYBM5M"]
    track_ids = ["3n3Ppam7vgaVa1iaRUc9Lp", "0VjIjW4GlUZAMYd2vXMi3b"]

    # Instantiate the SpotifyUtils class
    spotify_utils = SpotifyUtils(client_id, client_secret)

    # Test get_artist_from_playlist
    artist_df = spotify_utils.get_artist_from_playlist(playlist_uri)
    print("Artist DataFrame:")
    print(artist_df)

    # Test get_top_tracks_by_artist
    artist_id = artist_df.iloc[0]['artist_id']  # Use the first artist's ID from the DataFrame
    tracks_df = spotify_utils.get_top_tracks_by_artist(artist_id)
    print("Tracks DataFrame:")
    print(tracks_df)

    # Test get_audio_features
    audio_features_df = spotify_utils.get_audio_features(track_ids)
    print("Audio Features DataFrame:")
    print(audio_features_df)

    # Test generate_songs_data
    song_df = spotify_utils.generate_songs_data(playlist_uri)
    print("Songs DataFrame:")
    print(song_df)

if __name__ == "__main__":
    main()
    