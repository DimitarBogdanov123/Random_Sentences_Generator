import random


def print_random_word(words):
    return random.choice(words)


names = ["Stanimir", "Joan", "Mariana", "Dimitar"]
places = ["Yambol", "v.Botevo", "Sofia", "Kargon"]
verbs = ["eats", "play with", "move on", "going to"]
nouns = ["laptop", "apple", "bikes", "car"]
adverbs = ["slowly", "hardly", "angrily", "sadly"]
details = ["at home", "in the water", "in the park", "from home"]

print("Hello, this is your first random sentence:")
while True:
    random_name = print_random_word(names)
    random_places = print_random_word(places)
    random_verbs = print_random_word(verbs)
    random_nouns = print_random_word(nouns)
    random_adverbs = print_random_word(adverbs)
    random_details = print_random_word(details)
    print(f"{random_name} from {random_places} {random_adverbs} {random_verbs} {random_nouns}")
    print("Click [Enter] to generate a new one.")
    exit()
