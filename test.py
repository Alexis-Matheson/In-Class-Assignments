#test.py Test case file for calculator.py
import pytest
from calculator import calcAdd, calcSub, calcMult, calcDiv

testNum = 14
testNum2 = 7

def testAdd(calcTest):
    assert calcAdd(testNum, testNum2) == 21

def testSub(calcTest):
    assert calcSub(testNum, testNum2) == 7

def testMult(calcTest):
    assert calcMult(testNum, testNum2) == 98

def testDiv(calcTest):
    assert calcDiv(testNum, testNum2) == 2