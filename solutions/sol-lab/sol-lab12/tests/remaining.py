test = {
  'name': 'remaining',
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
          sqlite> SELECT * FROM remaining;
          10|0
          61A|1800
          61B|800
          61C|540
          70|0
          """,
        },
      ],
    },
  ]
}