#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 11:22:17 2018

@author: Eyan
"""

class Array:
    
    def __init__(self,data):
        self.data = data
        
    def sum(self):
        return sum(self.data)