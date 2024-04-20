test = {
  'name': 'gcd',
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
          scm> (gcd 24 60)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (gcd 1071 462)
          21
          """,
          'hidden': False,
          'locked': False
        }
      ],
    },
  ]
}