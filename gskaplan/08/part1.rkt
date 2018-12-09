#!/usr/bin/racket
#lang racket

(define input (file->list "input.txt"))

(struct tree (sum kstack mstack) #:transparent)

(define tree-record
  (foldl
   (lambda (v t)
     (let ([kst (tree-kstack t)]
           [mst (tree-mstack t)]
           [tsm (tree-sum t)])
       (if
        (eq? (length kst) (length mst))
        (cond
          [(null? kst) (struct-copy tree t [kstack (cons v null)])]
          [(and (zero? (car kst)) (eq? 1 (car mst)))
           (struct-copy tree t [sum (+ v tsm)]
                        [kstack (let ([k (cdr kst)])
                                  (if
                                   (null? k)
                                   null
                                   (cons (sub1 (car k)) (cdr k))
                                   ))]
                        [mstack (cdr mst)])]
          [(zero? (car kst))
           (struct-copy tree t [sum (+ v tsm)]
                        [mstack (cons (sub1 (car mst)) (cdr mst))])]
          [(eq? 1 (car mst)) (struct-copy tree t [sum (+ v tsm)]
                                          [kstack (cons (sub1 (car kst)) (cdr kst))]
                                          [mstack (cons 0 (cdr mst))])]
          [(zero? (car mst)) (struct-copy tree t [kstack (cons v kst)]
                                          [mstack (cdr mst)])]
          [else (struct-copy tree t [kstack (cons v kst)])]
          )
        (struct-copy tree t [mstack (cons v mst)])
        )
       )
     )
   (tree 0 null null)
   input
   ))

(displayln (tree-sum tree-record))
