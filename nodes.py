class Node:
    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __repr__(self):
        return f'{self.id}: {self.content}'

