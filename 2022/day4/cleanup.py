from pathlib import Path


def first_dupe_assignments(assignments):
    """Find duplicate assignments part 1."""
    with open(assignments, 'r') as f:
        dupes = 0
        for line in f:
            item1, item2 = line.split(',')
            beg_range1, end_range1 = item1.split('-')
            beg_range2, end_range2 = item2.split('-')
            if int(beg_range1) <= int(beg_range2) and int(end_range1) >= int(end_range2):
                dupes += 1
            elif int(beg_range2) <= int(beg_range1) and int(end_range2) >= int(end_range1):
                dupes += 1
    return dupes


def second_dupe_assignments(assignments):
    """Find duplicate assignments part 2."""
    with open(assignments, 'r') as f:
        dupes = 0
        for line in f:
            item1, item2 = line.split(',')
            beg_range1, end_range1 = item1.split('-')
            beg_range2, end_range2 = item2.split('-')
            first_set = set([*range(int(beg_range1), int(end_range1) + 1)])
            second_set = set([*range(int(beg_range2), int(end_range2) + 1)])
            if first_set.intersection(second_set):
                dupes += 1
    return dupes


def main():
    """Main function."""
    assignments = Path('assignments')
    first_dupes = first_dupe_assignments(assignments)
    print(f'The number of duplicate assignments are {first_dupes}.')
    second_dupes = second_dupe_assignments(assignments)
    print(f'The number of duplicate assignments are {second_dupes}.')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
