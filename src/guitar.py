from note import Note


class Guitar:
    num_strings: int = 6
    num_frets: int

    def __init__(self, num_frets: int = 17):
        """
        Creates an instance of Guitar
        with optionally specified num_strings and num_frets

        Functionality exists only for standard tuning: E, A, D, G, B, E
        """
        self.num_frets = num_frets

    def locate_note(self, note: Note):
        """
        locate_note locates the input note on each string

        Parameters
        ----------
        note : Note
        """
        pass
