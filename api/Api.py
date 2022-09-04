# Filename: Api.py
# Created By: Mackenly Jones on 07/12/2022
# Web: mackenly.com
# Twitter: @mackenlyjones

from api.Action import Action
from api.Tally import Tally
from api.Media import Media


class Api:
    """
    Api class contains the various methods to handle routes to the API
    """

    def __init__(self, switcher):
        """
        Initialize the api class.
        :param switcher: the switcher object that we're getting the tally from.
        """
        self.switcher = switcher
        self.tally = Tally(self.switcher)
        self.media = Media(self.switcher)
        self.action = Action(self.switcher)

    def get(self, path, passphrase=None, ip=None):
        """
        Handle a GET request to the API.
        :param ip: ip of the ATEM
        :param passphrase: passphrase to compare requests to
        :param path: the url path of the request.
        :return: dict - the response to the request.
        """

        # if path ends in /, remove it
        if path[-1] == '/':
            path = path[:-1]

        # process the path, trigger the correct method
        if path == '' or path == '/model':
            return {
                'model': self.switcher.atemModel,
            }
        elif '/connection' in path:
            if path == '/connection/ping' or path == '/connection':
                return {
                    'connected': self.switcher.waitForConnection(infinite=False),
                    'model': self.switcher.atemModel,
                }
        elif '/tally' in path:
            if path == '/tally':
                return self.tally.get_all()
            elif '/tally' in path and len(path) > 6 and path[7:].isnumeric() and int(path[7:]) in range(1, self.switcher.tally.channelConfig.tallyChannels + 1):
                return self.tally.get(int(path[7:]))
            elif path == '/tally/program':
                return self.tally.get_program()
            elif path == '/tally/preview':
                return self.tally.get_preview()
        elif '/media' in path:
            if path == '/media':
                return self.media.get_media()
        return {
                "error": "invalid request",
            }

    def post(self, path, passphrase=None, ip=None):
        """
        Handle a POST request to the API.
        :param ip: ip of the ATEM
        :param passphrase: passphrase to compare requests to
        :param path: the url path of the request.
        :return: dict - the response to the request.
        """

        # if path ends in /, remove it
        if path[-1] == '/':
            path = path[:-1]

        # process the path, trigger the correct method
        if path == '':
            return {
                'model': self.switcher.atemModel,
            }
        elif '/action' in path:
            """
                Paths in /action are currently untested.
            """
            if path == '/action':
                return {
                    'error': 'No action specified.',
                }
            elif '/action/ftb' in path and len(path) > 11:
                params = path[12:].split('/')
                self.action.set_me(int(params[0]))
                return self.action.ftb()
            elif '/action/cut' in path and len(path) > 11:
                params = path[12:].split('/')
                self.action.set_me(int(params[0]))
                if len(params) > 1:
                    return self.action.cut(int(params[1]))
                else:
                    return self.action.cut()
            elif '/action/auto' in path and len(path) > 12:
                params = path[13:].split('/')
                self.action.set_me(int(params[0]))
                if len(params) > 1:
                    return self.action.auto(int(params[1]))
                else:
                    return self.action.auto()
            elif '/action/preview' in path and len(path) > 15:
                params = path[16:].split('/')
                self.action.set_me(int(params[0]))
                return self.action.preview(int(params[1]))
            elif '/action/program' in path and len(path) > 15:
                params = path[16:].split('/')
                self.action.set_me(int(params[0]))
                return self.action.program(int(params[1]))
            elif '/action/dsk/cut' in path and len(path) > 15:
                params = path[16:].split('/')
                return self.action.dsk_cut(int(params[0]))
            elif '/action/dsk/tie' in path and len(path) > 15:
                params = path[16:].split('/')
                return self.action.dsk_tie(int(params[0]))
        elif '/media' in path:
            if '/media/' in path and '/loop' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_loop(int(params[0]), params[2])
            elif '/media/' in path and '/playing' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_playing(int(params[0]), params[2])
            elif '/media/' in path and '/beginning' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_beginning(int(params[0]), params[2])
            elif '/media/' in path and '/frame' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_frame(int(params[0]), params[2])
            elif '/media/' in path and '/type' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_type(int(params[0]), params[2])
            elif '/media/' in path and '/still' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_still(int(params[0]), params[2])
            elif '/media/' in path and '/clip' in path and len(path) > 12:
                params = path[7:].split('/')
                return self.media.set_clip(int(params[0]), params[2])
        return {
                "error": "invalid request",
            }
