import _PyPacwar
import numpy
import random
import sys
import re
import ast

# Example Python module in C for Pacwar
def main():
    ones = [1] * 50
    threes = [3] * 50
    depth = 3
    competitorSetSize = 3

    # blog2Test()
    # superSuperGeneTest(True, True, depth, competitorSetSize)

    # Results of initial recursive depth algorithm (depth 4, competitor size 8)
    # garbo1 = [0, 3, 1, 2, 0, 0, 0, 0, 1, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 1, 2, 1, 0, 2, 1, 3, 3, 3, 1, 3, 2, 2, 2, 3, 1, 1, 1, 1, 1, 0, 3, 3, 0, 3, 2, 2]
    # battleResults(garbo1, ones, False)
    # battleResults(garbo1, threes, False)
    #
    # It was trash, so adjusted to beat ones and threes:
    # garbo2 = [0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 1, 1, 3, 3, 1, 1, 3, 3, 3, 0, 3, 2, 1, 3, 3, 3, 0, 2, 3, 1, 3, 3, 1, 3, 3, 1, 2, 3, 1, 1, 1, 1, 1, 3, 3, 1, 0, 2, 0, 1]
    # battleResults(garbo2, ones, False)
    # battleResults(garbo2, threes, False)
    #
    # Two garbo genes battle it out:
    # battleResults(garbo1, garbo2, False)

    # goodGeneList = []
    # # The commented lines below are tests from my very first genes generated.
    # # goodGeneList.append([1, 0, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    # # goodGeneList.append([3, 0, 3, 3, 0, 0, 0, 0, 1, 3, 0, 3, 2, 3, 2, 3, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 0, 3, 2, 3, 3, 3, 0, 0, 3, 3, 3])
    # # battleResults(goodGeneList[0], goodGeneList[1], False)
    # goodGeneList.append([0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 2, 0, 3, 3, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 3, 1, 2, 1, 1, 2, 1, 1, 3, 1, 3, 1, 0, 1, 2, 1, 3, 0])
    # goodGeneList.append([0, 3, 1, 0, 0, 2, 1, 0, 0, 0, 1, 0, 2, 0, 2, 0, 0, 3, 3, 0, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 0, 3, 1, 1, 3, 1, 1, 3, 3, 0, 2, 0, 1, 2, 0])
    # goodGeneList.append([0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 3, 3, 3, 2, 3, 1, 2, 1, 3, 2, 1, 1, 2, 2, 3, 2, 3, 3, 2, 1, 1, 3, 0, 3, 3, 1, 1, 3, 0, 1, 0, 1])
    # goodGeneList.append([0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 2, 2, 0, 3, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 3, 1, 0])
    # goodGeneList.append([0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 3, 1, 2, 2, 2, 2, 3, 0, 3, 0, 3, 2, 1, 3, 2, 1, 3, 1, 1, 3, 1, 3, 3, 2, 2, 3, 2, 1, 1, 1, 3, 1, 3, 3, 2, 1, 0, 3, 1, 0])
    # goodGeneList.append([0, 1, 3, 3, 1, 0, 0, 0, 0, 0, 1, 3, 1, 2, 2, 1, 2, 0, 3, 3, 1, 2, 1, 3, 2, 3, 1, 1, 1, 3, 2, 1, 2, 2, 1, 2, 2, 3, 1, 3, 0, 3, 2, 3, 1, 0, 2, 3, 0, 0])
    # goodGeneList.append([0, 0, 1, 0, 3, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1, 2, 3, 3, 0, 1, 1, 2, 1, 1, 1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 2, 3, 3, 1, 1, 3, 1, 1, 2, 1, 2, 3, 1, 3, 0, 1])
    # goodGeneList.append([0, 2, 1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 2, 2, 1, 3, 0, 0, 0, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 0, 1, 3, 1, 3, 0, 0, 3, 2, 1])
    # goodGeneList.append([0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 0, 3, 0, 0, 3, 1, 1, 1, 1, 2, 3, 0, 3, 3, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 2, 3, 0, 3, 1, 1])
    # goodGeneList.append([0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0, 2, 3, 3, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 2, 2, 3, 2, 2, 1, 2, 1, 1, 0, 3, 0, 2, 3, 3, 3, 1])
    # goodGeneList.append([0, 0, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 0, 2, 1, 3, 3, 0, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2, 1, 1, 0, 1, 3, 0, 2, 0, 0, 3, 1, 3])
    # goodGeneList.append([3, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 2, 2, 0, 3, 3, 1, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 3, 2, 3, 3, 2, 3, 2, 2, 1, 0, 1, 1, 3, 0, 3, 1, 1, 0, 3])
    # goodGeneList.append([0, 3, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 0, 3, 3, 0, 1, 2, 1, 3, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1, 3, 2, 1, 3, 3, 1, 3, 0, 1, 3, 0, 3, 3, 0])
    # goodGeneList.append([3, 0, 0, 2, 0, 3, 0, 0, 1, 1, 0, 1, 2, 2, 2, 0, 3, 3, 3, 3, 1, 3, 2, 1, 1, 3, 2, 3, 3, 3, 2, 3, 2, 2, 3, 2, 3, 3, 1, 1, 3, 1, 1, 3, 2, 0, 1, 3, 1, 0])
    # goodGeneList.append([0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 3, 3, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 3, 2, 1, 1, 2, 1, 2, 3, 1, 3, 0, 1, 0, 1, 1, 1, 0, 3, 3, 3])
    # rankedGenes = iterateGeneSet(goodGeneList, 50, 17)
    # rankedGenes = rankGenes(goodGeneList, False)
    # print [geneDat[0] for geneDat in rankedGenes[:10]]
    # awesomerGene = adjustGeneToHandilyBeatOnesAndThrees(awesomeGene)

    # This is an amalgamation of the top 10 genes from the iterative algorithm after it found 20 new genes. Let's see
    # if something can strictly beat everything in THIS list. I'll relax the victory requirement to minimum 14 score
    # or something.

    # Disregard the above statement. I beat the above genes very easily. Now we perform the same process for a LONG
    # time, starting with the below set of genes, increasing set size to 40 to make sure the set's quality doesn't
    # decrease gradually over time (or at least limit this).
    # goodGeneList2 = [[0, 1, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 1, 0, 0, 0, 1, 1, 2, 1, 3, 2, 3, 3, 2, 3, 3, 3, 2, 3, 2, 2, 3, 2, 3, 3, 2, 3, 3, 1, 3, 2, 1, 3, 3, 1, 0],
    #                  [0, 3, 1, 3, 0, 3, 0, 0, 0, 3, 0, 3, 2, 0, 1, 0, 0, 3, 3, 3, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 1, 1, 3, 0, 0, 0, 1, 1, 3, 1],
    #                  [0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 3, 0, 1, 3, 1, 3, 3, 3, 2, 3, 3, 2, 3, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1, 0, 3, 1, 3, 2, 0, 3, 3, 1, 3],
    #                  [0, 3, 1, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 2, 1, 3, 1, 1, 3, 1, 0, 3, 1, 1, 3, 1],
    #                  [0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 3, 0, 0, 0, 1, 3, 1, 3, 2, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3],
    #                  [0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 3, 0, 1, 0, 1, 3, 1, 3, 2, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3],
    #                  [0, 1, 3, 1, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 0, 0, 0, 1, 1, 1, 1, 3, 1, 3, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 3, 2, 2, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3],
    #                  [0, 1, 3, 1, 0, 0, 0, 1, 0, 1, 1, 1, 2, 1, 0, 0, 0, 1, 0, 1, 1, 3, 0, 3, 2, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 1],
    #                  [0, 1, 3, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 2, 2, 2, 2, 3, 2, 2, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3],
    #                  [0, 1, 3, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1, 3, 3, 1, 3, 1, 1, 3, 3, 1, 3]]
    # rankGenes(goodGeneList2, False)

    # rankedGenes2 = iterateGeneSet(goodGeneList2, 500, 11, True, maxSetSize=40, startGene=goodGeneList2[-1], restartAtPreviousBestGene=True)
    # print rankedGenes2

    # try3 = []
    # try3.append([0, 3, 1, 0, 0, 3, 0, 0, 3, 0, 1, 0, 0, 3, 1, 0, 0, 3, 3, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 3, 2, 1, 3, 1, 1, 3, 1, 1, 2, 1, 1, 2, 1])
    # try3.append([0, 3, 1, 3, 0, 3, 1, 0, 0, 0, 2, 1, 3, 2, 2, 0, 3, 0, 1, 3, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 0, 1, 1, 2, 2, 1, 2, 3, 1, 0, 3, 1, 0, 0, 1, 3, 1, 1, 3, 1])
    # try3.append([0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 2, 0, 2, 0, 0, 0, 3, 1, 1, 2, 3, 3, 2, 3, 3, 1, 1, 1, 1, 2, 1, 2, 3, 3, 3, 3, 0, 1, 3, 0, 1, 0, 0, 0, 3, 3, 1, 3])
    # try3.append([3, 3, 3, 2, 0, 0, 3, 0, 3, 0, 3, 1, 2, 2, 2, 0, 3, 3, 3, 3, 2, 3, 3, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 2, 1, 0, 3, 1, 0, 1, 2, 1, 3, 1, 3, 3])
    # try3.append([3, 3, 3, 2, 0, 0, 3, 0, 1, 3, 3, 1, 2, 2, 2, 2, 3, 3, 3, 0, 2, 3, 3, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 2, 1, 0, 3, 1, 3, 3, 2, 0, 3, 1, 1, 0])
    # try3.append([3, 3, 3, 2, 0, 0, 0, 2, 1, 3, 3, 1, 2, 2, 2, 2, 3, 3, 3, 0, 2, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 2, 1, 0, 3, 1, 3, 3, 0, 1, 0, 1, 1, 0])
    # try3.append([3, 3, 3, 2, 0, 0, 0, 0, 1, 3, 3, 1, 2, 2, 2, 2, 3, 3, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 2, 1, 0, 3, 1, 3, 0, 0, 0, 0, 1, 1, 0])
    # try3.append([3, 3, 3, 2, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2, 2, 2, 3, 3, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1, 2, 3, 2, 1, 0, 3, 1, 1, 0, 0, 0, 1, 1, 1, 0])
    # try3.append([3, 3, 3, 2, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2, 2, 2, 3, 3, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1, 2, 3, 2, 1, 0, 3, 1, 1, 0, 0, 0, 0, 1, 1, 0])
    # try3.append([3, 3, 3, 2, 0, 0, 0, 0, 1, 1, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1, 2, 3, 2, 1, 0, 3, 1, 1, 0, 0, 0, 1, 1, 1, 0])
    # daGenes = iterateGeneSet(try3, 500, 16, True, 15, startGene=try3[0], mutateAmount=7, restartAtPreviousBestGene=True)
    # print daGenes

    # extractGenesFromFile("savedGenes.txt", "allGenesSet.txt")
    allOfTheAbove = readGenesFromFile("allGenesSet.txt")
    rankGenes(allOfTheAbove, False)

