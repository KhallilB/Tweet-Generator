from linkedlist import LinkedList

class Queue(LinkedList):

    def __init__(self, size, items=None):
        LinkedList.__init__(self, items=items)
        self.limit = size

    def enqueue(self, item):
        length = self.length()
        if length < self.limit:
            self.append(item)
        else:
            head = self.head.data
            self.delete(head)
            self.append(item)

    def dequeue(self):
        item = None
        length = self.length()
        if length == 0:
            raise IndexError
        else:
            item = self.head.data
            self.delete(item)
        return item


def test_queue():
    queue = Queue(size=3)
    print('queue: {}'.format(queue))

    print('\nTesting enqueue:')
    for item in ['A', 'B', 'C', 'D', 'E', 'F']:
        print('enqueue({!r})'.format(item))
        queue.enqueue(item)
        print('queue: {}'.format(queue))

    print('head: {}'.format(queue.head))
    print('tail: {}'.format(queue.tail))
    print('length: {}'.format(queue.length()))

    # Enable this after implementing dequeue method
    dequeue_implemented = True
    if dequeue_implemented:
        print('\nTesting dequeue:')
        for n in range(queue.length()):
            item = queue.dequeue()
            print('dequeue({!r})'.format(item))
            print('queue: {}'.format(queue))

        print('head: {}'.format(queue.head))
        print('tail: {}'.format(queue.tail))
        print('length: {}'.format(queue.length()))


if __name__ == '__main__':
    test_queue()