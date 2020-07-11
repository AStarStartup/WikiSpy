import unittest
from Stringf import *
from CRRoom import * 

class TestChineseRoomAbstractStackMachine(unittest.TestCase):

  def test_CR(self):
    CRAbs.Test(self)
    print ("> Crabs Test")
    #self.Do("Intake > ?")
    #wikipedia.search("Foo")
    print ("< ? Done testing Crabs. <")
  