import argparse
import threading

import bottle

from ..api import *


@bottle.route('/<:re:.*>', method='OPTIONS')
def enable_cors_generic_route():
    """
    This route takes priority over all others. So any request with an OPTIONS
    method will be handled by this function.

    See: https://github.com/bottlepy/bottle/issues/402

    NOTE: This means we won't 404 any invalid path that is an OPTIONS request.
    """
    add_cors_headers()


@bottle.hook('after_request')
def enable_cors_after_request_hook():
    """
    This executes after every route. We use it to attach CORS headers when
    applicable.
    """
    add_cors_headers()


def add_cors_headers():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE'
    bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--port',
        dest='port',
        default=8081
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        dest='debug'
    )
    parser.add_argument(
        '--reloader',
        action='store_true',
        dest='reloader'
    )
    args = parser.parse_args()

    bottle.debug(args.debug)
    run_config = {
        'host': '0.0.0.0',
        'port': args.port,
        'debug': args.debug,
        'reloader': args.reloader
    }

    bottle.run(
        **run_config
    )


if __name__ == '__main__':
    main()
