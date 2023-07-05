## Enqueue, dequeue and peek operations after implementing a queue.

class Queue:
    def __init__(self):
        self.queue =[]

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} is added to the given queue")
        
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"{item} is removed from the queue")
            return item
        else:
            print("The given queue is empty can't perform dequeue operation")
            return None
        
    def peek(self):
        if not self.is_empty():
            top_item = self.queue[0]
            print(f"{top_item} is the top item of the queue")
            return top_item
        else:
            print("The given queue is empty can't perform dequeue operation")
            return None
        
    def is_empty(self):
        return len(self.queue) == 0
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
q.dequeue()
q.peek()