test = {
  'name': 'curry-cook',
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
          scm> (curry-cook '(a) 'a)
          (lambda (a) a)
          scm> (curry-cook '(x y) '(+ x y))
          (lambda (x) (lambda (y) (+ x y)))
          scm> (define adder (curry-cook '(x y) '(+ x y)))
          adder
          scm> (eval adder)
          (lambda (x) (lambda (y) (+ x y)))
          scm> (((eval adder) 2) 3)
          5
          """,
          "locked": False,
          "hidden": False
        },
      ],
    },
  ]
}