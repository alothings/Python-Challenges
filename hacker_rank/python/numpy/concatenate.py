"""
#####################################################################
Intro:

Task:

Input:

Output:

"""
import numpy as np
N, M, _ = map(int, input().split())
a, b = map(lambda x: np.array([input().split() for i in range(int(x))], int), [N, M])
print(np.concatenate((a, b), axis = 0))

