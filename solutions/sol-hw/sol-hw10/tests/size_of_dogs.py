test = {
  'name': 'size_of_dogs',
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
          sqlite> SELECT name FROM size_of_dogs WHERE size="toy" OR size="mini";
          abraham
          eisenhower
          fillmore
          grover
          herbert
          """,
        },
      ],
    },
  ]
}