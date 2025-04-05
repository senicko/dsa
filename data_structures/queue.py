class Queue:
    def __init__(self, default_size=16):
        self.queue = [None] * default_size
        self.max_size = default_size
        self.size = 0
        self.head = 0

    # Enqueues the item to the queue.
    def enqueue(self, item):
        if self.size == self.max_size:
            self.double_size()
            self.enqueue(item)
            return

        self.queue[self.head + self.size] = item
        self.size += 1

    # Dequeues an item from the queue array.
    def dequeue(self):
        if self.size == 0:
            raise Exception("queue underflow")

        item = self.queue[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item

    # Doubles in size the queue array.
    def double_size(self):
        self.max_size *= 2
        new = [None] * self.max_size

        for i in range(self.size):
            new[i] = self.queue[(self.head + i) % self.size]

        self.head = 0


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
