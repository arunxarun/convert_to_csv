'''
Created on Mar 27, 2016

@author: arunjacob
'''
import unittest
import tcx_to_csv
from tcx_to_csv import TcxToCsv

class Test(unittest.TestCase):


    def testExtractsTrackPointsAcrossLaps(self):
        converter = TcxToCsv("../testData/testTrackPointsAcrossLaps.tcx")
        allData = converter.getCsvOutput()
        
        self.assertEquals(3,len(allData)) # counting header line
        
        
    def testExtractsFullDomMOdel(self):
        converter = TcxToCsv("../testData/round_the_rock_SUP_race_09_12_2015_tcxver.tcx")
        allData = converter.getCsvOutput()
        
        self.assertTrue(len(allData) > 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()