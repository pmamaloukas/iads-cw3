import graph
import random
import itertools
import sys
import math

def generateEuclideanGraph(numOfNodes, widthOfPlane, heightOfPlane):
    file = open("euclideanFile.txt", "w")
    for i in range(numOfNodes):
        file.write(str(random.randint(0, widthOfPlane+1)) + "  " + str(random.randint(0, heightOfPlane+1)) + "\n")

def generateGeneralGraph (numOfNodes, maxDistance):
    file = open("generalGraph.txt", "w")
    for i in range(numOfNodes):
        for j in range(i+1, numOfNodes):
            file.write(str(i) + " " + str(j) + " " + str(random.randint(1, maxDistance)) + "\n")

def generateLargeGraph(numOfNodes, y, maxWidth):
    file = open("largeGraph.txt", "w")
    start = 0
    width = maxWidth // numOfNodes
    for i in range (numOfNodes):
        file.write(str(random.randint(start, width)) + " " + str(y) + "\n")
        start = width
        width += (maxWidth // numOfNodes)

def bruteForce(graph):
    allPerms = list(itertools.permutations(graph.perm[1:]))
    minCost = sys.maxsize
    for i in range (len(allPerms)):
        graph.perm = [0] + list(allPerms[i])
        cost = graph.tourValue()
        if cost < minCost:
            minCost = cost
            minPerm = graph.perm
    return minCost

def testGeneralSmall(numOfNodes):
    comparisons = []
    for i in range(10):
        generateGeneralGraph(numOfNodes, random.randint(5,101))
        g1 = graph.Graph(numOfNodes, "generalGraph.txt")
        g2 = graph.Graph(numOfNodes, "generalGraph.txt")
        g3 = graph.Graph(numOfNodes, "generalGraph.txt")
        g4 = graph.Graph(numOfNodes, "generalGraph.txt")
        g2.swapHeuristic(-1)
        g2.TwoOptHeuristic(-1)
        g3.Greedy()
        g4.myAlgorithm()
        comparisons.append([bruteForce(g1), g2.tourValue(), g3.tourValue(), g4.tourValue()])
    return comparisons

# print(testGeneralSmall(5))
# print(testGeneralSmall(8))
# print(testGeneralSmall(10))

def testEuclideanSmall(numOfNodes):
    comparisons = []
    for i in range(10):
        generateEuclideanGraph(numOfNodes, random.randint(5,101), random.randint(5,101))
        g1 = graph.Graph(-1, "euclideanFile.txt")
        g2 = graph.Graph(-1, "euclideanFile.txt")
        g3 = graph.Graph(-1, "euclideanFile.txt")
        g4 = graph.Graph(-1, "euclideanFile.txt")
        g2.swapHeuristic(-1)
        g2.TwoOptHeuristic(-1)
        g3.Greedy()
        g4.myAlgorithm()
        comparisons.append([bruteForce(g1), g2.tourValue(), g3.tourValue(), g4.tourValue()])
    return comparisons

# print(testEuclideanSmall(5))
# print(testEuclideanSmall(8))
# print(testEuclideanSmall(10))

def testLarge(numOfNodes):
    comparisons = []
    for i in range(10):
        generateLargeGraph(numOfNodes, random.randint(0,500), random.randint(0,500))
        g1 = graph.Graph(-1, "largeGraph.txt")
        g2 = graph.Graph(-1, "largeGraph.txt")
        g3 = graph.Graph(-1, "largeGraph.txt")
        g4 = graph.Graph(-1, "largeGraph.txt")
        g2.swapHeuristic(-1)
        g2.TwoOptHeuristic(-1)
        g3.Greedy()
        g4.myAlgorithm()
        comparisons.append([g1.tourValue(), g2.tourValue(), g3.tourValue(), g4.tourValue()])
    return comparisons

# print(testLarge(20))
# print(testLarge(50))
# print(testLarge(100))