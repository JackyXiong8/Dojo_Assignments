
class card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class deck_class(object):
    def __init__(self):
        suit = ["spades", "diamonds", "hearts", "cloves"]
        self.cards = []
        for x in range(0, 13):
            for i in suit:
                self.cards.append(card(i,x))


deck1 = deck_class()
print (deck1.cards)

print (len(deck1.cards))

print (deck1.cards[0,1].value)


