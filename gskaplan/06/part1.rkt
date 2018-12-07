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

(define find-min
  (lambda (l)
    (define indices (indexes-of l (apply min l)))
    (if
     (null? (cdr indices))
     (car indices)
     #f
     )
    ))

(define closest-pt-at-each (map (lambda (l) (find-min l)) all-dists))

(define is-pt-at-edge?
  (lambda (p)
    (or
     (eq? (first p) 0)
     (eq? (first p) max-x)
     (eq? (second p) 0)
     (eq? (second p) max-y)
     )
    ))

(define grouped-indices
  (for/list ([idx (length input-pts)])
    (indexes-of closest-pt-at-each idx)
    ))

(define is-set-finite?
  (lambda (s)
    (define filtered-pts
      (filter (lambda (idx) (not (is-pt-at-edge? (list-ref grid-pts idx)))) s))
    (eq? (length s) (length filtered-pts))
    ))

(apply max
       (filter-map
        (lambda (x) (and (is-set-finite? x) (length x)))
        grouped-indices
        ))
