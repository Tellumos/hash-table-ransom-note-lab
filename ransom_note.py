def can_construct(ransomNote: str, magazine: str) -> bool:

    letters = {}

    for letter in magazine:
        letters[letter] = letters.get(letter, 0) + 1

    for letter in ransomNote:
        if not ((letter in letters) and (letters.get(letter, 0) != 0)):
            return False
        letters[letter] = letters.get(letter, 0) - 1
    
    return True