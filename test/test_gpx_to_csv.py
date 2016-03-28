'''
Created on Mar 27, 2016

@author: arunjacob
'''
import unittest
from gpx_to_csv import GpxToCsv

class Test(unittest.TestCase):


    def testExtractsTrackPointsAcrossLaps(self):
        converter = GpxToCsv("../testData/testGpxParsing.gpx")
        allData = converter.getCsvOutput()
        
        self.assertEquals(3,len(allData)) # counting header line
        
        
    def testExtractsFullDomModel(self):
        converter = GpxToCsv("../testData/RAMROD_2015.gpx")
        allData = converter.getCsvOutput()
        
        self.assertTrue(len(allData) > 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()