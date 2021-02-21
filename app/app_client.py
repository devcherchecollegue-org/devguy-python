class AppClient():
    def __init__(self, bot_client):
        self._bot_client = bot_client

    def start(self):
        self._bot_client.start()
