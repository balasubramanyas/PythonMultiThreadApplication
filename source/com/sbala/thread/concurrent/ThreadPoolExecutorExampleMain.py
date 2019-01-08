'''
Created on Jan 8, 2019

@author: balasubramanyas
'''

from concurrent.futures.thread import ThreadPoolExecutor

def printData(x):
    return x + 2

if __name__ == '__main__':
    values = [1,2,3,4]
    executor = ThreadPoolExecutor(2)
    # Submit method
    print("Executor.submit() : ")
    submitresultData = {executor.submit(printData, i) : i for i in values}
    for res in submitresultData:
        print(res.result())
        
    # Map method 
    print("Executor.map() : ")   
    mapresultData = executor.map(printData, values)
    for res in mapresultData:
        print(res)
    pass

