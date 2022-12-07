from pathlib import Path


def fix_comms_1(message):
    with open(message, 'r') as f:
        input = f.read()
        for i in range(4, len(input)):
            ulist = set(input[i-4:i])
            if len(ulist) == 4:
                return i


def fix_comms_2(message):
    with open(message, 'r') as f:
        input = f.read()
        for i in range(14, len(input)):
            ulist = set(input[i-14:i])
            if len(ulist) == 14:
                return i


def main():
    """Main function."""
    message = Path('input')
    packet_marker = fix_comms_1(message)
    print(f'The start of the packet marker is {packet_marker}.')
    message_marker = fix_comms_2(message)
    print(f'The start of the packet marker is {message_marker}.')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
