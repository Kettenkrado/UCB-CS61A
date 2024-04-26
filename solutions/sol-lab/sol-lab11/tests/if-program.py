test = {
  'name': 'if-program',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'setup': r"""
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': r"""
          scm> (define expr (if-program '(= 0 0) '2 '3))
          expr
          scm> (eval expr)
          2
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': r"""
          scm> (define expr2 (if-program '(= 1 0) '(print 3) '(print 5)))
          expr2
          scm> (eval expr2)
          5
          """,
          'hidden': False,
          'locked' : False
        }
      ],
    },
  ]
}