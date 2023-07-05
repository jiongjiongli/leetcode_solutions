from typing import List


# The game Babylon is a two-player alternating-moves game - like tic-tac-toe, or chess, or go. It's played with twelve tiles: three each of four colors.

# The tiles start out in 12 stacks of height 1.
# A move consists of combining two stacks: putting one whole stack on top of another.
# You are allowed to combine two stacks if either the heights match, or the top tile colors match.
# You win if you are the last player to move. You lose if it's your turn and there are no moves.

MAX_STACK_HEIGHT = 12


class Stack:
    def __init__(self, color, height, count):
        self.color = color
        self.height = height
        self.count = count

class Group:
    def __init__(self):
        self.stacks = []
        self.stack_counts = [0] * MAX_STACK_HEIGHT
        self.next_group = None

    def add_stack(self, stack):
        self.stacks.append(stack)
        self.stack_counts[stack.height - 1] += stack.count

    def encode(self):
        status = 0
        bit_value = 1

        for height_index, stack_count in enumerate(self.stack_counts):
            if height_index < 6:
                # 0 <= stack_count <= 3, so encode with 2 bits
                assert 0 <= stack_count <= 3

                if stack_count in [1, 3]:
                    status = (status | bit_value)

                bit_value = (bit_value << 1)

                if stack_count in [2, 3]:
                    status = (status | bit_value)

                bit_value = (bit_value << 1)
            else:
                # 0 <= stack_count <= 1, so encode with 1 bits
                assert 0 <= stack_count <= 1

                if stack_count == 1:
                    status = (status | bit_value)

                bit_value = (bit_value << 1)

        return status

    def get_avilable_stacks(self):
        stacks = [(height_index, stack_count)
                   for height_index, stack_count in enumerate(self.stack_counts)
                   if stack_count > 0]

        return stacks

    def decrease_stack(self, height_index):
        self.stack_counts[height_index] -= 1

    def increase_stack(self, height_index):
        self.stack_counts[height_index] += 1


class ActionNode:
    def __init__(self, content=None):
        self.content = content
        self.is_first_player = None
        self.is_winner = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_path(self, level=0):
        if self.is_first_player:
            assert self.is_winner
            print('=' * 20)
            print('{}: First Player Win'.format(level))
            print('-' * 20)
            print(self.content)
            print('=' * 20)

            if self.children:
                lose_children = [child for child in self.children if not child.is_winner]

                assert lose_children

                lose_children[0].print_path(level + 1)

        if (not self.is_first_player):
            assert not self.is_winner
            print('=' * 20)
            print('{}: Second Player Lose'.format(level))
            print('-' * 20)
            print(self.content)
            print('=' * 20)

            for child in self.children:
                assert child.is_winner
                child.print_path(level + 1)

