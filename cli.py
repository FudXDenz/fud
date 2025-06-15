import argparse

def main():
    parser = argparse.ArgumentParser(description='Note Manager CLI')
    parser.add_argument('--add', help='Add a note')
    parser.add_argument('--list', action='store_true', help='List notes')
    parser.add_argument('--delete', type=int, help='Delete note by ID')
    args = parser.parse_args()

if __name__ == '__main__':
    main()

