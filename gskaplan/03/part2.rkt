#!/usr/bin/racket
#lang racket

(define claims-raw (file->lines "input.txt"))

(struct claim (id x y dx dy) #:transparent)

(define parse-claim (lambda (c)
                      (define parts
                        (cdr (regexp-match
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

(define do-claims-overlap (lambda (c1 c2)
                            (and
                             (not (eq? (claim-id c1) (claim-id c2)))
                             (or
                              (does-claim-cover c1 (claim-x c2) (claim-y c2))
                              (does-claim-cover
                               c1 (+ (claim-x c2) (claim-dx c2)) (claim-y c2))
                              (does-claim-cover
                               c1 (claim-x c2) (+ (claim-y c2) (claim-dy c2)))
                              (does-claim-cover
                               c1 (+ (claim-x c2) (claim-dx c2))
                               (+ (claim-y c2) (claim-dy c2)))

                              (does-claim-cover c2 (claim-x c1) (claim-y c1))
                              (does-claim-cover
                               c2 (+ (claim-x c1) (claim-dx c1)) (claim-y c1))
                              (does-claim-cover
                               c2 (claim-x c1) (+ (claim-y c1) (claim-dy c1)))
                              (does-claim-cover
                               c2 (+ (claim-x c1) (claim-dx c1))
                               (+ (claim-y c1) (claim-dy c1)))

                              (does-claim-cover
                               c1 (+ (claim-x c2) (/ (claim-dx c2) 2))
                               (+ (claim-y c2) (/ (claim-dy c2) 2)))
                              )
                             )
                            ))

(define all-non-overlapping
  (lambda (c clist)
    (filter-not (lambda (c2) (do-claims-overlap c c2)) clist)
    ))

(foldl
 all-non-overlapping
 claims
 claims
 )
