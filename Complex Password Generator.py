import random
import string


# No words involved, just random characters
def simple_create(max_pass_length, lowercase_only, numbers, symbols):

    char_list = string.ascii_letters

    if lowercase_only:
        char_list = string.ascii_lowercase
    if numbers:
        char_list += string.digits
    if symbols:
        char_list += string.punctuation

    password = ''.join(random.choice(char_list) for _ in range(max_pass_length))
    return password


# Words are involved
def complex_create(max_pass_length, lowercase_only, numbers, symbols):

    # Gets all the english words
    import nltk
    nltk.download("words")
    all_words = nltk.corpus.words.words()

    # Groups them by length
    lengths = {}
    for word in all_words:
        word_length = len(word)
        if word_length not in lengths:
            lengths[word_length] = []
        lengths[word_length].append(word)

    # Declaring variables as their types
    password = ''
    char_list = []

    # Adding to the character list
    if numbers:
        char_list += string.digits
    if symbols:
        char_list += string.punctuation

    max_word_length = max_pass_length

    # Iterates while still has missing characters
    while len(password) < max_pass_length:

        # Longest words are 24 characters long
        # If the remaining characters are too long, then we set the max to 24
        if (0 > max_word_length - len(password)) or (max_word_length - len(password)) > 24:
            max_word_length = 24

        # There are two modes: pasting random characters or pasting a word
        paste_random_characters = random.choice([True, False])

        # This only applies if there are numbers and/or symbols in the character list
        if len(char_list) > 0:
            if paste_random_characters:
                # Here we use the max_pass_length because we don't care about word length limitations
                selected_rnd_char_length = random.randint(1, max_pass_length - len(password))
                for _ in range(selected_rnd_char_length):
                    password += random.choice(char_list)

        # This only applies if it's only words (empty character list) or if it's word pasting mode
        elif paste_random_characters is False or len(char_list) < 0:
            selected_word_length = random.randint(1, max_word_length)
            pick_word = random.choice(lengths[selected_word_length])
            password += str(pick_word)

    if lowercase_only:
        password = password.lower()

    return password


def generate_password(max_pass_length, lowercase_only, numbers, symbols, words=False):

    if words:
        password = complex_create(max_pass_length, lowercase_only, numbers, symbols)

    else:
        password = simple_create(max_pass_length, lowercase_only, numbers, symbols)
    return password


def main():
    length = int(input("Select characters: "))
    lowercase = bool(input("Lowercase? [Boolean]: "))
    numbers = bool(input("Numbers? [Boolean]:"))
    symbols = bool(input("Symbols? [Boolean]:"))
    words = bool(input("Include words? [Boolean]: "))
    final_password = generate_password(length, lowercase, numbers, symbols, words)
    print(final_password)


if __name__ == "__main__":
    main()
