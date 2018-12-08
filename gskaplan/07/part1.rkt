#!/usr/bin/racket
#lang racket

(define input-lines (file->lines "input.txt"))

(define string->char
  (lambda (c)
    (car (string->list c))
    ))

(define parse-req
  (lambda (s)
    (map string->char
         (cdr
          (regexp-match #px"^Step ([A-Z]) must be finished before step ([A-Z]) can begin.$" s)
          ))
    ))

(define requirements (map parse-req input-lines))

(define all-steps
  (sort
   (remove-duplicates
    (foldl
     (lambda (v c)
       (append c v)
       )
     null
     requirements
     ))
   char<?
   ))

(define initial-hash
  (foldl
   (lambda (s h)
     (hash-set h s null)
     )
   (make-immutable-hash)
   all-steps
   ))

(define dep-tree
  (foldl
   (lambda (v current)
     (hash-update current (second v) (lambda (l) (cons (first v) l)))
     )
   initial-hash
   requirements
   ))

(define is-step-ready?
  (lambda (deps already-done)
    (cond
      ((null? deps) #t)
      ((member (car deps) already-done) (is-step-ready? (cdr deps) already-done))
      (else #f)
      )
    ))

(define done-pile null)
(define todo-pile all-steps)

(let loop ()
  (define step-to-do
    (findf
     (lambda (s) (is-step-ready? (hash-ref dep-tree s) done-pile))
     todo-pile
     ))
  (set! done-pile (cons step-to-do done-pile))
  (set! todo-pile (remove step-to-do todo-pile))
  (when (not (null? todo-pile)) (loop))
  )

(define task-order (reverse done-pile))

(displayln task-order)
