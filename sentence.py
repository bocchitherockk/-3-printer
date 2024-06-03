from character import Character

class Sentence:
    def __init__(
        self,
        sentence: str,
        space_seperation: int = 10
    ) -> None:
        if not isinstance(sentence, str):
            raise Exception(f"sentence '{sentence}' should be a string")
        if not isinstance(space_seperation, int) or space_seperation < 0:
            raise Exception(f"space_seperation '{space_seperation}' should be a positive integer")

        self.sentence: str = sentence.upper()
        self.space_seperation: int = space_seperation

        self.characters: list[Character] = []
        for i in self.sentence:
            if i == ' ':
                self.characters.append(Character.get_space_object(space_seperation))
            elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                self.characters.append(Character.get_character_object(i))
            else:
                raise Exception(f"character '{i}' is not supported")
        self.height = max(character.height for character in self.characters if character != None)
        self.__adjust_characters_heights()

    """
    this function corrects the characters height in the same sentence to have the same height, including spaces
    smaller characters will be aligned to the bottom (the top will be filled with spaces)
    note: the same character can have different heights in different sentences
    """
    def __adjust_characters_heights(self) -> None:
        for character in self.characters:
            if character != None:
                character.parts = [' ' * character.width] * (self.height - character.height) + character.parts
                character.height = self.height
                # character.parts = [' ' * character.width] * self.pre_line_padding + character.parts + [' ' * character.width] * self.post_line_padding

    def __str__(self) -> str:
        return '\n'.join(''.join(i) for i in list(zip(*[character.parts for character in self.characters])))
