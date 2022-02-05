import matchers

class QueryBuilder:
  def __init__(self, matchers = [], matcher = matchers.All()):
    self._matchers = matchers
    self._matchers.append(matcher)

  def playsIn(self, team):
    return QueryBuilder(self._matchers, matchers.PlaysIn(team))

  def hasAtLeast(self, value, attr):
    return QueryBuilder(self._matchers, matchers.HasAtLeast(value, attr))

  def hasFewerThan(self, value, attr):
    return QueryBuilder(self._matchers, matchers.HasFewerThan(value, attr))

  def all(self):
    return QueryBuilder(self._matchers, matchers.All())

  def build(self):
    return matchers.And(*self._matchers)