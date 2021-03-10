from event import Event


class EventLogger():
    def __init__(self):
        pass

    async def on_receive_event(self, event):
        print("Received event", type(event).__name__)

    @staticmethod
    def subscribed_to():
        return [Event]
