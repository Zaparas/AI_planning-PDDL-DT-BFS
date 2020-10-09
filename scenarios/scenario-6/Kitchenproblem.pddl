(define (problem pb1)
  (:domain dinner)
  (:init
    (garbage)
    (quiet)
  )
  (:goal (and
    (dinner)
    (present)
    (not (garbage))
  ))
)