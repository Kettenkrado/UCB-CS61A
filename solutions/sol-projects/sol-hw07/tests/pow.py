test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (pow 2 5)
          32
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (pow 10 3)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (pow 3 3)
          27
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (pow 1 100000000000000) ; make sure this doesn't run forever!
          1
          """,
          'hidden': False,
          'locked': False
        },
      ],
    },
  ]
}