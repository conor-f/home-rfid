import bottle

from ..db import HomeRFIDDB


@bottle.route('/api/set_is_configuring')
def set_is_configuring():
    '''
    Return any actions that can be run.
    '''
    db = HomeRFIDDB()
    db.set_is_configuring(True)

    return {}


@bottle.post('/api/set_next_card')
def set_next_card():
    '''
    Sets the next card to be actions.
    '''
    print(dict(bottle.request.forms))

    return {}
