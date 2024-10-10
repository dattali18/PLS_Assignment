# This Assignment is assignment #4 of the PLS (Programming Language Structure) course.

# This program is to showcase basic Prolog Programming.

# Part 1: Family Structure

father(X, Y) :- parent(X, Y), male(X).

mother(X, Y) :- parent(X, Y), female(X).

son(X, Y) :- parent(Y, X), male(X).

daughter(X, Y) :- parent(Y, X), femal(X).

grandfather(X, Y) :- father(X, Z), parent(Z, Y).

grandmother(X, Y) :- mother(X, Z), parent(Z, Y).

grandson(X, Y) :- son(X, Z), parent(Y, Z).

granddaughter(X, Y) :- daughter(X, Z), parent(Y, Z).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

# uncle from marriage

uncle(X, Y) :- parent(Z, Y), sibling(Z, U), marriage(U, X), male(Y).

# male cousing from an aunt

cousin(X, Y) :- parent(Z, Y), sibling(Z, U), parent(U, X), 

brother_in_law(X, Y) :- marriage(X, Z), sibling(X, Y), male(Y).

nice(X, Y) :- parent(Z, Y), sibling(Z, X), female(X).

second_cousin(X, Y) :- cousin(Z, Y), cousin(Z, X), male(X), male(Y).

# Part 2: List Manipulation

# Reverse a list

reverse([], []).
reverse([H|T], R) :- reverse(T, R1), append(R1, [H], R).

# Check if an element is in the list

member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

# Palindrom check

palindrome(L) :- reverse(L, L).

# Sorted list check

sorted([]).
sorted([_]).
sorted([H1, H2|T]) :- H1 =< H2, sorted([H2|T]).


# Permutation

perm([], []).
perm(L, [H|T]) :- member(H, L), perm(L, T).

# Part 3: Arithmetic

sum(1, 1).
sum(N, Res) :- N > 1, N1 is N - 1, sum(N1, Res1), Res is Res1 + N.

sumDigits(0, 0).
sumDigits(Num, Sum) :-
    Num > 0,
    Digit is Num mod 10,
    Rest is Num // 10,
    sumDigits(Rest, SumRest),
    Sum is Digit + SumRest.

# Split a number into a list of digits
split(0, []).
split(N, [D|Rest]) :- 
    N > 0, 
    D is N mod 10, 
    N1 is N // 10, 
    split(N1, Rest).

# Create a number from a list of digits
create([], 0).
create([H|T], N) :- 
    create(T, N1), 
    N is N1 * 10 + H.

# Reverse the digits of a number
reverse_digits(N, R) :- 
    split(N, Digits), 
    reverse(Digits, RevDigits), 
    create(RevDigits, R).

intersection([], _, []).
intersection([H|T], L2, [H|Res]) :- member(H, L2), intersection(T, L2, Res).
intersection([_|T], L2, Res) :- intersection(T, L2, Res).

Reverse the digits of a number
reverse_digits(N, R) :- 
    split(N, Digits), 
    reverse(Digits, RevDigits), 
    create(RevDigits, R).
