import glob
import pandas as pd
import numpy as np

def main(): 

    allfiles = [f for f in glob.glob("dataset/*.csv")]
    print("Il y a "+ str(len(allfiles))+" fichiers")

    entireDataset = np.array([None,None,None,None,None,None,None])
    cpt = 0

    for x in allfiles:
        cpt+=1
        print(str(int((cpt/len(allfiles))*100))+"% completed")
        x = pd.read_csv(x,sep=",")
        x = x[:].values

        for i in range(0,x.shape[0],1):
            entireDataset = np.vstack([entireDataset, x[i][1:]])

    entireDataset = np.delete(entireDataset, 0, 0)

    headers = pd.read_csv(allfiles[0],sep=",").columns[1:]

    finalDataset = pd.DataFrame(entireDataset,columns=headers)

    print(finalDataset)

    finalDataset.to_csv("dataset.csv")


if __name__ == "__main__":
    main()