test = {
  'name': 'The Truth Will Prevail',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> True and 13
          13
          >>> False or 0
          0
          >>> not 10
          False
          >>> not None
          True
          """,
        },
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> True and 1 / 0  # If this errors, just type Error.
          Error
          >>> True or 1 / 0  # If this errors, just type Error.
          True
          >>> -1 and 1 > 0 # If this errors, just type Error.
          True
          >>> -1 or 5
          -1
          >>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
          1
          """,
        },
        {
          'code': """
          >>> print(3) or ""
          3
          ''
          """,
          'multiline': True,
        },
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> def f(x):
          ...     if x == 0:
          ...         return "zero"
          ...     elif x > 0:
          ...         return "positive"
          ...     else:
          ...         return ""
          >>> 0 or f(1)
          'positive'
          >>> f(0) or f(-1)
          'zero'
          >>> f(0) and f(-1)
          ''
          """,
        },
      ]
    },
  ]
}