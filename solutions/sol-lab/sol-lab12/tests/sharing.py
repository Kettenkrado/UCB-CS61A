test = {
  'name': 'sharing',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab12.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM sharing;
          61A|3
          61B|2
          61C|2
          70|1
          """,
        },
      ],
    },
  ]
}