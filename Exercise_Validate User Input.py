# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:49:04 2021

@author: Situa
"""

#Prompt: Write a program that asks the user to provide a word, validate that it is a word, and print the word.

#install PyEnchant module if not already done
#pip install pyenchant

import enchant

#checking english dictionary
c = enchant.Dict("en_US")

#input the word
word = input("Word you want to check: ")

#check the word
c.check(word)

#if True is returned
if c.check(word)==True:
    print(word, "is an English word")
    
#if False is returned
else:
    print(word, "is not an English word")
#suggest some words
    print("Did you mean: ", c.suggest(word))
