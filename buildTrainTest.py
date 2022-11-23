import pandas as pd
import numpy as np
import random

def main(): 

    #On lit le dataset que l'on a fait
    dataset = pd.read_csv("dataset.csv",sep=",").iloc[:,1:]


    #On groupe nos données par classe
    groupedDataset = dataset.groupby('class')

    #On va ensuite extraire 25 données par groupe pour servir de test
    groups = dataset["class"].unique()
    numberOfDatatest = 25

    #On initialise les jeux de données
    test = np.array([None,None,None,None,None,None,None])
    train = np.array([None,None,None,None,None,None,None])
    
    #On parcours l'ensemble des données pour extraire 25 données par groupe
    for x in groups:
        currentDatagroup = groupedDataset.get_group(x)
        testToAdd = currentDatagroup.sample(n=numberOfDatatest)
        indexToRemove = testToAdd.index
        test = np.vstack([test,testToAdd])
        train = np.vstack([train,currentDatagroup.drop(indexToRemove,axis=0)])

    #On retire la première ligne
    test = np.delete(test, 0, 0)
    train = np.delete(train, 0, 0)

    #On créé nos dataframe pandas
    headers = dataset.columns

    test = pd.DataFrame(test,columns=headers)
    train = pd.DataFrame(train,columns=headers)

    print(test)
    print(train)

    #On les sauvegarde

    test.to_csv("test.csv")
    train.to_csv("train.csv")
        


if __name__ == "__main__":
    main()