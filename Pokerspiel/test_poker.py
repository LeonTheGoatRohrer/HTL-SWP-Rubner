import unittest
from Kartenansicht import Karte, bewertung  # ggf. Namen anpassen


def k(farbe, wert):
    """Kürzere Karten-Erstellung"""
    return Karte(farbe, wert, "X")


class TestPoker(unittest.TestCase):

    def test_royal_flush(self):
        hand = [
            k("Herz", 10), k("Herz", 11),
            k("Herz", 12), k("Herz", 13), k("Herz", 14)
        ]
        self.assertEqual(bewertung(hand), "Royal Flush")

    def test_straight_flush(self):
        hand = [k("Pik", w) for w in [5,6,7,8,9]]
        self.assertEqual(bewertung(hand), "Straight Flush")

    def test_four_of_a_kind(self):
        hand = [k("Karo", 7), k("Herz", 7), k("Pik", 7), k("Kreuz",7), k("Herz",2)]
        self.assertEqual(bewertung(hand), "Four of a Kind")

    def test_full_house(self):
        hand = [k("Herz",9), k("Pik",9), k("Kreuz",9), k("Karo",5), k("Herz",5)]
        self.assertEqual(bewertung(hand), "Full House")

    def test_flush(self):
        hand = [k("Karo", w) for w in [2,4,7,9,12]]
        self.assertEqual(bewertung(hand), "Flush")

    def test_straight(self):
        # A straight must use mixed suits; one suit would be a straight flush.
        hand = [k(farbe, wert) for farbe, wert in zip(
            ["Kreuz", "Herz", "Pik", "Karo", "Kreuz"], [3, 4, 5, 6, 7]
        )]
        self.assertEqual(bewertung(hand), "Straight")

    def test_three_of_a_kind(self):
        hand = [k("Herz",4), k("Pik",4), k("Karo",4), k("Kreuz",8), k("Herz",9)]
        self.assertEqual(bewertung(hand), "Three of a Kind")

    def test_two_pair(self):
        hand = [k("Herz",10), k("Pik",10), k("Kreuz",8), k("Karo",8), k("Herz",3)]
        self.assertEqual(bewertung(hand), "Two Pair")

    def test_one_pair(self):
        hand = [k("Herz",11), k("Karo",11), k("Pik",7), k("Herz",4), k("Kreuz",2)]
        self.assertEqual(bewertung(hand), "One Pair")

    def test_high_card(self):
        hand = [k("Herz",2), k("Karo",5), k("Pik",7), k("Kreuz",9), k("Herz",12)]
        self.assertEqual(bewertung(hand), "High Card")


if __name__ == "__main__":
    unittest.main()
