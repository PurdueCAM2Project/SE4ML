#!/usr/bin/python3
# test_example3.py

def f1(x):
    return (x + 1)

def f2(x):
    return (x - 1)

def test_f1f2():
    assert f1(3) == 4
    assert f1(-3) == -2
    assert f2(3) == 4
    
    
