class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def update_tree(self, key):
        pass

    def display_tree(self, root):
        # print(root.left.left.val)
        # pivot = self
        # print("check 1")
        # if type(self.left) == Node:
        #     print("Yes in class I'm", self.left.val)
        # print("check 2")
        pass
    
    def insert_key(self, root, key):
        # Insert key by traversing left and right child in order.
        # Maintain a queue for pivot points to check its children
        q = []
        q.append(root)

        while(len(q)):
            pivot = q.pop(0)

            # Check left child of pivot
            if not pivot.left:
                pivot.left = Node(key)
                break
            else:
                q.append(pivot.left)
            
            # Check right child of pivot
            if not pivot.right:
                pivot.right = Node(key)
                break
            else:
                q.append(pivot.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.right = Node(5)
    root.insert_key(root, 8)
    print(root.left.left.val)
