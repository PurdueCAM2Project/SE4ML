#!/usr/bin/python3
# test_example1.py

def returntrue():
    return True

def returnfalse():
    return False

def test_truefalse():
    assert returntrue() == True
    assert returnfalse() == False
    
