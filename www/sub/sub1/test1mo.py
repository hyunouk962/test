import sys
import inspect
def modtest():
    print(1)
    print(inspect.getfile(inspect.currentframe()))