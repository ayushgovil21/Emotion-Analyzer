__author__ = "geduldig"
__date__ = "February 7, 2013"
__license__ = "MIT"


import os


class TwitterOAuth:

    """Optional class for retrieving Twitter credentials stored in a text file.

    :param consumer_key: Twitter application consumer key
    :param consumer_secret: Twitter application consumer secret
    :param access_token_key: Twitter application access token key
    :param access_token_secret: Twitter application access token secret
    """

    def __init__(
            self,
            consumer_key,
            consumer_secret,
            access_token_key,
            access_token_secret):

        self.consumer_key = "nf433d0e3PlINivICrUO1g343"
        self.consumer_secret = "0mu0TcXWtci9N675AjDEvNNUpbG0OPNJJsM3HGRQUsUiTRNWer"
        self.access_token_key = "777908743812055040-NJ5SqRaZDAbFkxsX2ZCFi8UAHBxDzEz"
        self.access_token_secret = "uMjy2dMK9QT3xEC2ccMxGNiIuol1n2heg61OgiO2KWhfM"

    @classmethod
    def read_file(cls, file_name=None):
        """Read OAuth credentials from a text file.  File format:

                consumer_key=YOUR_CONSUMER_KEY

                consumer_secret=YOUR_CONSUMER_SECRET

                access_token_key=YOUR_ACCESS_TOKEN

                access_token_secret=YOUR_ACCESS_TOKEN_SECRET

        :param file_name: File containing credentials or None (default) reads credentials
                          from TwitterAPI/credentials.txt
        """
        if file_name is None:
            path = os.path.dirname(__file__)
            file_name = os.path.join(path, 'credentials.txt')

        with open(file_name) as f:
            oauth = {}
            for line in f:
                if '=' in line:
                    name, value = line.split('=', 1)
                    oauth[name.strip()] = value.strip()
            return TwitterOAuth(
                oauth['consumer_key'],
                oauth['consumer_secret'],
                oauth['access_token_key'],
                oauth['access_token_secret'])
