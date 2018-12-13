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

(define (max-square-sum sz)
  (foldl
   (lambda (xy curr)
     (define sqr-sum
       (foldl
      (lambda (v c)
        (+ c (power-level v))
        )
      0
      (let ([x (first xy)] [y (second xy)])
        (cartesian-product (range x (+ x sz)) (range y (+ y sz)))
        )
      ))
     (if (> sqr-sum (first curr)) (list sqr-sum xy) curr)
     )
   '(0 (0 0))
   (let ([lst (range (add1 (- grid-size sz)))])
     (cartesian-product lst lst))
   ))

(define max-mod-sum
  (foldl
   (lambda (sz curr)
     (define ret (max-square-sum sz))
     (displayln ret)
     (if
      (> (first ret) (first curr))
      (list (first ret) sz (second ret))
      curr
      )
     )
   '(0 1 (0 0))
   (range 1 300)
   ))

(let ([v (third max-mod-sum)])
  (printf "~a,~a,~a~n" (first v) (second v) (second max-mod-sum))
  )
