#!/usr/bin/python3
# test_example6.py

import filecmp
import funcs

def test_f1f2(capsys):
    funcs.f1(3)
    funcs.f2(5)
    captureout, captureerr = capsys.readouterr()
    capturename = 'capturedstdout'
    fhd = open(capturename, 'w')
    fhd.write(captureout)
    fhd.close() # ensure that it has been saved
    assert filecmp.cmp(capturename, 'funcsexpected')

    

    
    
