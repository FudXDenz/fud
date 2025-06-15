
import nodes

def main():
    parser = argparse.ArgumentParser(description='Note Manager CLI')
    parser.add_argument('--add', help='Add a note')
    parser.add_argument('--list', action='store_true', help='List notes')
    parser.add_argument('--delete', type=int, help='Delete note by ID')
    args = parser.parse_args()

    if args.add:
        nodes.add_note(args.add)
        print('Note added.')
    elif args.list:
        for n in nodes.list_notes():
            print(n)
    elif args.delete:
        nodes.delete_note(args.delete)
        print('Note deleted.')

