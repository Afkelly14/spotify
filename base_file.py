import json
from pprint import pprint
import requests
import secrets

class lastFmSpotify:
    def __init__(self):
        self.token = secrets.spotify_token()
        self.api_key = secrets.last_fm_api_key()
        self.user_id = secrets.spotify_user_id()
        self.headers = {"Content-Type": "application/json",
                        "Authorization": f"Bearer {self.token}"}
        self.playlist_id = ''

    def fetch_songs_from_lastfm(self):
        params = {'limit': 20, 'api_key': self.api_key}
        url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&format=json'
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print('ERROR')
        response = response.json()
        for item in response['tracks']['track']:
            pprint(item)
            print('\n\n')

    def get_uri_from_spotify(self):
        pass

    def create_spotify_playlist(self):
        pass

    def add_songs_to_playlist(self):
        pass

    def list_songs_in_playlist(self):
        pass

d = lastFmSpotify()
d.fetch_songs_from_lastfm()