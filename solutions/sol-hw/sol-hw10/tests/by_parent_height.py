test = {
  'name': 'by_parent_height',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'ordered': True,
      'setup': """
      sqlite> .read hw10.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM by_parent_height;
          herbert
          fillmore
          abraham
          delano
          grover
          barack
          clinton
          """,
        },
      ],
    },
  ]
}