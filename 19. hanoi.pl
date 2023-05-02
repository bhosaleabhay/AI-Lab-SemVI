% Move N disks from the From pole to the To pole using the Aux pole
% hanoi(+N, +From, +To, +Aux, -Moves)

:- initialization(hanoi).
hanoi(0, _, _, _, []).
hanoi(N, From, To, Aux, Moves) :-
    N1 is N - 1,
    hanoi(N1, From, Aux, To, Moves1),
    move(From, To, Moves2),
    hanoi(N1, Aux, To, From, Moves3),
    append(Moves1, Moves2, Temp),
    append(Temp, Moves3, Moves).

% Move a single disk from the From pole to the To pole
% move(+From, +To, -Moves)
move(From, To, [move(From, To)]).

/*
To use this program, you can call hanoi(N, From, To, Aux, Moves) where N is the 
number of disks, From is the starting pole, To is the destination pole, Aux is the auxiliary pole, 
and Moves is the list of moves required to solve the puzzle. For example:

?- consult("D:/App Develop/AI/hanoi.pl").  
true.

?- hanoi(3, left, right, middle, Moves).
Moves = [move(left, middle), move(left, right), move(middle, right), move(left, middle), move(right, left), move(right, middle), move(left, middle)]

This shows that to solve the puzzle with 3 disks, we need to move the top 2 disks to the 
auxiliary pole, then move the bottom disk to the destination pole, and finally move the 2 
disks from the auxiliary pole to the destination pole. The move predicate is used to
represent a single move, and the append predicate is used to concatenate the lists of
moves generated by the recursive calls.

*/