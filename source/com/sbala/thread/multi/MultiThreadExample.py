'''
Created on Jan 6, 2019

@author: balasubramanyas
'''
import threading
import time

isDoneThreadJob = False

class MyThreadClass(threading.Thread):

    def __init__(self, queObj, threadName, threadLock):
        threading.Thread.__init__(self)
        self.queObj = queObj
        self.name = threadName
        self.threadLock = threadLock
        
    def run(self):
        while(not isDoneThreadJob):
            if(self.queObj.empty()):
                self.threadLock.acquire()
                print("Sleeping " + self.getName())
                time.sleep(2)
                self.threadLock.release()
            else:
                self.threadLock.acquire()
                self.displayQueueData()
                self.threadLock.release()
        
        
        
    def displayQueueData(self):
        print("Thread " + self.getName() + " displayed " + self.queObj.get())
        