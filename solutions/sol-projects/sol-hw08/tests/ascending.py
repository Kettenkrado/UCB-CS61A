test = {
  'name': 'ascending?',
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
          scm> (ascending? '(1 2 3 4 5))  ; #t or #f
          #t
          """,
        },
        {
          'code': r"""
          scm> (ascending? '(1 5 2 4 3))  ; #t or #f
          #f
          """,
        },
        {
          'code': r"""
          scm> (ascending? '(2 2))  ; #t or #f
          #t
          """,
        },
        {
          'code': r"""
          scm> (ascending? '(1 2 2 4 3))  ; #t or #f
          #f
          """,
        },
        {
          'code': r"""
          scm> (ascending? '())  ; #t or #f
          #t
          """,
        },
      ],
    },
  ]
}