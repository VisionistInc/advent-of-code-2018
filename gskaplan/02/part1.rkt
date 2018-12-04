#!/usr/bin/racket
#lang racket

(define box-ids (file->lines "./input.txt"))

(define get-counts (lambda (id)
                     (foldl (lambda (val current)
                              (hash-update current val (lambda (x) (+ 1 x)) 0)
                              )
                            (make-immutable-hash)
                            (string->list id))
                     ))

(define are-there-n (lambda (id n)
                      (define count-map (get-counts id))
                      (define count-list (hash-values count-map))
                      (not (eq? #f (member n count-list)))
                      ))

(define twos (length (filter (lambda (id) (are-there-n id 2)) box-ids)))
(define threes (length (filter (lambda (id) (are-there-n id 3)) box-ids)))

(* twos threes)
