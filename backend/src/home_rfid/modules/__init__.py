from .homeassistant import HomeAssistantModule
from .spotify import SpotifyModule

modules = [
    {
        'module_id': 'homeassistant',
        'module': HomeAssistantModule()
    },
    {
        'module_id': 'spotify',
        'module': SpotifyModule()
    },
]

print('Modules loaded.')
