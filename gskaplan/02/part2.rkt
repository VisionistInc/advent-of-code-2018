#!/usr/bin/racket
#lang racket

(define box-ids (file->lines "./input.txt"))

(define comm (lambda (str1 str2)
                        (cond
                          ((or (null? str1) (null? str2)) '())
                          ((eq? (car str1) (car str2)) (cons (car str1) (comm (cdr str1) (cdr str2))))
                          (else (comm (cdr str1) (cdr str2)))
                          )
                        ))

(define str-comm (lambda (str1 str2)
                   (list->string (comm (string->list str1) (string->list str2)))
                   ))

(foldl
 (lambda (val current)
   (define len (string-length val))
   (define commons (map (lambda (val2) (str-comm val val2)) box-ids))
   (define matched (filter
                    (lambda (common) (eq? (string-length common) (- len 1)))
                    commons
                    ))
   (if (null? matched) current (car matched))
   )
 ""
 box-ids
 )
