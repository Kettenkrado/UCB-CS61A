(define (over-or-under num1 num2) 
  (if (>= num1 num2)
      (if (> num1 num2)
          1
          0)
      -1)
)
; if version

(define (over-or-under num1 num2) 
  (cond ((> num1 num2) 1)
        ((= num1 num2) 0)
        (else -1))
)
; cond version

(define (make-adder num) 
  (define (adder inc)
    (+ num inc))
  adder
)

(define (composed f g) 
  (define (compute x)
    (f (g x)))
  compute
)

(define (repeat f n) 
  (define (repeat-on x)
    (if (> n 0) ((repeat f (- n 1))(f x)) x))
  repeat-on
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (or (zero? a) (zero? b))

      (if (zero? a) b a)

      (let ((r (modulo (max a b) (min a b))))
        (gcd r (min a b))
      )
  )
)
