test = {
  'name': 'repeatedly-cube',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': """
          scm> (repeatedly-cube 3 1)
          1
          scm> (repeatedly-cube 2 2)
          512
          scm> (repeatedly-cube 3 2)
          134217728
          """,
          'hidden': False,
          'locked' : False
        },
      ]
    }
  ]
}