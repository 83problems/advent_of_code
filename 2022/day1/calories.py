from pathlib import Path


def food_carried(food_list):
    elf_food = []
    total_calories = []
    with open(food_list, 'r') as f:
        for line in f:
            if not line.strip():
                total = additup(elf_food)
                total_calories.append(total)
                elf_food = []
            else:
                elf_food.append(line.strip())
    total_calories.sort()
    top3 = sum(total_calories[-3:])
    return max(total_calories), top3


def additup(elf_food):
    elf_food = [int(i) for i in elf_food]
    total = sum(elf_food)
    return total


def main():
    """Main function."""
    food_list = 'food'
    food_list_path = Path(food_list)
    most_calories, top3 = food_carried(food_list_path)
    print(f'The most calories carried is {most_calories}')
    print(f'The top three total calories carried is {top3}')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
