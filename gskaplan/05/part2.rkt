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

(define react-polymer ; haha get it
  (lambda (poly-in)   ; i'll be here all week
    (define t poly-in)
    (define last-len 0)
    (define current-len 0)
    (let loop ()
      (set! last-len (length t))
      (set! t (annhilate t))
      (set! current-len (length t))
      (when (< current-len last-len) (loop)))
    current-len
      ))

(define purge-char
  (lambda (c t)
    (remove* (list c) (remove* (list (char-downcase c)) t))
    ))

(define alphabet (for/list ([i 26]) (integer->char (+ 65 i))))

(for-each
 (lambda (letter)
   (define poly (purge-char letter text-in))
   (define poly-len (react-polymer poly))
   (printf "~a ~a~n" letter poly-len)
   ) alphabet)
