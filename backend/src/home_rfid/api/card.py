import bottle

from ..db import HomeRFIDDB


@bottle.route('/api/list_cards')
def list_cards():
    '''
    Return the Cards registered and their associated actions.
    '''
    db = HomeRFIDDB()

    return {
        'cards': db.list_cards()
    }


@bottle.post('/api/get_card')
def get_card(card_id):
    '''
    Return the Card object.
    '''
    db = HomeRFIDDB()

    print(f"Getting card: {card_id}")

    args = dict(bottle.request.query.decode())
    card_id = args.get('card_id', None)

    return db.get_card(card_id)


@bottle.post('/api/add_card')
def add_card():
    '''
    Configure a card with an ID to have actions specified in the body.
    '''
    db = HomeRFIDDB()
    print('configuring card....')

    card_name = bottle.request.json.get('card_name', 'Sample Name')
    actions = bottle.request.json.get('actions', [])

    print(f'ACTIONS: {actions}')
    db.add_card('UNSET_CARD_ID', card_name, actions)
    db.set_is_configuring(True)

    return {
        'todo': 'todo'
    }
