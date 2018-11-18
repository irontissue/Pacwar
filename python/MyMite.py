import _PyPacwar
import numpy
import random


# Example Python module in C for Pacwar
def main():
    ones = [1] * 50
    threes = [3] * 50

    # blog2Test()
    # superSuperGeneTest()

    # awesomeGene = [0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 1, 1, 3, 3, 1, 1, 3, 3, 3, 0, 3, 2, 1, 3, 3, 3, 0, 2, 3, 1, 3, 3, 1, 3, 3, 1, 2, 3, 1, 1, 1, 1, 1, 3, 3, 1, 0, 2, 0, 1]
    # awesomerGene = adjustGeneToHandilyBeatOnesAndThrees(awesomeGene)
    # # One example of awesomerGene:
    # awesomerGene = [0, 3, 1, 2, 0, 0, 0, 0, 1, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 1, 2, 1, 0, 2, 1, 3, 3, 3, 1, 3, 2, 2, 2, 3, 1, 1, 1, 1, 1, 0, 3, 3, 0, 3, 2, 2]
    # battleResults(awesomerGene, ones, False)
    # battleResults(awesomerGene, threes, False)
    # battleResults(awesomeGene, awesomerGene, False)

# Requires that the given gene will beat ones and threes with an average score of >16.
def adjustGeneToHandilyBeatOnesAndThrees(gene):
    ones = [1] * 50
    threes = [3] * 50
    return hillClimbVSCompetitors([list(ones), list(threes)], True, True, False, gene, None, 16)

# Recursively sets up groups of competitors for the hillclimb / mutate algorithm to fight against and beat.
# A depth of 4 and competitor set size 8 (which is actually size 10 due to the competitor set always containing ones
# and threes by default) took about 1.5 days to run on my laptop. The result was this gene:
# [0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 1, 1, 3, 3, 1, 1, 3, 3, 3, 0, 3, 2, 1, 3, 3, 3, 0, 2, 3, 1, 3, 3, 1, 3, 3, 1, 2, 3, 1, 1, 1, 1, 1, 3, 3, 1, 0, 2, 0, 1]
# But apparently this gene sucked vs threes (1-19 SMOKED) so I did a little extra mutation on it manually, requiring
# an average score of >16 vs ones and threes (see adjustGeneToHandilyBeatOnesAndThrees() above).
def superSuperGeneTest():
    open("log.txt", "w").close()
    zeroes = [0] * 50
    ones = [1] * 50
    twos = [2] * 50
    threes = [3] * 50

    maxDepth = 4
    competitorSetSize = 8
    awesomeGene = superSuperGeneHelper(competitorSetSize, 0, maxDepth)
    battleResults(awesomeGene, ones, True)
    battleResults(awesomeGene, threes, True)

def superSuperGeneHelper(competitorSetSize, depth, maxDepth):
    logMsg = "Finding best gene in depth " + str(depth) + "..."
    print logMsg
    with open("log.txt", "a") as f:
        f.write(logMsg + "\n")
    ones = [1] * 50
    threes = [3] * 50
    if depth >= maxDepth:
        randOneThree = randOnesAndThreesStartFunction()
        return hillClimbVSCompetitors([list(ones), list(threes)], True, True, True, randOneThree, lambda:randOnesAndThreesStartFunction(), 15)
    else:
        competitorSet = [list(ones), list(threes)]
        for _ in range(competitorSetSize):
            competitorSet.append(list(superSuperGeneHelper(competitorSetSize, depth + 1, maxDepth)))
        return hillClimbVSCompetitors(competitorSet, True, True, True)

def randOnesAndThreesStartFunction():
    randOneThree = []
    while len(randOneThree) < 50:
        toAppend = [random.randint(1, 2) * 2 - 1] * random.randint(1, 15)
        randOneThree += toAppend
    return randOneThree[:50]

def blog2Test():
    zeroes = [0] * 50
    ones = [1] * 50
    twos = [2] * 50
    threes = [3] * 50

    competitors = [list(ones), list(threes)]
    testGene = hillClimbVSCompetitors(competitors, False, True, False, threes)
    battleResults(testGene, ones, False)
    battleResults(testGene, threes, False)

    while 1:
        if len(competitors) > 5:
            del competitors[2]
        competitors.append(list(testGene))
        testGene = hillClimbVSCompetitors(competitors, False, False, False, testGene)
        battleResults(testGene, ones, False)
        battleResults(testGene, threes, False)

def test1BeatOnesAndThrees():
    zeroes = [0] * 50
    ones = [1] * 50
    twos = [2] * 50
    threes = [3] * 50

    testGene = hillClimbVSCompetitors((ones, threes), False, False, False, threes)
    battleResults(testGene, ones, False)
    battleResults(testGene, threes, False)

    testGene2 = hillClimbVSCompetitors((ones, threes), False, False, False, ones)
    battleResults(testGene, ones, False)
    battleResults(testGene, threes, False)

    testGene3 = hillClimbVSCompetitors((testGene, testGene2, ones, threes), False, False, False, testGene)
    battleResults(testGene3, ones, False)
    battleResults(testGene3, threes, False)

    testGene4 = hillClimbVSCompetitors((testGene, testGene2, ones, threes), False, False, False, testGene2)
    battleResults(testGene4, ones, False)
    battleResults(testGene4, threes, False)

