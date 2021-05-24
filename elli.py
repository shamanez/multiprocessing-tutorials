import time
import threading
from datasets import Features, Sequence, Value, load_dataset,load_from_disk
import faiss
import random

stepCount = 0
isOtherThreadBusy = False
threadHandle = None

import multiprocessing

def indexed_function(text):
    

    print("Building Index")
    passages_path='/home/gsir059/Music/faisis_index_test/my_kb'
    dataset = load_from_disk(passages_path)
    print("dataset loaded")
    index = faiss.IndexHNSWFlat(768 ,128, faiss.METRIC_INNER_PRODUCT)
    dataset.add_faiss_index("embeddings", custom_index=index)
    print("Building Done")
    
    
def trainingStep():
    # do something heavy
    global stepCount
    global isOtherThreadBusy
    global threadHandle
    stepCount += 1
    #print("Training %d" % stepCount)
    #time.sleep(2)
    # tell the index builder to start working
    out_list=[]
    for i in range(1000000):
        out_list.append(random.random())
    
    if stepCount % 5 == 0:
        if not isOtherThreadBusy:
            # save the checkpoint
            #print("Saving Checkpoint and informing the other process")
            #time.sleep(1)
            # inform the index builder
            #threadHandle = threading.Thread(target=indexed_function, args=('haha',))
            threadHandle =multiprocessing.Process(target=indexed_function, args=('haha',))
            threadHandle.start()
            isOtherThreadBusy = True
        # else:
        #     print("Indexed builder is busy not saving checkpoint")
    if isOtherThreadBusy:
        #print("I am inside", threadHandle.is_alive())
        if not threadHandle.is_alive():
            # Do the index updating
            print("Loading new index")
            time.sleep(20)
            isOtherThreadBusy = False
        # else:
        #     print("still thread calculating")
  
while True:
    trainingStep()