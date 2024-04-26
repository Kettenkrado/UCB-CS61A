test = {
  'name': 'repeat-lambda',
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
          scm> (repeat (+ 2 3) (print 1))
          1
          1
          1
          1
          1
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': r"""
          scm> (repeat 2 (repeat 2 (print 'four)))
          four
          four
          four
          four
          """,
          'hidden': False,
          'locked' : False
        },
      ],
    },
  ]
}