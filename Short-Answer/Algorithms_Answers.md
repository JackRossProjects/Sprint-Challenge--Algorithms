#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Algorithm A has a complexity of O(n).\n
   O(1) for the first line (constant)
   O(n^3 + 1) for the second line
   O(n^2 + 1) for the third line
   This simplifies to O(n).
   
b) Algorithm B has a complexity of O(n^2)
   O(1) to set the sum (constant)
   O(n) to loop through each element in range(n)
   O(1) to initialize j
   O(n) to check if j is less than n
   O(1) to increment j
   O(1) to increment sum
   Getting rid of exponents and constants, this algorithm runs in O(n^2)
   (Or just look that 2 loops have been combined)

c) Algorithm C has a complexity of O(n)
   This is a recursive function that calls itself so this runtime will be linear.

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

# Answer:
We could use a binary search. We would start by dropping an egg off of the middle floor (lobby + top floor // 2). If the egg broke, we would move down one floor (moving left on a hypothetical binary tree). If the egg didn't break, we would move one floor higher and drop the egg again. (moving right on a hypothetical binary tree.) We would do this until we find the optimal floor to drop eggs. (ie. the target).

Runtime Complexity:
Binary search runs in O(log(n)).

