# Collatzgrammar
Collatzgrammer is a symbolic, string-based, balanced ternary system for exploring Collatz sequences and trees.
Instead of performing arithmetic, numbers are represented as strings if +, 0, and - (balanced ternary digits), and rewrite rules simulate Collatz steps.
So let me explain the rules a bit better. i assume you know a bit about collatz conjecture so i wont explain it.
rather i will talk about balanced ternary system.

any integer number can be defined using balanced ternary form. like +,0,-
division by 2 was a problem in base 3, but luck was on my side.
so i did that and discovered two axioms that made this grammar possible.
any number divided by 2 in base 3 can be decomposed in these two axioms.

1. +000...(n times)+/2 == +-...n+1 times
2. +000...(n times)-/2 == +...n+1 times

the rest follows by grouping up toether
