# Eat Grapes

Source: [Nowcoder](https://www.nowcoder.com/questionTerminal/14c0359fb77a48319f0122ec175c9ada)

Chinese version: [eat_grapes.md](eat_grapes.md)

## 1. Problem

There are three kinds of grapes, with quantities $a$, $b$, and $c$. There are three people:

- The first person can only eat grape types 1 and 2.
- The second person can only eat grape types 2 and 3.
- The third person can only eat grape types 1 and 3.

Arrange the three people so that all grapes are eaten, and the number of grapes eaten by the person who eats the most is as small as possible.

### Input

$a$, $b$, and $c$ are positive integers.

### Output

Output the minimum possible number of grapes eaten by the person who eats the most.

## 2. Conclusion

Let $s = a + b + c$, and let $m = \max(a, b, c)$. The answer is:

$$
\max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{m}{2} \right\rceil\right)
$$

Code:

```python
def find_min_max(a, b, c):
    return max((a + b + c + 2) // 3, (max(a, b, c) + 1) // 2)
```

The rest of this document proves the conclusion.

## 3. Visualization

We can view the three people as sitting at vertices $A$, $B$, and $C$ of a triangular table, with the three grape types placed at the three vertices. Each grape type can only be eaten by the two adjacent people.

The red, yellow, and blue segments in the figure represent the numbers of grapes eaten by the three people. These segments are only used to illustrate the allocation relationship; they do not need to form a real triangle.

![eat_grapes_visualization](../images/eat_grapes_visualization.png)

## 4. Lower Bound Derivation

Without loss of generality, sort the three grape quantities and assume:

$$
a \le b \le c
$$

Now the largest grape type has quantity $c$. Let the final numbers of grapes eaten by the three people be $x$, $y$, and $z$.

Since all grapes must be eaten:

$$
x + y + z = a + b + c = s
$$

Therefore, the person who eats the most must eat at least the average:

$$
\max(x, y, z) \ge \left\lceil \frac{s}{3} \right\rceil
$$

On the other hand, the largest grape type has $c$ grapes, and it can only be eaten by two people. So at least one of those two people must eat at least half of it:

$$
\max(x, y, z) \ge \left\lceil \frac{c}{2} \right\rceil
$$

Thus the answer is at least:

$$
\max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{c}{2} \right\rceil\right)
$$

It remains to prove that this lower bound is always achievable.

## 5. Proof

Let:

$$
R = \max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{c}{2} \right\rceil\right)
$$

The previous section shows that no valid allocation can have an answer smaller than $R$. Now we only need to prove that there is always an allocation where each person eats at most $R$ grapes.

Think of the problem as a capacity allocation problem:

- Each grape type is a batch of items to allocate.
- Each person has capacity $R$.
- Each grape type can only flow to the two people who can eat it.

This is a small bipartite allocation problem. By the max-flow min-cut theorem, if every group of grape types has total quantity no larger than the total capacity of the people who can eat that group, then a complete allocation exists. In other words, we only need to check whether any capacity bottleneck exists.

### One Grape Type

Any single grape type has at most $c$ grapes, and it can be eaten by two people. The total capacity of those two people is $2R$.

Because:

$$
R \ge \left\lceil \frac{c}{2} \right\rceil
$$

we have:

$$
c \le 2R
$$

So no single grape type exceeds the total capacity of the two people who can eat it.

### Two Or Three Grape Types

Any two grape types together can be eaten by all three people. For example:

- Grape types 1 and 2 can be eaten collectively by people 1, 2, and 3.
- Grape types 1 and 3 can also be eaten collectively by people 1, 2, and 3.
- Grape types 2 and 3 are the same.

The total capacity of the three people is $3R$. Because:

$$
R \ge \left\lceil \frac{s}{3} \right\rceil
$$

we have:

$$
s \le 3R
$$

The total quantity of any two grape types is no more than $s$, and the total quantity of all three grape types is exactly $s$. Therefore, neither two grape types nor three grape types can exceed the total capacity of all three people.

### Therefore It Is Feasible

We have checked every possible bottleneck:

- A single grape type does not exceed the capacity of its two eligible people.
- Two or three grape types do not exceed the total capacity of all three people.

Therefore, there must be an allocation where each person eats at most $R$ grapes.

Combining this with the lower bound, the answer is:

$$
\max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{c}{2} \right\rceil\right)
$$

The following two figures show the intuition for the cases where the largest grape type dominates and where the total average dominates:

![eat_grapes_case1](../images/eat_grapes_solution1.png)

![eat_grapes_case2](../images/eat_grapes_solution2.png)

## 6. Complexity

We only need to compute the sum and the maximum.

- Time complexity: $O(1)$
- Space complexity: $O(1)$
