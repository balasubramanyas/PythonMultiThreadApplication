'''
Created on Jan 6, 2019

@author: balasubramanyas
'''
import com.sbala.thread.multi.MultiThreadExample as mte
import queue
import threading
if __name__ == '__main__':
    
    workQueue = queue.Queue(20)
    queueLock = threading.Lock()
    thread1 = mte.MyThreadClass(workQueue, "BalaThread-1", queueLock)
    thread2 = mte.MyThreadClass(workQueue, "BalaThread-2", queueLock)
    thread3 = mte.MyThreadClass(workQueue, "BalaThread-3", queueLock)
    for i in range(20):
        workQueue.put("Data_" + str(i))
        
    thread1.start()
    thread2.start()
    thread3.start()
    
    while(True):
        if(workQueue.empty()):
            mte.isDoneThreadJob = True
            break
             
    pass