class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Checks if there are any nodes in the queue.
    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)

        # If our queue is empty, set both
        # front and rear to new_node.
        if self.is_empty():
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        # Store removed node
        removed = self.front

        # Advance front node
        self.front = self.front.next

        # If front node advanced to None
        # we don't have any nodes left.
        if self.front is None:
            self.rear = None

        return removed.value


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
