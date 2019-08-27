#!/usr/bin/python3
# test_intpart2.py

import intpart
import filecmp

def run_test(args, expected, capsys):
    capturename = 'capturedstdout'
    fhd = open(capturename, 'w')
    cargs = intpart.checkArgs(args)
    intpart.partition(cargs)
    captured = capsys.readouterr()
    fhd.write(captured.out)
    fhd.close()
    assert filecmp.cmp(capturename, expected)

def test_intpart(capsys):
    test_cases = [ ['5'],
                   ['-o', '5'],
                   ['-e', '8'],
                   ['-r', '5'],
                   ['-s', '4'] ]
    expected_output = ['expected/5',
                       'expected/o5',
                       'expected/e8',
                       'expected/r5',
                       'expected/s4' ]
    for ind in range(len(test_cases)):
        run_test(test_cases[ind],
                 expected_output[ind],  
                 capsys)

    
