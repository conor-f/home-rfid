import json
import requests


class SpotifyModule:
    def __init__(self):
        print("Init Spotify module.")

    def get_actions(self):
        '''
        Returns all the actions that Spotify can expose/interact with.
        '''
        return [
            'play_playlist'
        ]

    def perform_action(self, action):
        action_details = json.loads(action['extra'])
        print(f"Performing action {action}")
