class DiscordClientStub():
    def __init__(self, event_bus):
        self.is_start = False
        self._event_bus = event_bus

    def run(self):
        self.is_start = True

    async def trigger_event(self, event):
        await self._event_bus.publish(event)
