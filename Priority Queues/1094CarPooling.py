


data = [[2,1,5], [3,3,7]]
data_2 = 5
def carpooling(trips, capacity):

    if len(trips) == 0:
        return

    for i in range(1, len(trips)):

        if trips[i][1] < trips[i-1][2]:
            tot_pass = trips[i][0] + trips[i-1][0]

        if tot_pass > capacity:
            return False

    return True

res = carpooling(trips= data, capacity= data_2)

print(res)
