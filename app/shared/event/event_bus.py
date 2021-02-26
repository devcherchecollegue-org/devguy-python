class EventBus():
    def __init__(self):
        self._subscribers = {}

    async def publish(self, event):
        event_classes = [x for x in list(
            map(lambda x: x.__name__, type(event).mro())) if x != 'object']

        subscribers = []
        for event_class in event_classes:
            if not event_class in self._subscribers.keys():
                continue
            subscribers += self._subscribers[event_class]

        if not subscribers:
            return

        for subscriber in subscribers:
            await subscriber.on_receive_event(event)

    def subscribe(self, subscriber):
        subscribed_events = list(
            map(lambda event_class: event_class.__name__, subscriber.subscribed_to()))

        for event_class_name in subscribed_events:
            if not event_class_name in self._subscribers.keys():
                self._subscribers[event_class_name] = []

            self._subscribers[event_class_name].append(subscriber)
