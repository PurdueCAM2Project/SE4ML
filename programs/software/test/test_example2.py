#!/usr/bin/python3
# test_example2.py

def returntrue():
    return False

def returnfalse():
    return True

def test_truefalse():
    assert returntrue() == True
    assert returnfalse() == False
    
