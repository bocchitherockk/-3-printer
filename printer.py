import os
from character import Character
from sentence import Sentence

class Printer:
    def __init__(
        self,
        position: str = 'start',
        character_seperation: int = 2,
        space_seperation: int = 10,
        pre_line_padding: int = 1,
        post_line_padding: int = 1
    ) -> None:

        if position not in ['start', 'center', 'end']:
            raise Exception(f"position '{position}' should be in ('start', 'center', or 'end')")
        if not isinstance(character_seperation, int) or character_seperation < 0:
            raise Exception(f"character_seperation '{character_seperation}' should be a positive integer")
        if not isinstance(space_seperation, int) or space_seperation < 0:
            raise Exception(f"space_seperation '{space_seperation}' should be a positive integer")
        if not isinstance(pre_line_padding, int) or pre_line_padding < 0:
            raise Exception(f"pre_line_padding '{pre_line_padding}' should be a positive integer")
        if not isinstance(post_line_padding, int) or post_line_padding < 0:
            raise Exception(f"post_line_padding '{post_line_padding}' should be a positive integer")

        self.position = position
        self.character_seperation = character_seperation
        self.space_seperation = space_seperation
        self.pre_line_padding = pre_line_padding
        self.post_line_padding = post_line_padding

    def add_character_seperation(self, sentence: Sentence) -> None:
        for i in range(len(sentence.characters) - 1):
            sentence.characters.insert(i * 2 + 1, Character('\n'.join([' ' * self.character_seperation] * sentence.height)))

    def align_sentence(self, sentence: Sentence, position: str, terminal_width: int, sentence_length: int) -> None:
        if position == 'start':
            return
        if position == 'center':
            sentence.characters.insert(0, Character('\n'.join([' ' * ((terminal_width - sentence_length) // 2)] * sentence.height)))
        if position == 'end':
            sentence.characters.insert(0, Character('\n'.join([' ' * (terminal_width - sentence_length)] * sentence.height)))

    def print(self, sentence: str, position: str = None):
        if position == None:
            position = self.position
        if not isinstance(sentence, str):
            raise Exception(f"sentence '{sentence}' should be a string")
        if position not in ['start', 'center', 'end']:
            raise Exception(f"position '{position}' should be in ('start', 'center', or 'end')")

        terminal_width = os.get_terminal_size(0).columns
        sentence_obj = Sentence(sentence = sentence, space_seperation = self.space_seperation)
        self.add_character_seperation(sentence_obj)

        sentence_to_string = str(sentence_obj)
        sentence_length = len(sentence_to_string.split('\n')[0])

        if sentence_length > terminal_width:
            raise Exception(f"width of '{sentence}' = {sentence_length} surpasses the terminal width ({terminal_width})")

        self.align_sentence(sentence_obj, position, terminal_width, sentence_length)
        sentence_to_string = str(sentence_obj)

        for _ in range(self.pre_line_padding):
            print()
        print(sentence_to_string)
        for _ in range(self.post_line_padding):
            print()