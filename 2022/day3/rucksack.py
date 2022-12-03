from pathlib import Path
from string import ascii_lowercase, ascii_uppercase


def common_item_1(compartment_items):
    """Get the common item in each compartment."""
    common_items = []
    with open(compartment_items, 'r') as f:
        for line in f:
            items = [i for i in line.strip()]
            half = len(items) // 2
            first_half, second_half = items[:half], items[half:]
            common_item = [x for x in first_half if x in second_half]
            common_items.append(common_item[0])
        priority_sum = get_priority(common_items)
    return priority_sum


def common_item_2(compartment_items):
    """Get the common item in each compartment."""
    common_items = []
    with open(compartment_items, 'r') as f:
        lines = f.read().splitlines()
        listsplit = [lines[i:i+3] for i in range(0,len(lines),3)]
        for i in listsplit:
            common_item_first = [x for x in i[0] if x in i[1]]
            common_item = [x for x in common_item_first if x in i[2]]
            common_items.append(common_item[0])
        priority_sum = get_priority(common_items)
    return priority_sum


def get_priority(common_items):
    """Get the priority numbers and sum."""
    lower_case = {v:k for k,v in enumerate(ascii_lowercase, start=1)}
    upper_case = {v:k for k,v in enumerate(ascii_uppercase, start=27)}
    priorities = []
    for item in common_items:
        if item.islower():
            priorities.append(lower_case[item])
        else:
            priorities.append(upper_case[item])
    return sum(priorities)


def main():
    """Main function."""
    compartment_items = Path('compartment_items')
    priority_sum_part_1 = common_item_1(compartment_items)
    print(f'The sum of the priority items is for part 1 is {priority_sum_part_1}.')
    priority_sum_part_2 = common_item_2(compartment_items)
    print(f'The sum of the priority items is for part 2 is {priority_sum_part_2}.')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
