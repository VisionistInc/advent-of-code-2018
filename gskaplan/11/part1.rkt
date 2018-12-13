#!/usr/bin/racket
#lang racket

(define grid-size 300)
(define grid-serial 9995)

(define (rack-id x) (+ 10 x))
(define (hundreds-digit n) (floor (/ (modulo n 1000) 100)))

(define (power-level xy)
  (let ([rid (rack-id (first xy))])
  (- (hundreds-digit (* rid (+ grid-serial (* (second xy) rid)))) 5)
  ))

(define square-indices
  (let ([lst (range (- grid-size 2))])
    (cartesian-product lst lst))
  )

(define max-square-sum
  (foldl
   (lambda (xy curr)
     (define sqr-sum
       (foldl
      (lambda (v c)
        (+ c (power-level v))
        )
      0
      (let ([x (first xy)] [y (second xy)])
        (cartesian-product (range x (+ x 3)) (range y (+ y 3)))
        )
      ))
     (if (> sqr-sum (first curr)) (list sqr-sum xy) curr)
     )
   '(0 (0 0))
   square-indices
   ))

(let ([v (second max-square-sum)])
  (printf "~a,~a~n" (first v) (second v))
  )
