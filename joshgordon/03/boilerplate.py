class AdventOfCode:

    def __enter__(self):
        self.f = open("input.txt", "r")
        self.data = self.f.read().strip()
        self.array = self.data.split("\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __contains__(self, value):
        return value in self.array
