class Heap:
    def __init__(self, elements):
        self.elements = elements
        self.heaped = None

    def build_heap(self):
        if self.elements is None:
            return

        self.heaped = [i for i in self.elements]
        for i in range(len(self.heaped) - 1, 0, -1):
            self.heapify(i)

        return self.heaped

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heaped) and self.heaped[left] < self.heaped[smallest]:
            smallest = left

        if right < len(self.heaped) and self.heaped[right] < self.heaped[smallest]:
            smallest = right

        if smallest != i:
            self.heaped[smallest], self.heaped[i] = self.heaped[i], self.heaped[smallest]
            self.heapify(smallest)

if __name__ == '__main__':
    arr = [1, 5, 6, 8, 9, 7, 3]
    heap = Heap(arr).build_heap()
    print(heap)
