#!/usr/bin/racket
#lang racket

(define initial 0)
(define deltas (file->list (string->path "./input.txt")))

(define member? (lambda (qval reflist)
                  (cond
                    ((null? reflist) #f)
                    ((eq? qval (car reflist)) #t)
                    (else (member? qval (cdr reflist)))
                    )
                  ))

(define pluscar (lambda (v l)
                  (+ v (car l))
                  ))

(define firstmatch (lambda (current dfreq out)
                     ;(println current)
                     (cond
                       ((null? dfreq) '())
                       ((member? current (cdr out)) current)
                       (else (firstmatch (pluscar current dfreq) (cdr dfreq) (cons (pluscar current dfreq) out)))
                       )
                     ))

(define again-and-again (flatten (make-list 250 deltas)))

(firstmatch initial again-and-again '(()))
