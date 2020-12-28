import numpy as np
import random


def MarkovChainModel(src, n):
    with open(src, 'r', encoding='utf-8') as file:
        OGdata = file.read()
    OGList = OGdata.split(' ')
    indexList = list(dict.fromkeys(OGList))
    sentences = OGdata.split("\n\n")
    fWords = [i.split(' ')[0] for i in sentences]
    N = len(indexList)
    T = np.zeros((N, N))
    for i in range(len(OGList)-1):
        iword, jword = OGList[i], OGList[i+1]
        iIndex, jIndex = indexList.index(iword), indexList.index(jword)
        T[iIndex][jIndex] += 1
    for i in range(N):
        sum = np.sum(T[i])
        T[i] = T[i]/sum
    seq = [random.choice(fWords)]
    running = True
    step = 1
    while running:
        iwordn = seq[-1]
        iIndexn = indexList.index(iwordn)
        jwordn = random.choices(indexList, weights=list(T[iIndexn]), k=1)[-1]
        seq.append(jwordn)
        step += 1
        if step >= n and seq[-1] in [".", ". "]:
            running = False
    return seq
