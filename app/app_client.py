from domain.event.message_received_event import MessageReceivedEvent


class AppClient:
    def __init__(self, bot_client, event_bus):
        self._bot_client = bot_client
        self.event_bus = event_bus

        self.event_bus.subscribe(self)

    def start(self):
        self._bot_client.run()

    async def on_receive_event(self, event):
        if isinstance(event, MessageReceivedEvent):
            print("yolo")

    @staticmethod
    def subscribed_to():
        return [MessageReceivedEvent]
