import graph
import itertools
import sys

# def printList(n):
#     if n > -1:
#         file = open("twelvenodes", "r")
#         li = []
#         for line in file:
#             line = line.split()
#             li.append(line[2])
#         file.close()
#         dist = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
#         count = 0
#         for row in range(n):
#             for col in range(row+1,n):
#                 elem = li.pop(0)
#                 dist[row][col] = elem
#                 dist[col][row] = elem
#         print(dist)



#printList(12)
def findCost():
    g = graph.Graph(-1, "euclidean_tsp.txt")
    return (g.tourValueAfterSwap([0,2,1,3,4]))
#print(findCost())

def printList(n):
    if n > -1:
        file = open("twelvenodes", "r")
        li = []
        for line in file:
            line = line.split()
            li.append(line[2])
        file.close()
        dist = [[0]*n for i in range(n)]
        for row in range(n):
            for col in range(row+1,n):
                elem = li.pop(0)
                dist[row][col] = elem
                dist[col][row] = elem
        print(dist)
#printList(12)

string1 = "137 263 376 231"
string2 = "32 84 145 222"
string1 = string1.split()
string2 = string2.split()
strings = [string1, string2]
strings = [[int(y) for y in x] for x in strings]
#print(strings)

def reverseList(i,j):
    li = [10,2,1,4,3,6,5,7,8,9,0,11]
    print(li[0:i])
    print(li[j:(i-1):-1])
    print(li[(j+1):])
    if i!=0:
        li = li[0:i] + li[j:(i-1):-1] + li[(j+1):]
    else:
        li = li[j:i:-1] + [li[0]] + li[(j+1):] 
    print (li)
#reverseList(0,2)



g = graph.Graph(-1, "cities50")
print(g.myAlgorithm())
# #print (g.dists)
# print(g.tourValue())
# g.swapHeuristic(12)
#g.TwoOptHeuristic(12)
#g.Greedy()
#print(g.tourValue())

 
def bruteForce(graph):
    allPerms = list(itertools.permutations(graph.perm[1:]))
    minCost = sys.maxsize
    for i in range (len(allPerms)):
        graph.perm = (0,) + allPerms[i]
        print(graph.perm)
        cost = graph.tourValue()
        if cost < minCost:
            minCost = cost
            minPerm = g.perm
    return (minCost, minPerm)

    # if n > -1:
    #     dist = [[0]*n for i in range(n)]
    #     file = open(filename, "r")
    #     li = []
    #     for line in file:
    #         line = line.split()
    #         li.append(line[2])
    #     file.close()
    #     for row in range(n):
    #         for col in range(row+1,n):
    #             elem = int(li.pop(0))
    #             dist[row][col] = elem
    #             dist[col][row] = elem

    # def convertMST(self,mst):
    #     convertedMST = [0]*len(mst)
    #     for i in range(len(mst)):
    #         neighbors = []
    #         for j in range(len(mst)):
    #             if mst[j] == i:
    #                 neighbors.append(j)
    #         convertedMST[i] = neighbors
    #     return convertedMST

    # def printMST(self, mst): 
    #     print ("Edge  Weight")
    #     for i in range(1, len(self.dists)): 
    #         print (mst[i], "-", i, "  ", self.dists[i][mst[i]] )

#     Finally, the last step of deleting duplicates can be achieved very simply:
# 1.	Iterate through each element e in the list returned by DFS and store its value.
# 2.	Compare e with all other elements in the list.
# 3.	If we find another element equal to e, delete it from the list.
# This is a very simple algorithm which will have complexity O(2*n), where n is the number of nodes in the graph, since the list returned by DFS will always have length greater than n, but smaller than 2*n (all nodes in the graph are visited more than once by DFS except leaf nodes).
