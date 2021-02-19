class DiscordClient():
    def __init__(self, client, bot_secret_key):
        self._client = client
        self._bot_secret_key = bot_secret_key

    def run(self):
        self._client.run(self._bot_secret_key)
