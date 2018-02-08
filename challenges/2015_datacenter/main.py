import itertools

# Set example values for testing

numRows = 2
numSlots = 5
numAvailableSlots = 9
unAvailableSlots = [(0, 0)]
# Create list of row lists containing booleans to mark if the slot is available
rows = [[False if (x, y) in unAvailableSlots else True for y in range(
    numSlots)] for x in range(numRows)]
# print(rows)

# (index, slot number, capacity)
servers = [(0, 3, 10), (1, 3, 10), (2, 2, 5), (3, 1, 5), (4, 1, 1)]

# Determine number of (exceeding) server slots
numServerSlots = sum([server[0] for server in servers])
numExceedingSlots = numServerSlots - numAvailableSlots

# Change making problem: Brute force method to remove servers with the least capacity. To be improved as complexity is worst.


def removeServers(numExceedingSlots, servers):
    if(numExceedingSlots > 0):

        minCapacity = 1000000000
        tuplesToDelete = []
    for a, b in itertools.combinations(filter(lambda x: x[1] <= numExceedingSlots, servers), 2):
        if a[1] == numExceedingSlots and a[2] < minCapacity:
            tuplesToDelete = [(a[0], a[1], a[2])]
            minCapacity = a[2]
        if b[1] == numExceedingSlots and b[2] < minCapacity:
            minCapacity = b[2]
            tuplesToDelete = [(b[0], b[1], b[2])]

        if (a[1]+b[1] == numExceedingSlots and (a[2]+b[2]) < minCapacity):
            minCapacity = a[2]+b[2]
            tuplesToDelete = [(a[0], a[1], a[2]), (b[0], b[1], b[2])]

    for t in tuplesToDelete:
        servers.remove(t)
    return servers


servers = removeServers(numExceedingSlots, servers)


# Row slot allocation: First fit decreasing algorithm. To be improved as complexity is bad.

def rowSlotAllocate(servers, numSlots, rows):
    serversByCapacity = sorted(servers, key=lambda x: x[2], reverse=True)
    print(serversByCapacity)
    print(rows)
    reverse = False
    elemOfServer = 0
    while len(serversByCapacity) > 0:
        print (reverse)

        for y in range(0, numRows):
            for x in range(0, numSlots):
                if len(serversByCapacity) > 0:
                        # print(server)
                    print("elemofSever " + str(elemOfServer))
                    print("serverbycap: "+str(len(serversByCapacity)))
                    if reverse:
                        elemOfServer = len(serversByCapacity)-1

                    else:
                        elemOfServer = 0
                    if (x+serversByCapacity[elemOfServer][1] <= len(rows[y])):
                        if all(rows[y][x:(x+serversByCapacity[elemOfServer][1])]):
                            print("Allocate server: " +
                                  str(serversByCapacity[elemOfServer][0])+"at slot: "+str(x)+"of row: "+str(y))
                            rows[y][x:(x+serversByCapacity[elemOfServer][1])
                                    ] = itertools.repeat(False, (x+serversByCapacity[elemOfServer][1]-x))
                            del serversByCapacity[elemOfServer]
                            print(serversByCapacity)
                            print(rows)
                            break
                    else:
                        # Reset loop with next server: elemOfServer+1
                        print("No place found for server"+str(
                            serversByCapacity[elemOfServer][0])+"at slot: "+str(x)+"of row: "+str(y))
        reverse = not reverse


rowSlotAllocate(servers, numSlots, rows)
