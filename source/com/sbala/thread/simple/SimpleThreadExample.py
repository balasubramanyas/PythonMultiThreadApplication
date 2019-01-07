'''
Created on Jan 5, 2019

@author: balasubramanyas
'''
import threading

class MyThreadClass(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self);
        self.name = threadName
        
    def run(self):
        print("Thread : " + self.getName() + " Started")
        print("Calling Method Print Numbers 1 to 10")
        self.printNumbers()
        print("Thread : " + self.getName() + " Done its Job")
        
        
    def printNumbers(self):
        for i in range(10):
            print(i)