'''
Created on Jan 5, 2019

@author: balasubramanyas
'''
import com.sbala.thread.simple.SimpleThreadExample as ste

if __name__ == '__main__':
    print("Hi this is ThreadMain")
    mythread = ste.MyThreadClass("MyThread")
    mythread.start()
    print("Bye i'm leaving ThreadMain")
    pass