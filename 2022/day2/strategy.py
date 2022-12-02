from pathlib import Path

def calculate_first_score(cheat_guide):
    """Calculate the first score based on the cheat guide"""
    points = {'A': 1, 'B': 2, 'C': 3}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}

    score = []
    with open(cheat_guide, 'r') as f:
        for line in f:
            results = {}
            results[line[0]] = line[2]
            draws = all((draw.get(k) == v for k, v in results.items()))
            loses = all((lose.get(k) == v for k, v in results.items()))

            if loses:
                score.append(0)
            elif draws:
                score.append(3)
            else:
                score.append(6)
            score.append(points[line[0]])
    return sum(score)


def calculate_second_score(cheat_guide):
    """Calculate the second score based on the cheat guide"""
    points = {'X': 1, 'Y': 2, 'Z': 3}
    win = {'C': 'X', 'B': 'Z', 'A': 'Y'}
    lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}

    score = []
    with open(cheat_guide, 'r') as f:
        for line in f:
            results = {}
            results[line[0]] = line[2]
            if line[2] == 'X':
                score.append(0)
                find_loss = lose[line[0]]
                score.append(points[find_loss])
            elif line[2] == 'Y':
                score.append(3)
                find_draw = draw[line[0]]
                score.append(points[find_draw])
            else:
                score.append(6)
                find_win = win[line[0]]
                score.append(points[find_win])
    return sum(score)


def main():
    """Main function."""
    cheat_guide = Path('cheat_guide')
    first_score_total = calculate_first_score(cheat_guide)
    print(f'The total score if using the guide is {first_score_total}')
    second_score_total = calculate_second_score(cheat_guide)
    print(f'The total score if using the guide is {second_score_total}')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
