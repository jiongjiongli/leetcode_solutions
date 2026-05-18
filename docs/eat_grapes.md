# 吃葡萄

来源：[牛客网](https://www.nowcoder.com/questionTerminal/14c0359fb77a48319f0122ec175c9ada)

English version: [eat_grapes_en.md](eat_grapes_en.md)

## 1. 问题

有三种葡萄，数量分别为 $a, b, c$。有三个人：

- 第一个人只吃第 1、2 种葡萄。
- 第二个人只吃第 2、3 种葡萄。
- 第三个人只吃第 1、3 种葡萄。

请合理分配三个人吃葡萄，使所有葡萄都被吃完，并让“吃得最多的人”的数量尽量少。

### 输入

$a, b, c$ 均为正整数。

### 输出

输出三个人中吃得最多的那个人最少需要吃多少颗葡萄。

## 2. 结论

设 $s = a + b + c$，并令 $m = \max(a, b, c)$，答案为：

$$
\max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{m}{2} \right\rceil\right)
$$

对应代码：

```python
def find_min_max(a, b, c):
    return max((a + b + c + 2) // 3, (max(a, b, c) + 1) // 2)
```

下面证明这个结论。

## 3. 可视化

可以把三个人看作坐在一个三角形桌子的三个顶点 $A, B, C$，三种葡萄分别放在三条边上。每种葡萄只能由这条边两端相邻的两个人吃。

图中的红、黄、蓝线段表示三个人分别吃掉的葡萄数量。注意这些线段只是帮助理解分配关系，并不要求它们构成一个真正的三角形。

![eat_grapes_visualization](../images/eat_grapes_visualization.png)

## 4. 下界推理

不失一般性，先把三种葡萄数量排序，假设：

$$
a \leqslant b \leqslant c
$$

此时最大的一种葡萄数量就是 $c$。设三个人最终吃掉的数量分别为 $x, y, z$。

因为所有葡萄都要吃完，所以：

$$
x + y + z = a + b + c = s
$$

因此，三个人中吃得最多的人至少要吃平均值这么多：

$$
\max(x, y, z) \geqslant \left\lceil \frac{s}{3} \right\rceil
$$

另一方面，数量最多的第 3 种葡萄有 $c$ 颗，但它只能由两个人吃完。所以这两个人中至少有一个人要吃不少于一半：

$$
\max(x, y, z) \geqslant \left\lceil \frac{c}{2} \right\rceil
$$

于是答案至少为：

$$
\max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{c}{2} \right\rceil\right)
$$

接下来只需要证明：这个下界一定可以达到。

## 5. 证明

令：

$$
R = \max\left(\left\lceil \frac{s}{3} \right\rceil,\left\lceil \frac{c}{2} \right\rceil\right)
$$

上一节已经证明，任何方案的答案都不可能小于 $R$。现在只需证明：一定存在一种方案，使每个人最多吃 $R$ 颗。

把问题看成一个容量分配问题：

- 每种葡萄是一批待分配的物品。
- 每个人有容量 $R$。
- 每种葡萄只能流向能吃它的两个人。

这是一个很小的二分图分配问题。根据最大流最小割定理，只要任意一组葡萄的总量都不超过能吃这组葡萄的人的总容量，就一定能完成分配。也就是说，我们只需要检查是否存在容量瓶颈。

### 单独看一种葡萄

任意一种葡萄最多有 $c$ 颗，而它可以由两个人吃。两个人的总容量是 $2R$。

因为：

$$
R \geqslant \left\lceil \frac{c}{2} \right\rceil
$$

所以：

$$
c \leqslant 2R
$$

也就是说，任意一种葡萄都不会超过能吃它的两个人的总容量。

### 看两种或三种葡萄

任意两种葡萄涉及的可食用人群一定覆盖全部三个人。例如：

- 第 1、2 种葡萄可以由第 1、2、3 个人共同消化。
- 第 1、3 种葡萄也可以由第 1、2、3 个人共同消化。
- 第 2、3 种葡萄同理。

三个人的总容量是 $3R$。因为：

$$
R \geqslant \left\lceil \frac{s}{3} \right\rceil
$$

所以：

$$
s \leqslant 3R
$$

任意两种葡萄的总量不超过 $s$，三种葡萄的总量也正好是 $s$，因此它们都不会超过三个人的总容量。

### 因此一定可行

上面检查了所有可能产生瓶颈的情况：

