'''
链接：https://www.nowcoder.com/questionTerminal/14c0359fb77a48319f0122ec175c9ada
来源：牛客网

[Chinese Version]
[编程题]吃葡萄
有三种葡萄，每种分别有a,b,c颗。有三个人，第一个人只吃第1,2种葡萄，第二个人只吃第2,3种葡萄，第三个人只吃第1,3种葡萄。
适当安排三个人使得吃完所有的葡萄,并且且三个人中吃的最多的那个人吃得尽量少。

1 <= a, b, c <= 10^18

[English Version]
There are three kinds of grapes, each with a, b, and c pieces, respectively.
There are three individuals,
the first person only eats the 1st and 2nd types of grapes,
the second person only eats the 2nd and 3rd types,
and the third person only eats the 1st and 3rd types.
They should eat up all of the grapes,
and the person who eats the most should eat as little as possible.
Return the max

1 <= a, b, c <= 10^18
'''

import sys


def find_min_max(a, b, c):
    return max((a + b + c + 3 - 1) // 3, (max(a, b, c) + 2 - 1) // 2)

def main():
    for line_index, line in enumerate(sys.stdin):
        if line_index == 0:
            num_inputs = int(line.strip())
            continue

        a, b, c = [int(argument_str) for argument_str in line.strip().split()]
        result = find_min_max(a, b, c)

        print(result)

if __name__ == '__main__':
    main()
