#!/usr/bin/racket
#lang racket

(define read-coordinates
  (lambda (l)
    (map string->number (map string-trim (string-split l ",")))
    ))

(define input-pts (map read-coordinates (file->lines "input.txt")))

(define manhattan
  (lambda (p1 p2)
    (+ (abs (- (first p1) (first p2))) (abs (- (second p1) (second p2))))
    ))

(define max-x (apply max (map first input-pts)))
(define max-y (apply max (map second input-pts)))

(define x-vals (stream->list (in-range 0 (+ 1 max-x))))

(define y-vals (stream->list (in-range 0 (+ 1 max-y))))

(define grid-pts
  (foldl
   (lambda (x l)
     (define y-lst
       (map
        (lambda (y)
          (list x y))
        y-vals)
       )
     (append l y-lst)
     )
   null
   x-vals
   ))

(define all-dists
  (map (lambda (p) (map (lambda (q) (manhattan q p)) input-pts)) grid-pts)
  )

(define all-dists-sum (map (lambda (l) (apply + l)) all-dists))

(count (lambda (d) (< d 10000)) all-dists-sum)
