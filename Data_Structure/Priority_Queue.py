class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return index * 2 + 1
    
    def right_child(self, index):
        return index * 2 + 2
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def _heapify_down(self, index):
        size = len(self.heap)
        smallest = index

        left_index = self.left_child(index)
        right_index = self.right_child(index)

        if left_index < size and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index < size and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        return self.heap[0] if self.heap else None

    def print_heap(self):
        print(self.heap)


class PriorityQueue:
    def __init__(self):
        self.min_heap = MinHeap()

    def add(self, val):
        self.min_heap.insert(val)

    def remove(self):
        return self.min_heap.extract_min()

    def peek(self):
        return self.min_heap.peek()

    def print_queue(self):
        self.min_heap.print_heap()
