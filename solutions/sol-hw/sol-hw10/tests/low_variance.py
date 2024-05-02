test = {
  'name': 'low_variance',
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
          sqlite> SELECT * FROM low_variance;
          curly|1
          """,
        },
      ],
    },
  ]
}