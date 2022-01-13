from ..db import HomeRFIDDB
from ..modules import modules

import os
import time


class RFIDListener:
    def __init__(self):
        self.db = HomeRFIDDB()
        self.test_env = True

        if (self.test_env):
            print('testing...')
        else:
            import board
            import busio

            from digitalio import DigitalInOut

            from adafruit_pn532.spi import PN532_SPI

            # SPI connection:
            spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
            cs_pin = DigitalInOut(board.D5)
            self.pn532 = PN532_SPI(spi, cs_pin, debug=False)

            # Configure PN532 to communicate with MiFare cards
            self.pn532.SAM_configuration()

    def handle_unregistered_card(self, card_id):
        '''
        Triggered when an unregistered card is read.
        '''
        print(f'handle_unregistered_card {card_id}')
        self.db.set_is_configuring(False)

    def handle_registered_card(self, card):
        '''
        Triggered when a registered card is read.
        '''
        print(f'handle_registered_card {card}')

        for action_id in eval(card['action_ids']):
            action = self.db.get_action_from_id(action_id)
            print(action)

            # I don't want to talk about how bad this code is...
            for module in modules:
                if module['module_id'] == action['module']:
                    module['module'].perform_action(action)
                    break

    def handle_card(self, card_id):
        if self.db.is_configuring():
            self.handle_unregistered_card(card_id)
        else:
            card = self.db.get_card(card_id)

            if (card is None):
                self.handle_unregistered_card(card_id)
            else:
                self.handle_registered_card(card)

    def listen(self):
        '''
        Runs on a thread and listens for any nearby RFID card.
        '''
        while True:
            if (self.test_env):
                time.sleep(10)
                self.handle_card('todo_card_id')
            else:
                uid = self.pn532.read_passive_target(timeout=0.5)
                if uid is not None:
                    self.handle_card(str(uid))
