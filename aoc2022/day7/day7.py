def read_input():
    with open('input.txt', 'r') as f:
        line = [line.split(' ') for line in f.read().split('\n')[:-1]]
    return line

def test_input():
    with open('test_input.txt', 'r') as f:
        line = [line.split(' ') for line in f.read().split('\n')[:-1]]
    return line

class Tree:
    def __init__(self, root, parent_tree=None):
        self.root = root
        self.parent_tree = parent_tree
        self.children = {}

    def add_child(self, key, child):
        self.children[key] = child

    def size(self):
        return sum([self.children[child_key].size() if isinstance(self.children[child_key], Tree) else int(self.children[child_key]) for child_key in self.children.keys()])

    def size_list(self, list_to_fill):
        for child_key in self.children.keys():
            if isinstance(self.children[child_key], Tree):
                list_to_fill.append(self.children[child_key].size())
                self.children[child_key].size_list(list_to_fill)



class TreeBuilder:
    def __init__(self, tree):
        self.tree = tree

    def fill_tree(self, cmd):
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    self.tree = self.tree.parent_tree
                else:
                    self.tree = self.tree.children[cmd[2]]
        else:
            if cmd[0] == 'dir':
                self.tree.add_child(cmd[1], Tree(cmd[1], self.tree))
            else:
                self.tree.add_child(cmd[1], cmd[0])

        return self.tree




def main():
    input = read_input()

    # part 1
    tree = Tree(input[0][2])
    tree_builder = TreeBuilder(tree)

    trees = [tree_builder.fill_tree(cmd) for cmd in input[1:]]
    dir_size_list = []
    tree.size_list(dir_size_list)
    dir_sizes_filtered = [size for size in dir_size_list if size <= 100000]
    print(sum(dir_sizes_filtered))

    # part 2
    unused_space = 70000000 - tree.size()
    dir_sizes_filtered = [size for size in dir_size_list if size >= (30000000 - unused_space)]
    if dir_sizes_filtered == []:
        print(tree.size())
    else:
        print(min(dir_sizes_filtered))


if __name__ == '__main__':
    main()
