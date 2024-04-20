test = {
  'name': 'my-filter',
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
          scm> (my-filter even? '(1 2 3 4))
          (2 4)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (my-filter odd? '(1 3 5))
          (1 3 5)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (my-filter odd? '(2 4 6 1))
          (1)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (my-filter even? '(3))
          ()
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (my-filter odd? nil)
          ()
          """,
          'hidden': False
        },
      ]
    },
    {
      'scored': True,
      'setup': """
      scm> (define filter nil)
      scm> (load-all ".")
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (my-filter even? '(1 2 3 4)) ; checks you dont use builtin filter
          (2 4)
          """,
          'hidden': False
        }
      ]
    }
  ]
}