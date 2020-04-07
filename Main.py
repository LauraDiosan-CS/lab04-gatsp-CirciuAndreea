from FileR import readNet, parseFile
from GA import *

def run(network,pop_sz,gen):
    N= network['noNodes']
    fcEval= routeFitness

    gaParam={'popSize': pop_sz, 'noGen': gen}
    problParam= {'function': fcEval, 'network': network}

    ga=GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestRepres=None

    for g in range(gaParam['noGen']):
        # ga.oneGeneration()
        ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()

        bestChromo= ga.bestChromosome()
        print('Best solution in generation '+ str(g+1) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))

    print("SOLUTION: ",bestChromo)

def main():
    while True:
        print("1. Introduceti numele fisierului de unde se vor colecta datele:")
        print("0. Exit")

        cmd= input()
        if cmd == "1":
            print("Introdceti nume fisier de intrare: ")
            fileName = input()
            if (fileName == "150p_eil51.txt"):
                print("Introduceti marimea populatiei:")
                pop_size = int(input())
                print("Introduceti numarul de generatii: ")
                generatii = int(input())
                network = parseFile(fileName)
                run(network, pop_size, generatii)
            if(fileName!=""):
                print("Introduceti marimea populatiei:")
                pop_size= int(input())
                print("Introduceti numarul de generatii: ")
                generatii= int(input())
                network= readNet(fileName)
                run(network, pop_size,generatii)


        else:
            break

main()