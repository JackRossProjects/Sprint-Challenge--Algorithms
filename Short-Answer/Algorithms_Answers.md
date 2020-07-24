#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Algorithm A has a complexity of O(n).</br>
   O(1) for the first line (constant)</br>
   O(n^3 + 1) for the second line</br>
   O(n^2 + 1) for the third line</br>
   This simplifies to O(n).</br>
   
b) Algorithm B has a complexity of O(n^2)</br>
   O(1) to set the sum (constant)</br>
   O(n) to loop through each element in range(n)</br>
   O(1) to initialize j</br>
   O(n) to check if j is less than n</br>
   O(1) to increment j</br>
   O(1) to increment sum</br>
   Getting rid of exponents and constants, this algorithm runs in O(n^2)</br>
   (Or just look that 2 loops have been combined)</br>

c) Algorithm C has a complexity of O(n)
   This is a recursive function that calls itself so this runtime will be linear.</br>

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

# Answer:
We could use a binary search. We would start by dropping an egg off of the middle floor (lobby + top floor // 2). If the egg broke, we would move down one floor (moving left on a hypothetical binary tree). If the egg didn't break, we would move one floor higher and drop the egg again. (moving right on a hypothetical binary tree.) We would do this until we find the optimal floor to drop eggs. (ie. the target).</br>

Runtime Complexity:</br>
Binary search runs in O(log(n)).

