import threading

class TreeNode():
    def __init__(self, value, branches = []):
        self.value = value
        self.branches = []
        for value in branches:
            self.branches.append(TreeNode(value))
    
    def get_leaves(self, leaves):
        if len(self.branches) == 0:
            leaves.append(self.value)
            return
        
        for branch in self.branches:
            branch.get_leaves(leaves)
    
    def blink(self):
        if len(self.branches) > 0:
            for branch in self.branches:
                branch.blink()
        else:
            if self.value == '0':
                self.branches.append(TreeNode('1'))
            elif (len(self.value) % 2) == 0:
                split = int(len(self.value) / 2)
                self.branches.append(TreeNode(str(int(self.value[0:split]))))
                self.branches.append(TreeNode(str(int(self.value[split:]))))
            else:
                self.value = str(int(self.value) * 2024)

class MultiThreadedStoneObserver():
    def __init__(self, input_string):
        self.stones_tree_observers = self.parse_input(input_string)
    
    def run_obsevers_in_parallel(self, blink_count = 1):
        threads = []
        for stone_tree_observer in self.stones_tree_observers:
            t = threading.Thread(target=stone_tree_observer.blink, args=(blink_count,))
            threads.append(t)
            t.start()
        for thread in threads:
            thread.join()
        
        #print("All threads finished")
        
        total = 0
        for i, stone_tree_observer in enumerate(self.stones_tree_observers):
            #print("stone tree observer result", i, stone_tree_observer.get_stone_count())
            total += stone_tree_observer.get_stone_count()
        
        #print("Result", total)
        return total
    
    def parse_input(self, input_string):
        stone_observers = []
        for i, input in enumerate(input_string.split(" ")):
            stone_observers.append(StoneObserver(input, i))
        return stone_observers

class StoneObserver():
    def __init__(self, input_string, id = ''):
        self.id = id
        self.stones_tree = self.parse_input(input_string)
    
    def blink(self, blink_count = 1):
        for i in range(blink_count):
            #print(f'{self.id} Blink', i)
            self.stones_tree.blink()
            self.stones_tree = TreeNode('Root', self.get_current_stones())
    
    def get_stone_count(self):
        return len(self.get_current_stones())
    
    def get_current_stones(self):
        leaves = []
        self.stones_tree.get_leaves(leaves)
        return leaves
    
    def parse_input(self, input_string):
        return TreeNode('root', input_string.split(" "))
    
    def get_leaves(self, root, leaves):
        if len(root.branches) == 0:
            leaves.append(root.value)
            return
        
        for branch in root.branches:
            self.get_leaves(branch, leaves)
    
    def tree_to_matrix(self, root, row, col, height, ans):
        if not root:
            return

        # Calculate offset for child positions
        offset = 2 ** (height - row - 1)

        # Traverse the left subtree
        if len(root.branches) > 1:
            self.tree_to_matrix(root.branches[0], row + 1, col - offset, 
                    height, ans)

        # Place the current node's value in the matrix
        ans[row][col] = str(root.value)

        # Traverse the right subtree
        if len(root.branches) > 1:
            self.tree_to_matrix(root.branches[1], row + 1, col + offset, 
                    height, ans)
    
    def print_tree(self, root):
        height = self.get_height(root) 
        rows = height + 1
        cols = 2 ** (height + 1) - 1
        tree_matrix = [["" for _ in range(cols)] for _ in range(rows)]
        self.tree_to_matrix(root, 0, (cols - 1) // 2, height, tree_matrix)
        for row in tree_matrix:
            for cell in row:
                if cell == "":
                    print(" ", end="")
                else:
                    print(cell, end="")
            print()
    
    def get_height(self, root):
        if len(root.branches) < 1:
            return 0
        branch_heights = list(map(self.get_height, root.branches))
        return max(branch_heights) + 1

class DictionaryStoneObserver():
    def __init__(self, input_string, id = ''):
        self.id = id
        self.stones = self.parse_input(input_string)
    
    def parse_input(self, input_string):
        stones = {}
        for input in input_string.split(" "):
            stones[input] = 1
        return stones

    def get_stone_count(self, stones):
        total = 0
        for stone_count in stones.values():
            total += stone_count
        return total
    
    def observe_stones(self, blink_count = 1):
        return self.blink(blink_count, self.stones)
    
    def upsert_into_dict(self, stone_id, stone_count, stone_dict):
        if stone_id not in stone_dict:
            stone_dict[stone_id] = stone_count
        else:
            stone_dict[stone_id] = stone_dict[stone_id] + stone_count
    
    def blink(self, blink_count, stones):
        if blink_count == 0:
            return self.get_stone_count(stones)
        
        new_stones = {}
        
        for stone_id in stones:
            stone_count = stones[stone_id]
            if stone_id == '0':
                self.upsert_into_dict('1', stone_count, new_stones)
            elif (len(stone_id) % 2) == 0:
                split = int(len(stone_id) / 2)
                self.upsert_into_dict(str(int(stone_id[0:split])), stone_count, new_stones)
                self.upsert_into_dict(str(int(stone_id[split:])), stone_count, new_stones)
            else:
                self.upsert_into_dict(str(int(stone_id) * 2024), stone_count, new_stones)
        
        return self.blink(blink_count - 1, new_stones)
        

