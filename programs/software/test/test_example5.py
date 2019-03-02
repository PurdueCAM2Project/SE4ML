#!/usr/bin/python3
# test_example5.py

import funcs

def test_f1f2(capsys):
    funcs.f1(3)
    funcs.f2(5)
    captureout, captureerr = capsys.readouterr()
    capturename = 'capturedstdout'
    fhd = open(capturename, 'w')
    fhd.write(captureout)
    fhd.close()
    

    
    
