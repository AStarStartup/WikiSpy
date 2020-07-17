from Stringf import *
from CRMission import * 

class TestCR(CRMission):

  def __init__(self, Crabs):
    CRNode.__init__(self, Crabs, 'MissionTestCRAbs')
    print ("> CRAbs Test")
    #self.Do("Intake > ?")
    #wikipedia.search("Foo")
    print ("< ? Done testing CRAbs. <")
  