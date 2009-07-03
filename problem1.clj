; Givens
(def mx 1000)
(def f1 3)
(def f2 5)

; Addition/Subtraction Solution (This is not done.)
(+
    (sum (range f1 mx f1))
    (sum (range f2 mx f2))
    (neg (sum (range (* f1 f2) mx (* f1 f2)) )))
