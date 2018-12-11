#!/usr/bin/racket
#lang racket

(define screen-w 80)
(define screen-h 24)
(define n-frames 10124)

(command-line
 #:program "day-10-pt-1"
 #:once-each
 [("-w" "--width") w "width to set" (set! screen-w (string->number w))]
 [("-g" "--height") h  "height to set" (set! screen-h (string->number h))]
 [("-f" "--frame") f "frame to view" (set! n-frames (string->number f))]
 )

(define re #px"< *(-?\\d+), +(-?\\d+)>")

(define (parse-vec s)
  (define parts (regexp-match* re s #:match-select cdr))
  (map (lambda (v) (map string->number v)) parts)
  )

(define input-vecs (map parse-vec (file->lines "input.txt")))

(define (get-extreme-val init-val comparison accessor-fn)
  (lambda (list-of-vecs)
    (foldl
     (lambda (v c)
       (comparison c (accessor-fn v))
       )
     init-val
     list-of-vecs
     )))

(define min-x (get-extreme-val +inf.0 min caar))
(define min-y (get-extreme-val +inf.0 min cadar))
(define max-x (get-extreme-val -inf.0 max caar))
(define max-y (get-extreme-val -inf.0 max cadar))

(define (bin-1d vmin vmax vi nbins)
  (floor (* (/ (- vi vmin) (- vmax vmin)) (sub1 nbins)))
  )

(define (disp-pts l)
  (let ([xmin (min-x l)]
        [xmax (max-x l)]
        [ymin (min-y l)]
        [ymax (max-y l)])
    (define grid-pts
      (for/list ([yc (in-range screen-h)])
        (for/list ([xc (in-range screen-w)])
          (define is-there-a-point
            (findf
             (lambda (v)
               (and
                (= xc (bin-1d xmin xmax (caar v) screen-w))
                (= yc (bin-1d ymin ymax (cadar v) screen-h))
                ))
             l
             ))
          (if is-there-a-point true false)
          ))
      )
    (define (disp-row r) (displayln (list->string (map (lambda (v) (if v #\# #\space)) r))))
    (for-each disp-row grid-pts)
    (displayln "")
    )
  )

(define (advance-n-keyframes n l)
  (map
   (lambda (v)
     (list (list (+ (caar v) (* n (caadr v))) (+ (cadar v) (* n (cadadr v)))) (cadr v))
     )
   l
   )
  )

(disp-pts (advance-n-keyframes n-frames input-vecs))
(displayln n-frames)
