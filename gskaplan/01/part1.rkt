#!/usr/bin/racket
#lang racket

(define initial 0)
(define deltas (file->list (string->path "./input.txt")))

(define finalfreq (lambda (current dfreq) 
                    (cond 
                      ((null? dfreq) current) 
                      (else (finalfreq (+ current (car dfreq)) (cdr dfreq)))
                      )
                    ))

(finalfreq initial deltas)
