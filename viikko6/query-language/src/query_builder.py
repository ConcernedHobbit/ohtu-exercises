from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, Or, And, Not

class QueryBuilder:
  def __init__(self, matchers = [], matcher = None, combiner = And):
    self._combiner = combiner
    self._matchers = matchers

    if matcher:
      self._matchers.append(matcher)

  def playsIn(self, team):
    return QueryBuilder(
      self._matchers, 
      PlaysIn(team),
      self._combiner
    )

  def hasAtLeast(self, value, attr):
    return QueryBuilder(
      self._matchers, 
      HasAtLeast(value, attr),
      self._combiner
    )

  def hasFewerThan(self, value, attr):
    return QueryBuilder(
      self._matchers, 
      HasFewerThan(value, attr),
      self._combiner
    )

  def all(self):
    return QueryBuilder(
      self._matchers, 
      All(),
      self._combiner
    )

  def oneOf(self, *matchers):
    return QueryBuilder(
      [*matchers],
      None,
      Or
    )

  def build(self):
    matchers = self._matchers[:]
    self._matchers.clear()

    if len(matchers) == 0:
      return All()

    if len(matchers) == 1:
      return matchers[0]

    return self._combiner(*matchers)