# Given a file with words and genes all jumbled together, extracts the genes (e.g. from log.txt) and outputs them all
# in target file.
def extractGenesFromFile(fileName, targetFileName):
    with open(fileName, "r") as f:
        with open(targetFileName, "w") as t:
            p = re.compile('\[.*\]')
            x = f.readline()
            while x:
                cool = p.findall(x)
                if cool:
                    for cool2 in cool:
                        t.write(cool2 + "\n")
                x = f.readline()

# Given a file with genes separated by newlines (if there is an existing file with genes not formatted like this, you
# can use the above method to automatically format it like so), reads them into a list and returns the list.
def readGenesFromFile(fileName):
    deGenes = []
    with open(fileName, "r") as f:
        x = f.readline()
        while x:
            listy = ast.literal_eval(x)
            deGenes.append(listy)
            x = f.readline()
    return deGenes

def generateRandomGene():
    gene = [0]*50
    for i in range(50):
        gene[i] = random.randint(0,3)
    return gene

# Finds a gene that beats all the genes in "genes". Then, adds this to the set, removes the worst gene, and repeats
# this process numIter times.
def iterateGeneSet(genes, numIter, minScore, wantToLog, maxSetSize = 15, startGene = generateRandomGene(), restartAtPreviousBestGene = False, mutateAmount = 4):
    open("log.txt", "w").close()
    prevBestGene = None
    for i in range(numIter):
        scoresAndGenes = rankGenes(genes, wantToLog)
        betterGene = []
        if prevBestGene is None:
            betterGene = hillClimbVSCompetitors(genes, True, True, True, startGene=startGene, restartThresholdScore=minScore, strictlyBeats=True, mutateAmount=mutateAmount)
        else:
            betterGene = hillClimbVSCompetitors(genes, True, True, True, startGene=prevBestGene, restartThresholdScore=minScore, strictlyBeats=True, mutateAmount=mutateAmount)
        if len(genes) >= maxSetSize:
            genes.remove(scoresAndGenes[len(genes) - 1][0])
        genes.append(betterGene)
        if restartAtPreviousBestGene:
            prevBestGene = list(betterGene)
        logMsg = "Iteration " + str(i + 1) + " has ended."
        print logMsg
        if wantToLog:
            with open("log.txt", "a") as f:
                f.write(logMsg)
    rankGenes(genes, wantToLog)
    return genes

