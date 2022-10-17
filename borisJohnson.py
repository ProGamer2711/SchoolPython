def getInput():
    maxBoatTrips = int(input(
        "Max number of boat trips Boris Johnson can make\n> "))

    weightsString = input(
        "Weights of Boris Johnson's goats\n> ")
    weights = weightsString.split(" ")

    for (idx, weight) in enumerate(weights):
        weights[idx] = int(weight)

    minBoatCapacity = max(weights)

    return (maxBoatTrips, weights, minBoatCapacity)


def findNextWeight(weights, freeCapacity):
    maxWeightThatFits = False

    for weight in weights:
        if (weight > maxWeightThatFits and weight <= freeCapacity):
            maxWeightThatFits = weight

    return maxWeightThatFits


def calculateCapacity(maxBoatTrips, weights, boatCapacity):
    weightsCopy = weights.copy()

    for i in range(maxBoatTrips):
        usedCapacity = 0

        while usedCapacity <= boatCapacity:
            if len(weightsCopy) <= 0:
                return boatCapacity

            freeCapacity = boatCapacity - usedCapacity
            nextWeight = findNextWeight(weightsCopy, freeCapacity)

            if not nextWeight:
                break

            usedCapacity += nextWeight
            weightsCopy.remove(nextWeight)

    if len(weightsCopy) > 0:
        return calculateCapacity(maxBoatTrips, weights, boatCapacity + 1)

    return boatCapacity


maxBoatTrips, weights, boatCapacity = getInput()
capacityNeeded = calculateCapacity(maxBoatTrips, weights, boatCapacity)

print(f"The minimum capacity of Boris Johnson's boat is {capacityNeeded}")
