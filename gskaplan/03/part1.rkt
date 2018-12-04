#!/usr/bin/racket
#lang racket

(define claims-raw (file->lines "input.txt"))

(struct claim (x y dx dy))

(define parse-claim (lambda (c)
                      (define parts
                        (cddr (regexp-match
                              #px"^#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)$" c))
                        )
                      (define vals (map string->number parts))
                      (apply claim vals)
                      ))

(define claims (map parse-claim claims-raw))

(define does-claim-cover (lambda (c x y)
                           (and
                            (> x (claim-x c))
                            (> y (claim-y c))
                            (<= x (+ (claim-x c) (claim-dx c)))
                            (<= y (+ (claim-y c) (claim-dy c)))
                            )
                           ))

(define max-x (foldl
               (lambda (val current)
                 (max current (+ (claim-x val) (claim-dx val)))
                 )
               0
               claims))

(define max-y (foldl
               (lambda (val current)
                 (max current (+ (claim-y val) (claim-dy val)))
                 )
               0
               claims))

(define grid-x (for/list ([i max-x]) i))
(define grid-y (for/list ([i max-y]) i))

(define pixls
  (map (lambda (xval)
         (map (lambda (yval)
                (foldl
                 (lambda (c current)
                   (if (does-claim-cover c xval yval) (+ current 1) current)
                   )
                 0
                 claims
                 ))
              grid-y
              )
         )
       grid-x
       ))

(length (filter (lambda (v) (> v 1)) (flatten pixls)))
