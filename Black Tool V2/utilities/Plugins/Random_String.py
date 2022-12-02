import random, json, string

def generate_random_string(Ammount):
    string_returned = "".join(
        random.choice(string.ascii_letters) for i in range(0, Ammount)
    )
    return string_returned

json = {"content": generate_random_string(20)}