# Given a list of genes, battles all of them round robin and ranks them.
def rankGenes(genes, wantToLog):
    n = len(genes)
    scores = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            iscore = battleScore(_PyPacwar.battle(genes[i], genes[j]))
            scores[i] += iscore / float(n)
            scores[j] += (20 - iscore) / float(n)
    scoresAndGenes = zip(genes, scores)
    scoresAndGenes.sort(lambda x, y : 1 if x[1] - y[1] > 0 else -1, None, True)
    r = 1
    for s in scoresAndGenes:
        logMsg = "Rank " + str(r) + ", avg score " + str(s[1]) + ": " + str(s[0]) + "."
        print logMsg
        if wantToLog:
            with open("log.txt", "a") as f:
                f.write(logMsg)
        r += 1
    return scoresAndGenes

# Requires that the given gene will beat ones and threes with an average score of >16.
# This won't be needed if setting strictlyBeats=True in superSuperGeneTest().
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
# aggregateCompetitors means every depth will pass its competitors to the next depth and add the competitor sets. Be
# careful as this will make runtime VERY HIGH.
def superSuperGeneTest(aggregateCompetitors, strictlyBeats, depth, competitorSize):
    open("log.txt", "w").close()
    zeroes = [0] * 50
    ones = [1] * 50
    twos = [2] * 50
    threes = [3] * 50

    awesomeGene, competitors = superSuperGeneHelper(competitorSize, 0, depth, aggregateCompetitors, strictlyBeats)
    logMsg = "Competitors in outermost depth: " + str(competitors + [ones, threes])
    print logMsg
    with open("log.txt", "a") as f:
        f.write(logMsg + "\n")
    battleResults(awesomeGene, ones, True)
    battleResults(awesomeGene, threes, True)

