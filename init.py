from loading.loader import loader
from optimization.geneticAlgorithm import geneticoptimizer


#loader= loader("data/tabular/iris.csv")

def fx(par):
    return(sum(par))

initpar = [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0]

genopt=geneticoptimizer()
solution = genopt.startOptimization(tfunc=fx, initpar=initpar)


test=1