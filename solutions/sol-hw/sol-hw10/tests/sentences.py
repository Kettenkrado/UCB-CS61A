test = {
  'name': 'sentences',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read hw10.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM sentences;
          The two siblings, barack and clinton, have the same size: standard
          The two siblings, abraham and grover, have the same size: toy
          """,
        },
      ],
    },
  ]
}