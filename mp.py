#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:05:57 2018

@author: Eyan
"""

iimport multiprocessing as mp
import time
import os

q = mp.Queue()  #FIFO
a_list = []

def worker(x, num):
    pid = os.getpid()
    print(f'I am process {num} with pid {pid}')
    time.sleep(5)
    q.put(x ** 2)
    a_list.append(x ** 2)

if __name__ == '__main__':
    pid = os.getpid()
    print(f'Main has pid {pid}')
    p1 = mp.Process(target=worker, args=(5, 1))
    p2 = mp.Process(target=worker, args=(15, 2))
    p1.start()
    p2.start()

    print(f'first item in queue {q.get()}')
    print(f'second item in queue {q.get()}')
    print('the list ', a_list)
