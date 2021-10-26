class BusStop:
    def __init__(self, bus_stop):
        self.name = bus_stop
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return len(self.queue)

    def clear(self):
        self.queue = []