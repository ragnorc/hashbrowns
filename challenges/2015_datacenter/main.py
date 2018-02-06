# Set example values for testing

numRows = 2
numSlots = [5, 5]
numAvailableSlots = 9
unAvailableSlots = [(0, 0)]

# First elem is slot number, second ist capacity
servers = [(3, 10), (3, 10), (2, 5), (1, 5), (1, 1)]
serversByCap = sorted(servers, key=lambda x: x[1])
numServerSlots = 0

# Determine number of server slots
numServerSlots = sum([server[0] for server in servers])
numExceedingSlots = numServerSlots - numAvailableSlots

if(numExceedingSlots > 0):
    print (servers)
    print (serversByCap)
    print("hi")