# Agg - whether to aggregate the lower depth's competitor set into the current depth's. This is tricky - for the base
# case where the competitor set is just [ones, threes], it returns NOTHING as the competitor set, because otherwise
# we would be appending many [ones, threes] to the depth above the base case depth.
def superSuperGeneHelper(competitorSetSize, depth, maxDepth, agg, strictlyBeats):
    logMsg = "Finding best gene in depth " + str(depth) + "..."
    print logMsg
    with open("log.txt", "a") as f:
        f.write(logMsg + "\n")
    ones = [1] * 50
    threes = [3] * 50
    if depth >= maxDepth:
        randOneThree = randOnesAndThreesStartFunction()
        return hillClimbVSCompetitors([list(ones), list(threes)], True, False, True, randOneThree, lambda: randOnesAndThreesStartFunction(), 11, strictlyBeats=strictlyBeats), None
    else:
        competitorSet = []
        for _ in range(competitorSetSize):
            results, prevCompetitors = superSuperGeneHelper(competitorSetSize, depth + 1, maxDepth, agg, strictlyBeats)
            competitorSet.append(list(results))
            if agg:
                if not prevCompetitors == None:
                    competitorSet += prevCompetitors
        logMsg = "Aggregated competitor set is: " + str(competitorSet + [list(ones), list(threes)])
        print logMsg
        with open("log.txt", "a") as f:
            f.write(logMsg + "\n")
        return hillClimbVSCompetitors(competitorSet + [list(ones), list(threes)], True, True, True, restartThresholdScore=13, strictlyBeats=strictlyBeats), competitorSet

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

