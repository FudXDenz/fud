
import utils

def add_note(content):
    if not utils.validate_note(content):
        raise ValueError('Note cannot be empty')
    note_id = len(NOTES) + 1
    NOTES.append(Node(note_id, content))

class Node:
    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __repr__(self):
        return f'{self.id}: {self.content}'


NOTES = []

def add_note(content):
    note_id = len(NOTES) + 1
    NOTES.append(Node(note_id, content))

def list_notes():
    return NOTES

def delete_note(note_id):
    global NOTES
    NOTES = [n for n in NOTES if n.id != note_id]

