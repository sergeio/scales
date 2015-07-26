import random


notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
blues = [0, 3, 5, 6, 7, 10, 0]


def make_scale(starting_note, scale_indexes):
    start_index = notes.index(starting_note)
    all_notes = list(notes)
    all_notes = notes[start_index:] + notes[:start_index]
    return '  '.join(all_notes[i] for i in scale_indexes)


def main():
    start = random.choice(notes)
    print make_scale(start, blues)


if __name__ == '__main__':
    main()
