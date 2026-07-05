class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def get_count(self):
        return self.count


counter = Counter()
counter.increase()
counter.increase()
counter.increase()

print(f"현재 클릭 수: {counter.get_count()}")
