from numpy import random
import pandas as pd
class geneticoptimizer:
    def __init__(self,

                 popsize=20,
                 children=50,
                 generations=1000,
                 options={'mutate':True,
                          'custom_mutate':False,
                          'custom_mutate_func': None,
                          'mutation_decline': 0.98,
                          'crossover': True,
                          'custom_crossover': False,
                          'custom_crossover_func': None,
                          'dopar':True, 'cpu':1, 'alpha':0.5, 'beta':0.5, 'verbose':1}):

        self.popsize=popsize
        self.children =children
        self.generations=generations
        self.options=options

    def startOptimization(self, tfunc, initpar):

        self.parlen=len(initpar)

        Fitness={}
        Fitness['initial']=tfunc(initpar)
        Fitness['low']=Fitness['initial']
        Fitness['Generations'] = {}

        if self.options['mutate']:
            population=[self.mutatePar(initpar, self.options['alpha']) for x in range(self.generations)]
        if self.options['custom_mutate']:
            population=[globals()[self.options['custom_mutate_func']](initpar) for x in range(self.generations)]
        Fitness['Generations'][0] = [tfunc(cand) for cand in population]

        for gen in range(self.generations):
            children = [population[i] for i in random.choice(range(len(population)), size=self.children,
                                            p=self.generateProbability(Fitness['low'], Fitness['Generations'][gen]))]

            children=[self.modifyPar(cand, children, gen, self.options['mutation_decline']) for cand in children]
            childfit=[tfunc(child) for child in children]
            newindices=random.choice(range(len(children)),
                                                size=self.popsize,
                                                replace=False,
                                                p=self.generateProbability(Fitness['low'], childfit))

            population = [children[i] for i in newindices]
            Fitness['low']=(self.generations-gen)*Fitness['initial']+gen*min(childfit)
            Fitness['Generations'][gen+1] = [childfit[i] for i in newindices]

            print("Generation %d finished. Maximum Fitness: %d Minimum Fitness: %d" % (gen, max(Fitness['Generations'][gen+1]), min(Fitness['Generations'][gen+1])))

        return({"Population": population, "Fitness": Fitness})



    def generateProbability(self, low, fitness):
        maxfit=max(fitness)
        newlow=min(low, min(fitness))
        if maxfit==newlow:
            return [1/len(fitness) for f in fitness]
        else:
            weigths=[(f-newlow)/(maxfit-newlow) for f in fitness]
            sumw= sum(weigths)
            return([w/sumw for w in weigths])




    def modifyPar(self, x, population, gen, mutation_decline):
        if self.options['mutate']:
            x = self.mutatePar(x, self.options['alpha']*pow(mutation_decline,gen))
        if self.options['custom_mutate']:
            x = globals()[self.options['custom_mutate_func']](x)
        if self.options['crossover']:
            if self.options['beta'] > random.uniform(0, 1, 1):
                x = self.crossover(x, population[random.choice(range(len(population)))])
        if self.options['custom_crossover']:
            if self.options['beta'] > random.uniform(0, 1, 1):
                x = globals()[self.options['custom_crossover_func']](x, population)
        return(x.copy())

    def mutatePar(self, x, alpha):
        mutatevec = [r<alpha for r in random.uniform(0, 1, self.parlen)]
        newpar= [self.changeBit(b, m) for b, m in zip(x, mutatevec)]
        return(newpar.copy())

    def crossover(self, x1, x2):
        intersect1= random.choice(range(0,len(x1)-1))
        intersect2 = random.choice(range(intersect1, len(x1)))
        return(x1[:intersect1]+x2[intersect1:intersect2]+x1[intersect2:])

    def changeBit(self, bit, mutate):
        if mutate:
            if bit==0:
                bit=1
            else:
                bit=0
        return(bit)

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]






