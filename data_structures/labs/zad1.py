class Queue:
    def __init__(self):
        self.incoming = []
        self.outgoing = []

    def enqueue(self, value):
        self.incoming.append(value)

    def dequeue(self):
        if len(self.outgoing) == 0:
            while len(self.incoming) > 0:
                self.outgoing.append(self.incoming.pop(-1))

        return self.outgoing.pop(-1) if len(self.outgoing) > 0 else None


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
