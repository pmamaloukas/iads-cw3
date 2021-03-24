import math
import random
import operator
import sys

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)

def lineCount(file): #helper function 
        lines = 0
        for line in file:
            if (line != "\n") and (line != " "):
                lines += 1
        return lines

def nInit(n, filename):
    nValue = 0
    if n > -1:
        nValue = n
    else:
        file = open(filename,"r")
        nValue = lineCount(file)
        file.close()
    return nValue

def permInit (n, filename):
    perm = []
    if n > -1:
        for i in range(n):
            perm.append(i)
    else:
        file = open(filename, "r")
        size = lineCount(file)
        for i in range(size):
            perm.append(i)
    return perm

def distInit(n, filename):
    if n > -1:
        dist = [[0]*n for i in range(n)]
        file = open(filename, "r")
        li = []
        for line in file:
            line = line.split()
            li.append((int(line[0]), int(line[1]), int(line[2])))
        file.close()
        for i in range(len(li)):
            dist[ li[i][0] ] [ li[i][1] ] = li[i][2]
            dist[ li[i][1] ] [ li[i][0] ] = li[i][2]
    else:
        file = open(filename, "r")
        count = 0
        li = []
        for line in file:
            if (line != "\n") and (line != " "):
                count += 1
                line = line.split()
                li.append(line)
        dist = [[0]*count for i in range(count)]
        li = [[int(y) for y in x] for x in li]
        file.close()
        for row in range(count):
            for col in range(count):
                dist[row][col] = euclid(li[row], li[col])
    return dist
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        self.filename = filename
        self.n = nInit(n, filename)
        self.perm = permInit(n, filename)
        self.dists = distInit(n, filename)

    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        cost = 0
        for i in range(len(self.perm)-1):
            cost += self.dists[self.perm[i]][self.perm[i+1]]
        cost += self.dists[self.perm[-1]][self.perm[0]]
        return cost
    
    def swapHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True
    
    # Attempt the swap of cities i and i+1 in self.perm and commit
    # to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        costBefore = self.tourValue()
        testPerm = self.perm[:]

        pos = i % len(self.perm)
        nextPos = (i+1) % len(self.perm)

        temp = self.perm[pos]
        self.perm[pos] = self.perm[nextPos]
        self.perm[nextPos] = temp

        costAfter = self.tourValue()
        if costAfter < costBefore:
            return True
        else:
            self.perm = testPerm[:]
            return False


    def TwoOptHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
    # # Consider the effect of reversiing the segment between
    # # self.perm[i] and self.perm[j], and commit to the reversal
    # # if it improves the tour value.
    # # Return True/False depending on success.              
    def tryReverse(self,i,j):
        costBefore = self.tourValue()
        testPerm = self.perm[:]

        start = i % len(self.perm)
        end = j % len(self.perm)

        head = self.perm[0:start]
        middle = self.perm[end:(start-1):-1]
        tail = self.perm[(end+1):]
        if start != 0:
            self.perm = head + middle + tail
        else:
            self.perm = self.perm[end:start:-1] + [self.perm[0]] + tail
        costAfter = self.tourValue()
        if costAfter < costBefore:
            return True
        else:
            self.perm = testPerm[:]
            return False
                  
    # # Implement the Greedy heuristic which builds a tour starting
    # # from node 0, taking the closest (unused) node as 'next'
    # # each time.

    def Greedy(self):
        unused = self.perm[1:]
        testPerm = []
        testPerm.append(0)
        while len(unused) > 0:
            distanceFrom = self.dists[testPerm[-1]]
            minNode = unused[0]
            minDistance = distanceFrom[minNode]
            for i in range(len(unused)):
                elem = unused[i] 
                if minDistance > distanceFrom[elem]:
                    minDistance = distanceFrom[elem]
                    minNode = elem
            testPerm.append(minNode)
            unused.remove(minNode)
        self.perm = testPerm


    #PART C

    def minKey(self, keys, li): #helper function
        min = sys.maxsize
        node = 0
        for i in range(len(self.dists)):
            if keys[i] < min and i not in li:
                min = keys[i]
                node = i
        return node

    def prim(self):
        includedNodes = []
        numOfNodes = len(self.dists)
        mst = [-1] + ([None]*(numOfNodes-1)) #list to store mst - at index i we store the parent of node i (starting node has no parent, hence the -1)
        keys = [0] + ([sys.maxsize]*(numOfNodes-1))
        while len(includedNodes) != numOfNodes:
            node = self.minKey(keys,includedNodes)
            includedNodes.append(node)
            for i in range(numOfNodes):
                if self.dists[node][i] > 0 and i not in includedNodes and keys[i] > self.dists[node][i]:
                    keys[i] = self.dists[node][i]
                    mst[i] = node
        #self.printMST(mst)
        return mst

    def dfs (self, mst, root, path, neighbors):
        path.append(root)
        for i in range(len(mst)):
            if mst[i] == root:
                neighbors.append(i)
        for i in neighbors:
            newRoot = neighbors.pop()
            self.dfs(mst,newRoot,path,neighbors)
        return path

    def myAlgorithm(self):
        mst = self.prim()
        self.perm = self.dfs(mst,0,[],[])