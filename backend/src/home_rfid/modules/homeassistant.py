import json
import requests


class HomeAssistantModule:
    def __init__(self):
        print("Init HA module.")
        self.headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIwZWZmYjAzYzgyZGQ0ZTk0YmZiNTU0MTkwMjkwNzI4MCIsImlhdCI6MTYzOTA3OTAwMSwiZXhwIjoxOTU0NDM5MDAxfQ.uXwFFDto3N25PpB5WO94Ycetv7VXEmwx2b_1kpfezxs",
            "content-type": "application/json",
        }

        self.api_base_url = "https://home.randombits.host/api/"
        self.states_url = self.api_base_url + "states"
        self.services_url = self.api_base_url + "services"

    def should_include_entity(self, entity):
        '''
        Return True if an entity should be kept (e.g. lights, swithches,
        etc
        '''
        return any([
            entity['entity_id'].startswith('light'),
            entity['entity_id'].startswith('switch'),
        ])

    def get_actions_for_entity(self, entity):
        '''
        Returns what each entity is capable of.
        '''
        if (entity['entity_id'].startswith('light')):
            return [
                'turn_on',
                'turn_off',
                'toggle'
            ]
        if (entity['entity_id'].startswith('switch')):
            return [
                'turn_on',
                'turn_off',
                'toggle'
            ]

    def get_actions(self):
        '''
        Returns all the actions that HA can expose/interact with.
        '''
        response = requests.get(self.states_url, headers=self.headers)
        all_entities = json.loads(response.text)

        trimmed_entities = [
            {
                'entity_id': e['entity_id'],
                'entity_name': e['attributes']['friendly_name'],
                'actions': self.get_actions_for_entity(e)
            } for e in all_entities
            if self.should_include_entity(e)
        ]
        print(trimmed_entities)

        return trimmed_entities

    def perform_action(self, action):
        print('===========')
        print(action)

        #action_details = json.loads(action['extra'])
        #entity_type = action_details['entity_id'].split('.')[0]
        action_details = action['extra']
        entity_type = action_details['entityID'].split('.')[0]

        url = self.services_url + '/' + entity_type + '/' + action_details['action']

        # Have to delete things that HA is not expecting.
        payload = {
            'entity_id': action_details['entityID']
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        print(response.text)
