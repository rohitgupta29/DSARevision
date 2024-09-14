"""
Here, ecvery stair have a cost. Can take one or 2 stairs. We can start from oth index or 1st index


"""



def minCostClimbingStairs(cost):

    return min(minCostRecursion(cost,0), minCostRecursion(cost,1))


def minCostRecursion(cost, index):

    if index >= len(cost):
        return 0
    # two choices
    takeOneStep = cost[index] + minCostRecursion(cost, index + 1)
    takeTwoSteps = cost[index] + minCostRecursion(cost,index + 2)

    return min(takeOneStep, takeTwoSteps)