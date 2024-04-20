test = {
  'name': 'What Would Scheme Display?',
  'points': 0,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      """,
      'cases': [
        {
          'code':"""
          scm> (- 10 4)
          6
          scm> (* 7 6)
          42
          scm> (+ 1 2 3 4)
          10
          scm> (/ 8 2 2)
          2
          scm> (quotient 29 5)
          5
          scm> (modulo 29 5)
          4
          """,
        },
        {
          'code': """
          scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
          #f
          scm> (< 1 3)
          #t
          scm> (or 1 #t)                  ; or special form short circuits
          1
          scm> (and #t #f (/ 1 0))
          #f
          scm> (not #t)
          #f
          """,
        },
        {
          'code': """
          scm> (define x 3)
          x
          scm> x
          3
          scm> (define y (+ x 4))
          y
          scm> y
          7
          scm> (define x (lambda (y) (* y 2)))
          x
          scm> (x y)
          14
          """,
        },
        {
          'code': """
          scm> (if (not (print 1)) (print 2) (print 3))
          1
          3
          scm> (* (if (> 3 2) 1 2) (+ 4 5))
          9
          scm> (define foo (lambda (x y z) (if x y z)))
          foo
          scm> (foo 1 2 (print 'hi))
          hi
          2
          scm> ((lambda (a) (print 'a)) 100)
          a
          """,
        }
      ]
    }
  ]
}