- 单独一种葡萄不会超过对应两个人的容量。
- 两种或三种葡萄不会超过三个人的总容量。

所以一定存在一种分配方式，使每个人最多吃 $R$ 颗。

结合前面的下界，答案就是：

$$
\max\left(\left\lceil \frac{s}{3} \right\rceil, \left\lceil \frac{c}{2} \right\rceil\right)
$$

下面两张图分别对应“最大种类特别多”和“总量平均值更大”时的直观分配思路。它们是对上面容量证明的构造化理解。

第一张图对应最大种类 $c$ 特别多的情况，即：

$$
\frac{s}{3} \leqslant \frac{c}{2}
$$

此时 $R = \left\lceil \frac{c}{2} \right\rceil$。瓶颈在于 $c$ 只能由红色和黄色两个人吃，所以先让他们尽量平分 $c$：黄色的人吃 $\left\lceil \frac{c}{2} \right\rceil$，红色的人吃 $\left\lfloor \frac{c}{2} \right\rfloor$。由于：

$$
\frac{s}{3} \leqslant \frac{c}{2}
\implies \frac{a+b+c}{3} \leqslant \frac{c}{2}
\implies a+b \leqslant \frac{c}{2}
\implies a+b \leqslant \left\lceil \frac{c}{2} \right\rceil
\implies a+b \leqslant R
$$

剩下的 $a + b$ 不超过上界 $R$，可以交给蓝色的人吃，因此最大值为 $R$。

![eat_grapes_case1](../images/eat_grapes_solution1.png)

第二张图对应总量平均值更大的情况，即：

$$
\frac{s}{3} > \frac{c}{2}
$$

此时 $R = \left\lceil \frac{s}{3} \right\rceil$。因为 $a \leqslant b \leqslant c$ ，所以 $c \geqslant \frac{s}{3}$，从而 $c \geqslant R$。所以可以先让黄色的人吃 $c$ 中的 $R$ 颗。接下来需要说明蓝色的人能吃满 $R$，也就是 $a$ 加上一部分 $b$ 足够补到 $R$。

由 $a \leqslant b \leqslant c$ 可得：

$$
2a \leqslant b + c
\implies a \leqslant \frac{a+b+c}{3}
\implies a \leqslant \frac{s}{3}
\implies a \leqslant \left\lceil \frac{s}{3} \right\rceil
\implies a \leqslant R
$$

同时，由当前情况 $\frac{s}{3} > \frac{c}{2}$ 可得：

$$
\frac{s}{3} > \frac{c}{2}
\implies \frac{a+b+c}{3} > \frac{c}{2}
\implies 2(a+b) > c
\implies 3(a+b) > a+b+c
\implies a+b > \frac{a+b+c}{3}
\implies a+b > \frac{s}{3}
\implies a+b \geqslant \left\lceil \frac{s}{3} \right\rceil
\implies a+b \geqslant R
$$

因为 $a+b$ 是整数，所以上面的 $a+b > \frac{s}{3}$ 可以推出 $a+b \geqslant \left\lceil \frac{s}{3} \right\rceil$。于是 $R-a \geqslant 0$、$a+b-R \geqslant 0$、$c-R \geqslant 0$，下面的分配量都是合法的。

因此，可以让蓝色的人吃完 $a$ 颗，再吃 $b$ 中的 $R-a$ 颗。最后让红色的人吃剩下的 $c-R$ 以及：

$$
b-(R-a)=a+b-R
$$

红色的人一共吃：

$$
c-R+a+b-R=a+b+c-2R
$$

由于：

$$
s=a+b+c
\implies \frac{s}{3} + 2 \cdot \frac{s}{3} = a+b+c
\implies \left\lceil \frac{s}{3} \right\rceil + 2 \cdot \left\lceil \frac{s}{3} \right\rceil \geqslant a+b+c
\implies a+b+c-2\left\lceil \frac{s}{3} \right\rceil \leqslant \left\lceil \frac{s}{3} \right\rceil
\implies a+b+c-2R \leqslant R
\implies c-R+a+b-R \leqslant R
$$

所以红色的人吃的数量也不超过上界 $R$，因此最大值为 $R$。

![eat_grapes_case2](../images/eat_grapes_solution2.png)

## 6. 复杂度

只需要计算总和与最大值。

- 时间复杂度： $O(1)$
- 空间复杂度： $O(1)$
