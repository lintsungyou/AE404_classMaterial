# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:40:44 2023

@author: user
"""
import sys, math
IS_DEBUG = False
CROSS = 10
DIVIDE = 11

def bugPrint(_inpStr):
    if IS_DEBUG:
        bugPrint(_inpStr)

def cleanCrossDevideList(_numberTotal, _crossDivideOperands, _crossDivideOperators):
    res = float(_numberTotal)
    while len(_crossDivideOperators) > 0 :
        operand = _crossDivideOperands.pop()
        operator = _crossDivideOperators.pop()
        if operator == CROSS:
            res = res * operand
        if operator == DIVIDE:
            res = res / operand
    return res

def calByFormula(formulaStr):
    total = 0.0;
    forSize = len(formulaStr)
    if IS_DEBUG:
        bugPrint("forSize = " + str(forSize))
    digitCount = 0
    numberTotal = 0
    crossDivideOperands = []
    crossDivideOperator = []
    for r in range(0, forSize):
        i = forSize-r - 1
        bugPrint(str(i) + "," + str(formulaStr[i]))
        #如果碰到加號，把總值(total)加上運算元值(numberTotal)，並且重新計算運算元值和長度
        if formulaStr[i] == '+':
            #利用cleanCrossDevideList()把CrossDevideList 儲存的算式算出來
            res = cleanCrossDevideList(numberTotal, crossDivideOperands, crossDivideOperator)
            total = total + res
            #重新計算運算元值和長度
            numberTotal = 0
            digitCount = 0
        elif formulaStr[i] == '-':
            res = cleanCrossDevideList(numberTotal, crossDivideOperands, crossDivideOperator)
            total = total - res
            numberTotal = 0
            digitCount = 0
        ##如果碰到"乘號/除號"，把全域變數(CROSS/DIVIDE) append 到crossDivideOperator，
        #並且把numberTotal append 到crossDivideOperands.
        elif formulaStr[i] == '*':
            #把全域變數(CROSS/DIVIDE) append 到crossDivideOperator
            crossDivideOperator.append(CROSS)
            #並且把numberTotal append 到crossDivideOperands
            crossDivideOperands.append(numberTotal)
            #重新計算運算元值和長度
            numberTotal = 0
            digitCount = 0
        elif formulaStr[i] == '/':
            crossDivideOperator.append(DIVIDE)
            crossDivideOperands.append(numberTotal)
            numberTotal = 0
            digitCount = 0
        else:
            numberTotal = numberTotal + int(formulaStr[i]) * pow(10, digitCount)
            digitCount = digitCount + 1 #運算元長度加一
    res = cleanCrossDevideList(numberTotal, crossDivideOperands, crossDivideOperator)
    total = total + res
    print(str(total))
    return str(total)