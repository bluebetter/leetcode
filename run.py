#!/usr/bin/env python -B
# coding=utf-8
import sys

code = sys.argv[1]

prefix = "s_"
m = __import__("solutions." + prefix + code)
solution = eval("m." + prefix + code + ".Solution")

prefix = "tc_"
m = __import__("testcase." + prefix + code)
tcs = eval("m." + prefix + code + ".TCS")

s = solution()
f = eval("s." + tcs['func'])
for tc in tcs['tcs']:
    assert(tc['hope'] == f(tc['input']))

