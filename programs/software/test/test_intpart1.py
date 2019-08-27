#!/usr/bin/python3
# test_intpart1.py

import intpart
import filecmp

def run_test(args, expected, capsys):
    capturename = 'capturedstdout'
    fhd = open(capturename, 'w')
    args = intpart.checkArgs(args)
    intpart.partition(args)
    captured = capsys.readouterr()
    fhd.write(captured.out)
    fhd.close()
    assert filecmp.cmp(capturename, expected)

def test_intpart(capsys):
    run_test('3', 'expected/3', capsys)
    run_test('4', 'expected/4', capsys)
    run_test('5', 'expected/5', capsys)

    
