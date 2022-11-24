import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import cross_validate
from sklearn import preprocessing

def main(): 
    #On lit le dataset que l'on a fait
    dataset_train = pd.read_csv("train.csv",sep=",").iloc[:,1:]
    #On mélange pour notre cross-validation
    dataset_train = dataset_train.sample(frac=1)


    #On retire la colonne class
    labels = dataset_train["class"]
    labels = pd.factorize(dataset_train["class"])[0]
    dataset_train = dataset_train.drop("class",axis=1)

    scaler = preprocessing.StandardScaler().fit(dataset_train)
    dataset_train = scaler.transform(dataset_train)


    #Clustering avec un perceptron multiclasses
    K = 3

    result = cross_validate(Perceptron(),dataset_train,labels,cv=K,scoring=('r2', 'neg_mean_squared_error'),)
    print(result["score_time"])
    print(result["test_r2"])
    print(result['test_neg_mean_squared_error'])


    # dataset_test = pd.read_csv("test.csv",sep=",").iloc[:,1:]

    # #On retire la colonne class
    # labels = dataset_test["class"]
    # dataset_test = dataset_test.drop("class",axis=1)


if __name__ == "__main__":
    main()