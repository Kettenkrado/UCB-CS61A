;;; Return whether there are n perfect squares with no repeats that sum to total
(define (fit total n)
    (define (f total n k)
        (if (and (= n 0) (= total 0))
            #t
        (if (< total (* k k))
            #f
            (or (f (- total (* k k)) (- n 1) (+ k 1))
                (f total n (+ k 1)))
        )))
    (f total n 1))

(expect (fit 10 2) #t)  ; 1*1 + 3*3
(expect (fit 9 1)  #t)  ; 3*3
(expect (fit 9 2)  #f)  ;
(expect (fit 9 3)  #f)  ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
(expect (fit 25 1)  #t) ; 5*5
(expect (fit 25 2)  #t) ; 3*3 + 4*4

(define with-list
    (list
        (list 'a 'b)
        (list 'c 'd (list 'e))
    )
)
; (draw with-list)  ; Uncomment this line to draw with-list

(define with-quote
    '(
        (a b) (c d (e))
    )

)
; (draw with-quote)  ; Uncomment this line to draw with-quote

(define first
   (cons 'a (cons 'b nil)))

(define with-cons
    (cons
        first 
        (cons 'c (cons 'd (cons (cons 'e nil) nil)))
    )
)
; (draw with-cons)  ; Uncomment this line to draw with-cons


;;; Return a list of pairs containing the elements of s.
;;;
;;; scm> (pair-up '(3 4 5 6 7 8))
;;; ((3 4) (5 6) (7 8))
;;; scm> (pair-up '(3 4 5 6 7 8 9))
;;; ((3 4) (5 6) (7 8 9))
(define (pair-up s)
    (if (<= (length s) 3)
        (list s)
        (append
            (list (list (car s) (car (cdr s))))
            (pair-up (cdr (cdr s)))
        )
    ))

(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )