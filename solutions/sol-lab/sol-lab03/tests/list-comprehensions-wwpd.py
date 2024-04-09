test = {
  'name': 'Comprehensions',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> [2 * x for x in range(4)]
          [0, 2, 4, 6]
          >>> [y for y in [6, 1, 6, 1] if y > 2]
          [6, 6]
          >>> [[1] + s for s in [[4], [5, 6]]]
          [[1, 4], [1, 5, 6]]
          >>> [z + 1 for z in range(10) if z % 3 == 0]
          [1, 4, 7, 10]
          """
        }
      ]
    }
  ]
}