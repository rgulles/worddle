import random

WORDS = {
    "easy": {
        "list": ['noon', 'fire', 'echo'],
        "riddles": {
            'noon': "What 4-letter word can be written forward, backward or upside down, and can still be read from left to right?",
            'fire': "I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?",
            'echo': "What can't talk but will reply when spoken to?"
        }
    },

    "normal": {
        "list": ['towel', 'piano', 'clock'],
        "riddles": {
            'towel': "What gets wet while drying?",
            'piano': "What has many keys but can't open a single lock?",
            'clock': "What has hands, but can't clap?"
        }
    },

    "hard": {
        "list": ['candle', 'shadow', 'puzzle'],
        "riddles": {
            'candle': "I'm tall when I'm young, and short when I'm old. What am I?",
            'shadow': "I follow you all the time and copy your every move, but you can't touch me or catch me. What am I?",
            'puzzle': "I can be cracked, made, told, and played. What am I?"
        }
    }
}

def get_random_word_data(difficulty="easy"):
    data = WORDS[difficulty]

    word = random.choice(data["list"])
    riddle = data["riddles"][word]
    letters = [letter.upper() for letter in word]

    return word, riddle, letters