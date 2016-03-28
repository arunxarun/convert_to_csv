'''
Created on Mar 27, 2016

@author: arunjacob
'''
import xml.dom.minidom
import os

class TcxToCsv(object):
    '''
    classdocs
    '''


    def __init__(self, tcxFileName):
        '''
        Constructor
        '''
        self.tcxFileName = tcxFileName
        
    
    def convert(self,csvFileName):
        foo = os.getcwd()

        allOutput = self.getCsvOutput()
        
        with open(csvFileName, 'w') as f:
            for output in allOutput:
                f.write(output)
                
        
    def getCsvOutput(self):
        
        allOutput = []
        DOMTree = xml.dom.minidom.parse(self.tcxFileName)
        collection = DOMTree.documentElement
        trackPoints = collection.getElementsByTagName("Trackpoint")
        
        allOutput.append("Time,Latitude,Longitude,HeartRate,Altitude(Meters)\n")
        for trackPoint in trackPoints:
            outputStr = ""
            
            timeEl = trackPoint.getElementsByTagName("Time")
            if timeEl != None:
                timeData = timeEl.item(0).childNodes[0].data;
                outputStr += timeData
            else:
                outputStr += "notime"
            
            latEl = trackPoint.getElementsByTagName("LatitudeDegrees")
            
            if latEl != None:
                lat = latEl.item(0).childNodes[0].data
                outputStr += ","+lat
            else:
                outputStr += ",nolat"
            
            longEl = trackPoint.getElementsByTagName("LongitudeDegrees")
            
            if longEl != None:
                long = longEl.item(0).childNodes[0].data
                outputStr += ","+long
            else:
                outputStr += ",nolong"
                
            hrEl = trackPoint.getElementsByTagName("HeartRateBpm")
            
            if hrEl != None:
                valueEl = hrEl.item(0).getElementsByTagName("Value")
                if valueEl != None:
                    value = valueEl.item(0).childNodes[0].data
                    outputStr += ","+value
            else:
                outputStr += ",noHr"
                
            altEl = trackPoint.getElementsByTagName("AltitudeMeters")
            
            if altEl != None:
                altMeters = altEl.item(0).childNodes[0].data
                outputStr += ","+altMeters
            else:
                outputStr += ",noAlt"
            
            
            outputStr += "\n"
            allOutput.append(outputStr)
            
        return allOutput

            
            
            
        
        
            
            
                
                
                
            

            
            
        
        