from __future__ import annotations

values_12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
notes_12 = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D',
            'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']


class Note:

    def __init__(self, letter: str = None, value: int = None):
        """
        Creates a Note based on input
        i.e.
        Note('E')
        Note('C#')
        Note('Cb')

        Note(0) for A
        Note(3) for C
        Note(15) for C

        Possible note values:
        A, A#/Bb, B, C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab
        0    1    2  3    4    5    6    7    8  9    10   11

        internal representation is int [0, 11]
        """
        if value:
            self.value = value % 12
        elif letter:
            self.value = self.letter_to_value(letter)
        else:
            raise ValueError('letter or value needed to create Note')

    def letter_to_value(self, letter) -> int:
        lowered = letter.lower()
        if lowered == 'a':
            return 0
        elif lowered == 'a#' or lowered == 'bb':
            return 1
        elif lowered == 'b':
            return 2
        elif lowered == 'c':
            return 3
        elif lowered == 'c#' or lowered == 'db':
            return 4
        elif lowered == 'd':
            return 5
        elif lowered == 'd#' or lowered == 'eb':
            return 6
        elif lowered == 'e':
            return 7
        elif lowered == 'f':
            return 8
        elif lowered == 'f#' or lowered == 'gb':
            return 9
        elif lowered == 'g':
            return 10
        elif lowered == 'g#' or lowered == 'ab':
            return 11
        else:
            raise ValueError('input note is not valid')

    def n_half_steps_up(self, n: int) -> Note:
        """
        n_half_steps_up returns a Note that is n half steps up from the
        current Note
        n is an int argument
        example usage:
        for note A#, n_half_steps_up(2) should return C
        for note E, n_half_steps_up(8) should return C
        wraps around
        """
        new_value = (self.value + n) % 12
        return Note(value=new_value)

    def half_step_up(self) -> Note:
        """
        half_step_up
        returns a Note that is a half step (or semi-tone) up from the
        current Note
        """
        return self.n_half_steps_up(1)

    def whole_step_up(self) -> Note:
        """
        whole_step_up
        returns a Note that is a whole step (or tone) up from the current Note
        """
        return self.n_half_steps_up(2)

    def minor_2nd_interval_up(self) -> Note:
        return self.n_half_steps_up(1)

    def major_2nd_interval_up(self) -> Note:
        return self.n_half_steps_up(2)

    def minor_3rd_interval_up(self) -> Note:
        return self.n_half_steps_up(3)

    def major_3rd_interval_up(self) -> Note:
        return self.n_half_steps_up(4)

    def perfect_4th_inteval_up(self) -> Note:
        return self.n_half_steps_up(5)

    def diminished_5th_interval_up(self) -> Note:
        return self.n_half_steps_up(6)

    def perfect_5th_inteval_up(self) -> Note:
        return self.n_half_steps_up(7)

    def minor_6th_interval_up(self) -> Note:
        return self.n_half_steps_up(8)

    def major_6th_interval_up(self) -> Note:
        return self.n_half_steps_up(9)

    def minor_7th_interval_up(self) -> Note:
        return self.n_half_steps_up(10)

    def major_7th_interval_up(self) -> Note:
        return self.n_half_steps_up(11)
