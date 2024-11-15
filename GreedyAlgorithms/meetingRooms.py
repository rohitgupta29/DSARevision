



meetings = [(0,5), (10,20),(3,7)]

def meetingRooms(meetings):

    meetings = sorted(meetings)

    for i in range(1, len(meetings)):

        if meetings[i][0] < meetings[i-1][1]:

            return False

    return True


res = meetingRooms(meetings)

print(res)