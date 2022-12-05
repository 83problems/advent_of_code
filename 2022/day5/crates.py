from pathlib import Path
import sys


def crane_op(stacks):
    """Rearrange the stacks of crates."""
    list_of_all = []
    stack_list = []
    with open(stacks, 'r') as f:
        for line in f:
            x = 4
            for i in range(0, len(line), x):
                try:
                    if line[i:i+x][1].isnumeric():
                        break
                except:
                    break
                crate = line[i:i+x][1]
                stack_list.append(crate)
            x = 0
            list_of_all.append(stack_list)
            stack_list = []
        list_of_all = [i for i in list_of_all if i != []]
        list_of_all = [i for i in list_of_all if i != ['o']]
    x = 0
    reordered_list = []
    while x < 9:
        new_list = []
        new_list.append(extract_elements(list_of_all, x))
        new_list = [i for a,i in enumerate(new_list[0]) if i!=' ']
        reordered_list.append(new_list)
        x += 1
    reordered_lists = move_crates(stacks, reordered_list)
    return reordered_lists


def move_crates(stacks, reordered_list):
    with open(stacks, 'r') as f:
        for line in f:
            if 'move' not in line:
                continue
            to_move = int(line.split(' ')[1])
            stack_from = int(line.split(' ')[3])
            stack_to = int(line.split(' ')[5])
            while to_move > 0:
                from_ele = reordered_list[stack_from - 1][0]
                item_index = reordered_list[stack_from - 1].index(from_ele)
                reordered_list[stack_to -1].insert(0, reordered_list[stack_from - 1].pop(reordered_list[stack_from - 1].index(from_ele)))
                to_move -= 1
    return reordered_list


def extract_elements(lst, num):
    """Redo lists to match cargo stacks."""
    return [item[num] for item in lst]


def main():
    """Main function."""
    stacks = Path('input')
    results = crane_op(stacks)
    #from_ele = reordered_list[stack_from - 1][0]
    answer = ""
    for i in results:
        first_ele = i[0]
        answer += first_ele
    print(f'The crates on top of each stack for part one are {answer}.')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
