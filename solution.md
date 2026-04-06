### Solution Explanation

We are given an array and allowed to increase elements by 1 per operation.

We need at least one subarray of length ≥ 2 whose GCD is divisible by k.

Key Observation:
For the GCD of a subarray to be divisible by k, every element in that subarray must be divisible by k.

Thus, the problem reduces to:
Make at least two elements divisible by k with minimum operations.

For each element, compute the cost to make it divisible by k:
cost[i] = (k - (a[i] mod k)) mod k

Then:
- Sort all costs
- Pick the two smallest
- Their sum is the minimum operations required

Time Complexity:
O(n log n) due to sorting

Space Complexity:
O(n)
