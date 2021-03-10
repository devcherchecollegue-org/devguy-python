from app.shared.event.event import Event


class InMemoryEventLogger():
    def __init__(self):
        self.events = []

    async def on_receive_event(self, event):
        self.events.append(event)

    @staticmethod
    def subscribed_to():
        return [Event]
