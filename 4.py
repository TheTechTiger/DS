from collections import deque

class EventSystem:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)

    def process_next(self):
        if self.queue:
            event = self.queue.popleft()
            print(f"Processing event: {event}")
        else:
            print("No events to process.")

    def display_pending(self):
        print("Pending Events:", list(self.queue))

    def cancel_event(self, event):
        try:
            self.queue.remove(event)
            print(f"Canceled event: {event}")
        except ValueError:
            print("Event not found or already processed.")

# Usage
es = EventSystem()
es.add_event("E1")
es.add_event("E2")
es.display_pending()
es.process_next()
es.cancel_event("E2")
es.display_pending()