import time
import threading
from datasets import Features, Sequence, Value, load_dataset,load_from_disk
import faiss
stepCount = 0
isOtherThreadBusy = False
threadHandle = None



csv_path='/home/gsir059/Desktop/covid-19-preprocess/final_data/my_knowledge_dataset.csv'

print("Building Index")
passages_path='/home/gsir059/Music/faisis_index_test/my_kb'
dataset = load_from_disk(passages_path)
print('dataset loaded')
index = faiss.IndexHNSWFlat(768 ,128, faiss.METRIC_INNER_PRODUCT)
dataset.add_faiss_index("embeddings", custom_index=index)
print("Building Done")
