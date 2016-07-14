class Buffer:
    def __init__(self):
        self.list = []
        self.sum = 0

    def add(self, *a):
        for i in a:
            self.list.append(i)
            self.sum += i
            if len(self.list) == 5:
                print(self.sum)
                self.sum = 0
                self.list.clear()

    def get_current_part(self):
        return self.list

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()

