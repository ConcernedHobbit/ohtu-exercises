import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
  def get_players(self):
    return [
      Player("Selänne", "WPG", 62, 8),
      Player("Kurri", "EDM", 50, 5),
      Player("Koivu", "MTL", 8, 1),
      Player("Jokinen", "LA", 0, 6),
      Player("Tikkanen", "EDM", 12, 0)
    ]

class TestStatistics(unittest.TestCase):
  def setUp(self):
    self.statistics = Statistics(
      PlayerReaderStub()
    )

  def test_search_returns_player(self):
    player = self.statistics.search("Selänne")

    self.assertEqual(player.name, "Selänne")
    self.assertEqual(player.team, "WPG")
    self.assertAlmostEqual(player.goals, 62)
    self.assertAlmostEqual(player.assists, 8)

  def test_searching_nonexistant_returns_none(self):
    self.assertIsNone(self.statistics.search("Donskoi"))

  def test_team_returns_list_of_players(self):
    players = self.statistics.team("EDM")

    self.assertEqual(len(players), 2)
    self.assertIsInstance(players[0], Player)
    self.assertIsInstance(players[1], Player)

    self.assertEqual(players[0].team, "EDM")
    self.assertEqual(players[1].team, "EDM")

    self.assertIn(players[0].name, ["Kurri", "Tikkanen"])

  def test_top_scorers(self):
    top_scorers = self.statistics.top_scorers(2)

    self.assertEqual(len(top_scorers), 3)
    self.assertIsInstance(top_scorers[0], Player)
    self.assertIsInstance(top_scorers[1], Player)
    self.assertIsInstance(top_scorers[2], Player)
    
    self.assertGreaterEqual(
      top_scorers[0].points, 
      top_scorers[1].points
    )

    self.assertGreaterEqual(
      top_scorers[1].points,
      top_scorers[2].points
    )