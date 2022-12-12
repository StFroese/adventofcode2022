from tqdm import tqdm

def read_input():
    with open('input.txt', 'r') as f:
        monkeys = [monkey.split('\n')[1:] for monkey in f.read().split('\n\n')]
        monkey_list = []
        for monkey in monkeys:
            starting_items = [int(starting_item) for starting_item in monkey[0].replace(',', '').split(' ') if starting_item.isdigit()]
            operation = [monkey[1].split(' ')[-2], monkey[1].split(' ')[-1]]
            condition = int(monkey[2].split(' ')[-1])
            if_true = int(monkey[3].split(' ')[-1])
            if_false = int(monkey[4].split(' ')[-1])
            monkey_list.append(Monkey(starting_items, operation, condition, if_true, if_false))
    return monkey_list

def test_input():
    with open('test_input.txt', 'r') as f:
        monkeys = [monkey.split('\n')[1:] for monkey in f.read().split('\n\n')]
        monkey_list = []
        for monkey in monkeys:
            starting_items = [int(starting_item) for starting_item in monkey[0].replace(',', '').split(' ') if starting_item.isdigit()]
            operation = [monkey[1].split(' ')[-2], monkey[1].split(' ')[-1]]
            condition = int(monkey[2].split(' ')[-1])
            if_true = int(monkey[3].split(' ')[-1])
            if_false = int(monkey[4].split(' ')[-1])
            monkey_list.append(Monkey(starting_items, operation, condition, if_true, if_false))
    return monkey_list

class Monkey:
    def __init__(self, starting_items, operation, condition, if_true, if_false, modulus=None):
        self.items = starting_items
        self.operator = operation[0]
        self.operand = operation[1]
        try:
            self.operand = int(self.operand)
        except:
            pass
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false
        self.total_inspections = 0
        self.modulus = modulus
        self._operate = self._operate_func()

    def append(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def _operate_func(self):
        if self.operator == '*':
            def foo(item, operand):
                return item * operand
            return foo
        else:
            def foo(item, operand):
                return item + operand
            return foo

    def _throw(self, item):
        if item % self.condition == 0:
            return self.if_true
        else:
            return self.if_false

    def __call__(self):
        throw_items_to = []
        for item_idx, item in enumerate(self.items):
            self.total_inspections += 1
            if self.operand == 'old':
                self.items[item_idx] = self._operate(item, item)
            else:
                self.items[item_idx] = self._operate(item, self.operand)
            if self.modulus is None:
                self.items[item_idx] = int(self.items[item_idx] // 3)
            else:
                self.items[item_idx] = int(self.items[item_idx] % self.modulus)
            throw_items_to.append(self._throw(self.items[item_idx]))

        return throw_items_to

    def __str__(self):
        return f'Items: {self.items}'


class MonkeyManager:
    def __init__(self, monkey_list, do_i_worry=False):
        self.monkey_list = monkey_list
        modulus = 1
        for monkey in monkey_list:
            modulus *= monkey.condition
        if do_i_worry:
            for monkey in monkey_list:
                monkey.modulus = modulus

    def __call__(self):
        for monkey in self.monkey_list:
            throw_items_to = monkey()
            for throw_item_to in throw_items_to:
                self.monkey_list[throw_item_to].append(monkey.pop())

    def __str__(self):
        string = f''
        for monkey_idx, monkey in enumerate(self.monkey_list):
            string += f'Monkey {monkey_idx}:\n\t'
            string += monkey.__str__()
            string += '\n\n'

        return string

    def best_two(self):
        return sorted([monkey.total_inspections for monkey in self.monkey_list])[-2:]

    def best(self):
        return [monkey.total_inspections for monkey in self.monkey_list]

    def best_two_score(self):
        bt = self.best_two()
        return bt[0] * bt[1]

def main():
    input = read_input()


    # part 1
    monkey_manager = MonkeyManager(input)
    for i in range(20):
        monkey_manager()
        print(f'Round {i}:')
        print(monkey_manager)

    print(monkey_manager.best_two_score())

    # part 2
    input = read_input() # it didn't work yesterday because I forgot this line :(
    monkey_manager = MonkeyManager(input, do_i_worry=True)
    for i in tqdm(range(10000)):
        monkey_manager()

    print(monkey_manager.best_two_score())


if __name__ == '__main__':
    main()
