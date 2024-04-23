(define (ascending? s) 
  (if (or (null? s) (null? (cdr s))) 
      true
      (and (<= (car s) (car (cdr s)))
           (ascending? (cdr s)))
  )
)

(define (my-filter pred s) 
  (if (null? s) 
      nil
      (append 
              (if (pred (car s))
              (list (car s))
              nil)
              (my-filter pred (cdr s)))
  )
)

(define (interleave lst1 lst2) 
  (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else         (append 
                              (list (car lst1) (car lst2))
                              (interleave (cdr lst1) (cdr lst2)))))
)

(define (no-repeats s) 
  (if (null? s) nil
      (append 
              (if (not-in-rest (car s) (cdr s))
                  (list (car s))
                  nil)
              (no-repeats (cdr s)))
  )
)

(define (not-in-rest x s)
  (if (null? s) true
      (and (not (= x (car s)))
           (not-in-rest x (cdr s)))
  )
)

;;; the official hint says "You may find it helpful to use filter with a lambda procedure to filter out repeats.
;;; To test if two numbers a and b are not equal, use (not (= a b))."
;;; How to implement in this way?

(define (no-repeats s)
  (if (null? s) s
    (cons (car s)
      (no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s)))))
)

