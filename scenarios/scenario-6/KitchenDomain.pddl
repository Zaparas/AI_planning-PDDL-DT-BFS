; This is a comment line
(define (domain dinner)
  (:requirements :strips)
  (:predicates
    (clean)
    (dinner)
    (quiet)
    (present)
    (garbage)
  )
  (:action order_delivery_food
    :effect (dinner)
  )
  (:action cook
    :precondition (clean)
    :effect (dinner)
  )
  (:action wrap
    :precondition (quiet)
    :effect (present)
  )
  (:action carry
    :precondition (garbage)
    :effect (and
      (not (garbage))
      (not (clean))
    )
  )
  (:action dolly
    :precondition (garbage)
    :effect (and
      (not (garbage))
      (not (quiet))
    )
  )
  (:action santify
    :precondition (not (garbage))
    :effect (clean)
  )
)