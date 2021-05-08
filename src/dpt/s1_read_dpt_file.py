import pickle
import os
from dpt import Dpt,DptSet,DptFull

save_path = r"/home/output_dpt"


with open(f"{save_path}/all_dpt",'rb') as dpt_file:
    all_dpt = DptSet.from_pickle(pickle.load(dpt_file))

    print(all_dpt[:1])
    print(len(all_dpt))
with open(f"{save_path}/dpt",'rb') as dpt_file:
    all_dpt = DptSet.from_pickle(pickle.load(dpt_file))

    print(all_dpt[:2])
    print(len(all_dpt))