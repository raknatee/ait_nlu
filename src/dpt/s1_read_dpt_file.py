import pickle
import os
from dpt import Dpt,DptSet,DptFull

save_path = r"/home/output_dpt"


with open(f"{save_path}/dpt",'rb') as dpt_file:
    all_dpt = DptSet.from_pickle(pickle.load(dpt_file))
    print("n:",len(all_dpt))
    for i in range(len(all_dpt)):
        print(i,"/",len(all_dpt))


        print(all_dpt[i])
        input("press any key to continue\n")