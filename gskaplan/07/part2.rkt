#!/usr/bin/racket
#lang racket

(define input-lines (file->lines "input.txt"))
(define num-workers 5)
(define base-time 60)

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

(define completion-time
  (lambda (s)
    (+ base-time (- (char->integer s) 64))
    ))

(define seconds-elapsed 0)
(define done-pile null)
(define todo-pile all-steps)
(define in-progress (make-vector num-workers #f))

(define (step-to-do)
  (findf
   (lambda (s) (is-step-ready? (hash-ref dep-tree s) done-pile))
   todo-pile
   ))

(define (get-log-str v)
  (if v (second v) #\.)
  )

(let loop-time ()
  (for ([worker num-workers])
    (let ([doing (vector-ref in-progress worker)])
      (if
       (eq? #f doing)
       (if
        (eq? #f (step-to-do))
        #f
        (let ([my-step (step-to-do)]) ; take the task from the to-do pile
          (set! todo-pile (remove my-step todo-pile))
          (vector-set!
           in-progress
           worker
           (list (completion-time my-step) my-step)
           )
          )
        )
       (if ; check remaining time, then pick up a new task
        (eq? 1 (first doing))
        (begin ; put the task in the done pile
          (set! done-pile (cons (second doing) done-pile))
          (if
           (eq? #f (step-to-do))
           (vector-set! in-progress worker #f) ; set to idle
           (let ([my-step (step-to-do)]) ; pick up a new task
             (set! todo-pile (remove my-step todo-pile))
             (vector-set!
              in-progress
              worker
              (list (completion-time my-step) my-step)
              )
             )
           )
          )
        (vector-set! in-progress worker (list (- (first doing) 1) (second doing)))
        )
       )
      )
    )
  (for ([worker num-workers])
    (let ([doing (vector-ref in-progress worker)])
      (cond
        [doing]
        [(step-to-do)
         (let ([my-step (step-to-do)])
           (set! todo-pile (remove my-step todo-pile))
           (vector-set!
            in-progress
            worker
            (list (completion-time my-step) my-step)
            )
           )]
        )
      )
    )
  (printf "~.a ~a ~a ~a ~a ~a~n"
          seconds-elapsed
          (get-log-str (vector-ref in-progress 0))
          (get-log-str (vector-ref in-progress 1))
          (get-log-str (vector-ref in-progress 2))
          (get-log-str (vector-ref in-progress 3))
          (get-log-str (vector-ref in-progress 4))
          )
  (unless (eq? (length done-pile) (length all-steps))
    (set! seconds-elapsed (+ 1 seconds-elapsed))
    (loop-time)
    )
  )

(displayln seconds-elapsed)
