from time import sleep

class Stek:
    def __init__(self):
        self.elems=list()

    def add(self, value):
        self.elems.append(value)

    def get(self):
        val=self.elems.pop()
        return val

    def size(self):
        size=len(self.elems)
        return size

queue=Stek()

for i in range(10):
    queue.add(i)
    print(i, end=' ')
print()

for i in range(queue.size()):
    val=queue.get()
    print(val)
    sleep(2)