# -*- coding: utf-8 -*-
import random
import optparse


USAGE = """%prog [options] [KEY] ...

Print some scales!

KEY         Starting note of scales.  If omitted, make random.
"""


notes = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B']

major = [0, 2, 4, 5, 7, 9, 11, 0]
even = [0, 2, 4, 6, 8, 10, 0]
blues = [0, 3, 5, 6, 7, 10, 0]
hungarian_minor = [0, 2, 3, 6, 7, 8, 11, 0]
jazz_minor = [0, 2, 3, 5, 7, 9, 11, 0]


def main():
    options, args, _ = parse_options()
    start = args[0] if args else random.choice(notes)
    if not options.all_types:
        print make_scale(start, globals()[options.scale_type])
    else:
        print make_all_types(start)


def make_all_types(starting_note):
    """Return a string representing all supported types of scales."""
    _, _, parser = parse_options()
    output = []
    for scale_type in parser.get_option('--scale-type').choices:
        output.append(scale_type + ':')
        output.append(make_scale(starting_note, globals()[scale_type]))
    return '\n'.join(output)


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


def parse_options():
    parser = optparse.OptionParser(USAGE)
    parser.add_option(
        '-a', '--all-types', dest='all_types', action='store_true')
    parser.add_option('-s', '--scale-type', dest='scale_type', metavar='STYPE',
        choices=['major', 'even', 'blues', 'hungarian_minor', 'jazz_minor'],
        default='blues',
        help='Selects the type of scale to output.  Default is %default',
    )
    options, args = parser.parse_args()
    return options, args, parser


if __name__ == '__main__':
    main()
