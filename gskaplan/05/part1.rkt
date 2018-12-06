#!/usr/bin/racket
#lang racket

(define text-in (string->list (string-trim (file->string "input.txt"))))

(define can-annhilate
  (lambda (c1 c2)
    (or
     (and
      (eq? (char-upcase c1) c2)
      (eq? c1 (char-downcase c2))
      )
     (and
      (eq? c1 (char-upcase c2))
      (eq? (char-downcase c1) c2)
      )
     )
    ))

(define annhilate
  (lambda (lch)
    (cond
      ((or (null? lch) (null? (cdr lch))) lch)
      ((can-annhilate (car lch) (cadr lch)) (annhilate (cddr lch)))
      (else (cons (car lch) (annhilate (cdr lch))))
      )
    ))

(define last-len 0)
(define current-len 0)
(let loop ()
  (set! last-len (length text-in))
  (set! text-in (annhilate text-in))
  (set! current-len (length text-in))
  (displayln current-len)
  (when (< current-len last-len) (loop)))
