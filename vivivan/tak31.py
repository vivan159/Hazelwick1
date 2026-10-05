import random


number = random.randint(1, 6)


number_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six"
}

word = number_words[number]


print(f"I generated the number {word}")