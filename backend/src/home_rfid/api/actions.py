import bottle

from ..db import HomeRFIDDB
from ..modules import modules


@bottle.route('/api/list_actions')
def list_actions():
    '''
    Return any actions that can be run.
    '''
    args = dict(bottle.request.query.decode())
    configured = args.get('configured', "false") == "true"

    if configured:
        db = HomeRFIDDB()
        return {
            'actions': db.get_configured_actions()
        }
    else:
        return {
            'actions': [
                {
                    'module': module['module_id'],
                    'actions': module['module'].get_actions()
                }
                for module in modules
            ]
        }
