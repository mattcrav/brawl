import unittest
from brawl import Game, Card


class TestBrawl(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    # 11 players on offense and defense
    def test_player_count(self):
        self.assertEqual(len(self.game.offense.players), 11)
        self.assertEqual(len(self.game.defense.players), 11)

    # Each has a deck of cards
    def test_deck_size(self):
        for p in self.game.offense.players:
            self.assertGreater(len(p.deck), 1)
        for p in self.game.defense.players:
            self.assertGreater(len(p.deck), 1)

    # Cards are played in 4 x 3 grid of zones
    def test_field_size(self):
        # 4 regions
        self.assertEqual(len(self.game.field.grid), 4)
        # 3 columns (Left, Middle, Right)
        for c in self.game.field.grid:
            self.assertEqual(len(c), 3)

    # Trying to win zones by having the highest total on cards played
    def test_field_cards(self):
        o = self.game.offense.players[0]
        d = self.game.defense.players[0]
        z = self.game.field.grid[0][0]
        z.append(o.deck.pop())
        z.append(d.deck.pop())
        o_tot = sum([x.value for x in z if x.team == self.game.offense])
        d_tot = sum([x.value for x in z if x.team == self.game.defense])
        self.assertIsInstance(o_tot, int)
        self.assertIsInstance(d_tot, int)

    # X marks starting position of play, no cards are played here
    def test_field_start(self):
        for r in self.game.field.grid:
            for c in r:
                o = self.game.offense.players[0]
                if self.game.field.play(o.deck.pop(), c):
                    self.assertEqual(len(c), 1)
                else:
                    self.assertEqual(c, 'X')

    # 3 basic cards available
    def test_card_types(self):
        self.assertIn('Strength', Card.types)
        self.assertIn('Agility', Card.types)
        self.assertIn('Focus', Card.types)
        self.assertIsNotNone(Card(self.game.offense, 'Strength'))
        with self.assertRaises(ValueError):
            Card(self.game.offense, 'Not Valid')

    # Strength flat value.
    def test_card_strength(self):
        c = Card(self.game.offense, 'Strength')
        v = c.value
        c.roll()
        self.assertEqual(c.value, v)

    # Agility range of possible values that are rolled   
    def test_card_agility(self):
        c = Card(self.game.offense, 'Agility')
        c.roll()
        self.assertIsInstance(c.value, int)
        self.assertGreaterEqual(c.value, c.low)
        self.assertLessEqual(c.value, c.high)

    # Focus flat value.
    def test_card_focus(self):
        c = Card(self.game.offense, 'Focus')
        v = c.value
        c.roll()
        self.assertEqual(c.value, v)

    # Each Round represents a 3 play series.
    def test_game_round(self):
        self.assertIsNone(self.game.round)
        self.assertIsNone(self.game.play)
        self.game.start_round()
        self.assertEqual(self.game.round, 1)
        self.assertEqual(self.game.play, 1)
        play_count = 0
        while self.game.round == 1:
            self.game.run_play()
            play_count += 1
        self.assertEqual(self.game.round, 2)
        self.assertEqual(self.game.play, 1)
        self.assertEqual(play_count, 3)

    # Each round begins by drawing 3 cards for each player.
    def test_game_draw(self):
        for o in self.game.offense.players:
            self.assertEqual(len(o.hand), 0)  
        for d in self.game.defense.players:
            self.assertEqual(len(d.hand), 0)  
        self.game.start_round()
        for o in self.game.offense.players:
            self.assertEqual(len(o.hand), 3)  
        for d in self.game.defense.players:
            self.assertEqual(len(d.hand), 3)  


if __name__ == '__main__':
    unittest.main()