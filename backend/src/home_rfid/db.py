import json
from .settings import DB_LOCATION
import sqlite3


class HomeRFIDDB:
    def __init__(self):
        self.con = sqlite3.connect(DB_LOCATION)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def get_action_from_id(self, action_id):
        self.cur.execute(
            "SELECT * FROM actions WHERE action_id=:action_id",
            {
                'action_id': action_id
            }
        )

        raw_row = dict(self.cur.fetchone())
        return {
            'action_id': action_id,
            'module': raw_row['module'],
            'extra': json.loads(raw_row['extra'])
        }

    def add_action(self, action):
        self.cur.execute(
            "INSERT INTO actions (module, extra) VALUES (:module, :extra)",
            {
                'module': action['module'],
                'extra': json.dumps(action['extra'])
            }
        )
        self.con.commit()

        # Get the last added action ID. This has to be wrong...
        self.cur.execute("SELECT MAX(action_id) AS action_id FROM actions")
        return dict(self.cur.fetchone())['action_id']

    def list_cards(self):
        self.cur.execute("SELECT * FROM cards")
        details = {}

        for r in [dict(row) for row in self.cur.fetchall()]:
            print(r)
            details[r['card_id']] = {
                'name': r['name'],
                'actions': [
                    self.get_action_from_id(action_id) for action_id in
                    json.loads(r['action_ids'])
                ]
            }

        return details

    def get_card(self, card_id):
        self.cur.execute(
            "SELECT * FROM cards WHERE card_id=:card_id",
            {
                'card_id': card_id
            }
        )

        card = dict(self.cur.fetchone())
        return card

    def add_card(self, card_id, card_name, actions):
        actions_list = [
            self.add_action(action) for action in actions
        ]

        self.cur.execute(
            "INSERT OR REPLACE INTO cards (name, card_id, action_ids) VALUES (:name, :card_id, :action_ids)",
            {
                'name': card_name,
                'card_id': card_id,
                'action_ids': json.dumps(actions_list)
            }
        )
        self.con.commit()

    def is_configuring(self):
        '''
        Return True if the reader should be in configure mode for the next
        card.
        '''
        self.cur.execute("SELECT * FROM state")

        result = self.cur.fetchone()
        return result == 0

    def set_is_configuring(self, val):
        '''
        Set is_configuring in the state table to True or False.
        '''
        self.cur.execute(f"UPDATE state SET is_configuring={val}")
        self.con.commit()
