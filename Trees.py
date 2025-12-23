class Tree:
    def __init__(self, Data=None):
        self.Data = Data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.Data is None:
            self.Data = value
            return
        if value == '0':
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        elif value == '1':
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def inorder(self):
        result = ''
        if self.left:
            result += self.left.inorder()
        if self.Data is not None:
            result += self.Data
        if self.right:
            result += self.right.inorder()
        return result


num = int(input("Enter Integer: "))
print("Number: ", num)
binary = bin(num)[2:]
print("Binary: ", binary)
binary = list(binary)

bst = Tree()

if binary[0] == '1':
    for i in binary:
        bst.insert(i)
else:
    for i in range(len(binary)):
        if binary[i] == '1':
            bst.insert(binary[i])
            binary.pop(i)
            break
    for i in binary:
        bst.insert(i)

inorder_result = bst.inorder()
print("Inorder Result: ", inorder_result)

decimal_output = int(inorder_result, 2)
print("Decimal: ", decimal_output)
