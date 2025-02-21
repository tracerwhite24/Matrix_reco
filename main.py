import random


def heads_or_tails():
    flip = random.choice(["heads", "tails"])
    return flip

result = heads_or_tails()

def importer(result):
    if result == "heads":
        import rando
    else:
        import toep
    import recognizer

print(importer(result))
