# -*- coding: utf-8 -*-
import random


notes = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B']

major = [0, 2, 4, 5, 7, 9, 11, 0]
blues = [0, 3, 5, 6, 7, 10, 0]
hungarian_minor = [0, 2, 3, 6, 7, 8, 11, 0]
jazz_minor = [0, 2, 3, 5, 7, 9, 11, 0]


def make_scale(starting_note, scale_indexes):
    """Get string of notes representing the desired scale.

    starting_note: A string note.  Examples: 'C♯', 'F'.  Must appear in the
        global `notes` array.
    scale_indexes: List of indexes that make up the scale.  Can also be thought
        of as the distance from the starting note of the scale, in half-tones.
    """
    start_index = notes.index(starting_note)
    all_notes = list(notes)
    all_notes = all_notes[start_index:] + all_notes[:start_index]
    return '  '.join(all_notes[i] for i in scale_indexes)


def main():
    start = random.choice(notes)
    for type_ in ['major', 'blues', 'hungarian_minor', 'jazz_minor']:
        scale_indexes = globals()[type_]
        print type_ + ':'
        print make_scale(start, scale_indexes)


if __name__ == '__main__':
    main()