class BabylonGame:
    def __init__(self, stacks):
        self.stacks = stacks
        self.status_memory = {}
        self.status_memory_action_node = {}

    def find_winner(self):
        groups = self.stacks_to_groups(self.stacks)
        action_root = ActionNode()

        is_winner = self.process(groups, True, 0, action_root)

        action_root.print_path()

        winner_name = 'First Player' if is_winner else 'Second Player'

        return winner_name

    def stacks_to_groups(self, stacks):
        group_dict = {}

        for stack in stacks:
            color = stack.color
            height = stack.height
            count = stack.count

            group = group_dict.get(color)

            if group is None:
                group = group_dict[color] = Group()

            group.add_stack(stack)

        groups = list(group_dict.values())

        return groups

    def encode(self, groups):
        group_status_list = []

        for group in groups:
            group_status = group.encode()

            group_status_list.append(group_status)

        group_status_list.sort()
        return tuple(group_status_list)

    def get_actions(self, groups):
        move_actions = []

        for first_index, first_group in enumerate(groups):
            for second_index, second_group in enumerate(groups):
                if first_index == second_index:
                    # In group actions
                    actions = self.get_in_group_actions(first_group, first_index)
                else:
                    # Out group actions
                    actions = self.get_out_group_actions(first_group,
                                                         first_index,
                                                         second_group,
                                                         second_index)
                move_actions.extend(actions)

        return move_actions

    def get_in_group_actions(self, group, group_index):
        actions = []

        stacks = group.get_avilable_stacks()

        for first_index in range(len(stacks)):
            first_height_index, first_stack_count = stacks[first_index]

            for second_index in range(first_index + 1, len(stacks)):
                second_height_index, second_stack_count = stacks[second_index]

                # Stack first:      (group index, hight, count)
                # on top of second: (group index, hight, count)
                action = {
                     'first': (group_index,  first_height_index,  first_stack_count),
                    'second': (group_index, second_height_index, second_stack_count),
                    'new': (group_index,
                            first_height_index + second_height_index + 1,
                            first_stack_count + second_stack_count)
                }

                actions.append(action)

        return actions

    def get_out_group_actions(self,
                              first_group,
                              first_index,
                              second_group,
                              second_index):
        actions = []

        first_stacks = first_group.get_avilable_stacks()
        second_stacks = second_group.get_avilable_stacks()

        for first_height_index, first_stack_count in first_stacks:
            for second_height_index, second_stack_count in second_stacks:
                if first_height_index != second_height_index:
                    continue

                # Stack first:      (group index, hight, count)
                # on top of second: (group index, hight, count)
                action = {
                     'first': (first_index,   first_height_index,  first_stack_count),
                    'second': (second_index, second_height_index, second_stack_count),
                    'new': (first_index,
                            first_height_index + second_height_index + 1,
                            first_stack_count + second_stack_count)
                }

                actions.append(action)

        return actions

    def get_next_groups(self, groups, action):
        # Stack first:      (group index, hight, count)
        # on top of second: (group index, hight, count)
        first_index,   first_height_index,  first_stack_count = action['first']
        second_index, second_height_index, second_stack_count = action['second']


        first_group = groups[first_index]
        second_group = groups[second_index]

        first_group.decrease_stack(first_height_index)
        second_group.decrease_stack(second_height_index)

        new_height_index = first_height_index + second_height_index + 1
        first_group.increase_stack(new_height_index)

        return groups

    def recover_groups(self, groups, action):
        # Reverse stack first: (group index, hight, count)
        #    on top of second: (group index, hight, count)
        first_index,   first_height_index,  first_stack_count = action['first']
        second_index, second_height_index, second_stack_count = action['second']

        first_group = groups[first_index]
        second_group = groups[second_index]

        new_height_index = first_height_index + second_height_index + 1
        first_group.decrease_stack(new_height_index)

        first_group.increase_stack(first_height_index)
        second_group.increase_stack(second_height_index)
        return groups

    def process(self, groups, is_first_player, depth, action_node):
        action_node.is_first_player = is_first_player
        status = self.encode(groups)
        is_winner = self.status_memory.get(status)

        if is_winner is not None:
            action_node.is_winner = is_winner
            action_node.children = self.status_memory_action_node[status].children

            return is_winner

        actions = self.get_actions(groups)

        for action in actions:
            child_node = ActionNode(action)
            action_node.add_child(child_node)

            next_groups = self.get_next_groups(groups, action)
            is_winner = self.process(next_groups, not is_first_player, depth + 1, child_node)

            groups = self.recover_groups(next_groups, action)

            if not is_winner:
                self.status_memory[status] = True
                action_node.is_winner = True
                self.status_memory_action_node[status] = action_node
                return True

        self.status_memory[status] = False
        action_node.is_winner = False
        self.status_memory_action_node[status] = action_node
        return False


def main():
    stacks = [ Stack('yellow', 1, 3),
               Stack('white', 1, 3),
               Stack('green', 1, 3),
               Stack('black', 1, 3)
             ]

    game = BabylonGame(stacks)
    winner_name = game.find_winner()

    print(winner_name)

if __name__ == '__main__':
    main()
