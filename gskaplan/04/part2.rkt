#!/usr/bin/racket
#lang racket

(define times-raw (file->lines "input.txt"))
(define times-sorted (sort times-raw string<?))

(struct time-record (year month day hour minute activity) #:transparent)
(struct log-activity (id is-asleep is-starting) #:transparent)

(define try-parse-activity
  (lambda (a)
    (define parsed (regexp-match #px"^Guard #(\\d+) begins shift$" a))
    (if (eq? #f parsed) a (log-activity (string->number (second parsed)) #f #t))
    ))

(define parse-time
  (lambda (t)
    (define parsed (regexp-match #px"^\\[(\\d+)-(\\d+)-(\\d+) (\\d+):(\\d+)\\] (.*)$" t))
    (time-record (string->number (second parsed)) (string->number (third parsed))
                 (string->number (fourth parsed))  (string->number (fifth parsed))
                 (string->number (sixth parsed)) (try-parse-activity (seventh parsed)))
    ))

(define times-parsed (map parse-time times-sorted))

(define fully-parsed-times
  (foldl
   (lambda (t current)
     (define last-activity (time-record-activity (last current)))
     (append current
             (list
              (if
               (log-activity? (time-record-activity t))
               t
               (struct-copy time-record t
                            [activity (log-activity
                                       (log-activity-id last-activity)
                                       (equal? (time-record-activity t) "falls asleep")
                                       #f
                                       )])
               )))
     )
   (list (car times-parsed))
   (cdr times-parsed)
   ))

(struct sleep-time (id minute) #:transparent)

(define get-minutes
  (lambda (start-time end-time)
    (define start-hour (time-record-hour start-time))
    (define end-hour (time-record-hour end-time))
    (define list-of-minutes
      (stream->list
       (in-range (+ (* 60 start-hour) (time-record-minute start-time))
                 (+ (* 60 (if
                           (> start-hour end-hour)
                           (+ 24 end-hour)
                           end-hour
                           ))
                    (time-record-minute end-time)))
       ))
    (map
     (lambda (m)
       (sleep-time (log-activity-id (time-record-activity start-time)) (modulo m 60)))
     list-of-minutes
     )
    ))

(define atomized-minutes
  (foldl
   (lambda (t current)
     (define current-activity (time-record-activity t))
     (cond
       ((log-activity-is-starting current-activity) current)
       ((log-activity-is-asleep current-activity)
        (cons t current))
       (else (append
              (get-minutes (car current) t)
              (cdr current)))
       ))
   '()
   fully-parsed-times
   ))

(define minutes-by-guard
  (foldl
   (lambda (m current)
     (hash-update current (sleep-time-id m) (lambda (v) (cons (sleep-time-minute m) v)) '())
     )
   (make-immutable-hash)
   atomized-minutes
   ))

(define most-reliable-sleeper
  (argmax
   (lambda (ls) (length (second ls)))
   (hash-map minutes-by-guard
             (lambda (k v)
               (list k (argmax length (group-by (lambda (x) (modulo x 60)) v)))
               ))))

(* (car most-reliable-sleeper) (caadr most-reliable-sleeper))