#Prints results of a battle between 2 genes in a nice format.
def battleResults(gene1, gene2, wantToLog):
    print "gene1: " + str(gene1)
    print "gene2: " + str(gene2)
    (rounds, c1, c2) = _PyPacwar.battle(gene1, gene2)
    gene1Score = battleScore((rounds, c1, c2))
    gene2Score = 20 - gene1Score
    print "Number of rounds:", rounds
    print "gene1 PAC-mites remaining:", c1
    print "gene2 PAC-mites remaining:", c2
    print "gene1 score: " + str(gene1Score) + ". gene2 score: " + str(gene2Score)
    print ""
    if wantToLog:
        with open("log.txt", "a") as f:
            f.write("gene1: " + str(gene1) + "\n")
            f.write("gene2: " + str(gene2) + "\n")
            f.write("Number of rounds:" + str(rounds) + "\n")
            f.write("gene1 PAC-mites remaining:" + str(c2) + "\n")
            f.write("gene2 PAC-mites remaining:" + str(c2) + "\n")
            f.write("gene1 score: " + str(gene1Score) + ". gene2 score: " + str(gene2Score) + "\n")
            f.write("\n\n")

#The scoring system of pacwar. Returns the relative score for gene 1, if the battleResults = (rounds, c1, c2).
#This is anywhere from 0 to 20:
#20-0	Destroying the opposing species in under 100 rounds
#19-1	Destroying the opposing species in 100-199 rounds
#18-2	Destroying the opposing species in 200-299 rounds
#17-3	Destroying the opposing species in 300-500 rounds
#13-7	Outnumbering the opponent by at least 10:1 after 500 rounds
#12-8	Outnumbering the opponent by between 3:1 and 10:1 after 500 rounds
#11-9	Outnumbering the opponent by between 1.5:1 and 3:1 after 500 rounds
#10-10	If neither species outnumbers the other by more than 1.5:1 after 500 rounds
def battleScore(results):
    if results[0] <= 500 and (results[1] == 0 or results[2] == 0) and not(results[1] == 0 and results[2] == 0):
        modifier = (results[1] - results[2]) / abs(results[1] - results[2])
        if results[0] < 100:
            return 10 + modifier * 10
        elif results[0] < 200:
            return 10 + modifier * 9
        elif results[0] < 300:
            return 10 + modifier * 8
        elif results[0] <= 500:
            return 10 + modifier * 7
    else:
        ratio = float(results[1]) / results[2]
        if ratio <= 0.1:
            return 7
        elif ratio <= 1/3.0:
            return 8
        elif ratio <= 1/1.5:
            return 9
        elif ratio <= 1.5:
            return 10
        elif ratio <= 3:
            return 11
        elif ratio <= 10:
            return 12
        else:
            return 13

def generateRandomGene():
    gene = [0]*50
    for i in range(50):
        gene[i] = random.randint(0,3)
    return gene

# Hill climbs the starting gene until it can't get better. If restartUntilBetterFound == True, then it will
# repeat this process using random genes until a better one is found. Giving no restart function (None) will
# make the function attempt to randomly mutate the gene and continue the process...
def hillClimbVSCompetitors(competitors, restartUntilBetterFound, mutateOrNot, wantToLog, startGene=generateRandomGene(), restartFunction = None, restartThresholdScore = 10):
    current = startGene
    newBestScore = -9999999
    newBest = None
    while 1:
        for i in range(len(current)):
            for j in range(0,4):
                new = list(current)
                if current[i] == j:
                    continue
                new[i] = j
                totalScore = 0
                for competitor in competitors:
                    (rounds, c1, c2) = _PyPacwar.battle(new, competitor)
                    totalScore += battleScore((rounds, c1, c2))
                if totalScore > newBestScore:
                    newBestScore = totalScore
                    newBest = new
                    # print "Found better gene with score " + str(newBestScore) + ". " + str(newBest)
        if newBest != current:
            current = newBest
        else:
            if restartUntilBetterFound and float(newBestScore) / len(competitors) <= restartThresholdScore:
                # print "Hill climb found local maxima, and it sucked with average score of " + \
                #       str(float(newBestScore)/len(competitors)) + "... Restarting with random gene."
                if mutateOrNot or restartFunction is None:
                    current = mutate(current, wantToLog, 3)
                else:
                    current = restartFunction()
                newBest = None
                newBestScore = -9999999
            else:
                logMsg = "Hill Climb found better gene! " + str(current)
                print logMsg
                if wantToLog:
                    with open("log.txt", "a") as f:
                        f.write(logMsg + "\n")
                return current

def hillClimb():
    current = generateRandomGene()
    newBestScore = -9999999
    newBest = None
    while 1:
        for i in range(len(current)):
            for j in range(0,4):
                new = list(current)
                if current[i] == j:
                    continue
                new[i] = j
                (rounds, c1, c2) = _PyPacwar.battle(new, current)
                thisScore = battleScore((rounds, c1, c2))
                if thisScore >= newBestScore:
                    newBestScore = thisScore
                    newBest = new
        if newBest != current:
            current = newBest
        else:
            return current

# Randomly changes num bits in the gene.
def mutate(gene, wantToLog, num = 1):
    logMsg = "Mutating " + str(num) + "..."
    print logMsg
    if wantToLog:
        with open("log.txt", "a") as f:
            f.write(logMsg + "\n")
    geneCopy = list(gene)
    idxPool = range(50)
    for _ in range(num):
        randIdxPoolIdx = random.randint(0, len(idxPool) - 1)
        randIdx = idxPool[randIdxPoolIdx]
        newRand = random.randint(0, 3)
        while newRand == geneCopy[randIdx]:
            newRand = random.randint(0, 3)
        geneCopy[randIdx] = newRand
        idxPool.pop(randIdxPoolIdx)
    return geneCopy

if __name__ == "__main__": main()