# Hill climbs the starting gene until it can't get better. If restartUntilBetterFound == True, then it will
# repeat this process using random genes until a better one is found. Giving no restart function (None) will
# make the function attempt to randomly mutate the gene and continue the process...
def hillClimbVSCompetitors(competitors, restartUntilBetterFound, mutateOrNot, wantToLog, startGene=generateRandomGene(), restartFunction = None, restartThresholdScore = 10, strictlyBeats = False, mutateAmount = 4):
    current = startGene
    newBestScore = -9999999
    newBest = None
    newGeneSucks = False
    preMutateBest = None
    preMutateBestScore = 0
    roundsStuckAtMutation = 0
    roundsStuckThreshold = 200
    while 1:
        keepClimbing = False
        new = list(current)
        for i in range(len(current)):
            og = new[i]
            geneSucks = False
            for j in range(0,4):
                if new[i] == j:
                    continue
                new[i] = j
                totalScore = 0
                for competitor in competitors:
                    (rounds, c1, c2) = _PyPacwar.battle(new, competitor)
                    theScore = battleScore((rounds, c1, c2))
                    if strictlyBeats and theScore <= restartThresholdScore:
                        geneSucks = True
                        # print "Gene sucks! Only got score of " + str(theScore) + " while required is " + str(restartThresholdScore) + " versus gene " + str(competitor)
                    totalScore += theScore
                # print "Avg = " + str(float(totalScore) / len(competitors))
                if totalScore > newBestScore:
                    keepClimbing = True
                    newBestScore = totalScore
                    newBest = list(new)
                    newGeneSucks = geneSucks
                    # print "Found better gene with score " + str(newBestScore) + ". " + str(newBest)
            new[i] = og
        if keepClimbing:
            current = newBest
        else:
            if restartUntilBetterFound and (float(newBestScore) / len(competitors) <= restartThresholdScore or
                                            newGeneSucks):
                # print "Hill climb found local maxima, and it sucked with average score of " + \
                #       str(float(newBestScore)/len(competitors)) + "..."
                if mutateOrNot or restartFunction is None:
                    if newBestScore > preMutateBestScore:
                        preMutateBest = list(current)
                        preMutateBestScore = newBestScore
                        print "New Best Score: " + str(newBestScore)
                        roundsStuckAtMutation = 0
                    else:
                        roundsStuckAtMutation += 1
                        if roundsStuckAtMutation == roundsStuckThreshold:
                            print "Stuck at mutation for " + str(roundsStuckThreshold) + " rounds! Mega mutating."
                            # Fishy line below. This will most probably decrease the strength of the preMutateBest...
                            # Not sure if this is the correct approach.
                            preMutateBest = mutate(preMutateBest, wantToLog, mutateAmount * 2)
                            roundsStuckAtMutation = 0
                        current = list(preMutateBest)
                    current = mutate(current, wantToLog, mutateAmount)
                else:
                    current = restartFunction()
                newBest = None
                newBestScore = -9999999
                newGeneSucks = False
            else:
                logMsg = "Hill Climb found "
                if strictlyBeats:
                    logMsg += "strictly "
                logMsg += "better gene! " + str(current)
                print logMsg
                if wantToLog:
                    with open("log.txt", "a") as f:
                        f.write(logMsg + "\n")
                return current

# Generates a random gene and hill climbs as much as possible.
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
