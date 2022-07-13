# Filename: Api.py
# Created By: Mackenly Jones on 07/12/2022
# Web: mackenly.com
# Twitter: @mackenlyjones

from api.Tally import Tally


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

    def get(self, path):
        """
        Handle a GET request to the API.
        :param path: the url path of the request.
        :return: dict - the response to the request.
        """

        # if path ends in /, remove it
        if path[-1] == '/':
            path = path[:-1]

        # process the path, trigger the correct method
        if path == '/' or path == '/model':
            print('/')
            return {
                'model': self.switcher.atemModel,
            }
        elif path == '/tally':
            return self.tally.get_all()
        elif '/tally' in path and len(path) > 6 and path[7:].isnumeric() and int(path[7:]) in range(1, self.switcher.tally.channelConfig.tallyChannels + 1):
            return self.tally.get(int(path[7:]))
        elif path == '/tally/program':
            return self.tally.get_program()
        elif path == '/tally/preview':
            return self.tally.get_preview()
        else:
            return {
                'error': 'invalid request',
            }
