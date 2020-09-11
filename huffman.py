class HuffmanNode(object):
    def __init__(self, val=None, left=None, right=None, letter=None):
        self.val, self.left, self.right = val, left, right
        self.letter = letter
        self.code = ''

    def __repr__(self):
        return str(self.val)


class PriorityQueue(object):
    def __init__(self, *args, **kwargs):
        self.queue = []

    def put(self, val):
        self.queue.append(val)

    def get(self):
        if self.queue != []:
            return self.queue.pop(self.queue.index(min(self.queue, key=lambda x: x.val)))
        else:
            return None

    def __repr__(self):
        return str(sorted(self.queue, key=lambda x: x.val))


class HuffmanCoding(object):
    def __init__(self, *args, **kwargs):
        self.Tree = None
        self.queue = PriorityQueue()
        self.Table = {}

    def createTable(self, root, code=''):
        if root.left != None:
            code += '0'
            self.createTable(root.left, code)

        if root.letter != None:
            root.code = code
            self.Table[root.letter] = code

        if root.right != None:
            code += '1'
            self.createTable(root.right, code)

    def encode(self, message):
        self.message = message

        for i in set(message):
            self.queue.put(HuffmanNode(val=message.count(i), letter=i))

        while len(self.queue.queue) > 1:
            left, right = self.queue.get(), self.queue.get()
            temp = HuffmanNode(val=left.val + right.val, left=left, right=right)
            self.queue.put(temp)
        self.Tree = temp
        self.createTable(self.Tree)


message = 'ABBBBAACAADDDCAACBAABBBC'

huff = HuffmanCoding()
huff.encode(message)
print(huff.Table) #Output -> {'A': '0', 'D': '0100', 'C': '01001', 'B': '0101'}
