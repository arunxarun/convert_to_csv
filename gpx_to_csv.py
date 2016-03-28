'''
Created on Mar 27, 2016

@author: arunjacob
'''

import xml.dom.minidom
import os

class GpxToCsv(object):
    '''
    classdocs
    '''


    def __init__(self, gpxFileName):
        '''
        Constructor
        '''
        self.gpxFileName = gpxFileName
        
        
    def convert(self,csvFileName):
        
        allOutput = self.getCsvOutput()
        
        with open(csvFileName, 'w') as f:
            for output in allOutput:
                f.write(output)


    def getCsvOutput(self):
        
        allOutput = []
        DOMTree = xml.dom.minidom.parse(self.gpxFileName)
        collection = DOMTree.documentElement
        trackPoints = collection.getElementsByTagName("trkpt")
        
        allOutput.append("Time,Latitude,Longitude,HeartRate,Altitude(Meters),Temp(C)\n")
        
        for trackPoint in trackPoints:
            outputStr = ""
            
            timeEl = trackPoint.getElementsByTagName("time")
            if timeEl != None:
                timeData = timeEl.item(0).childNodes[0].data;
                outputStr += timeData
            else:
                outputStr += "notime"
            
            latVal = trackPoint.getAttribute("lat")
            
            if latVal != None:
                outputStr += ","+latVal
            else:
                outputStr += ",nolat"
            
            
            longVal  = trackPoint.getAttribute("lon")
            
            if longVal != None:
                outputStr += ","+longVal
            else:
                outputStr += ",nolong"
                
            
            '''
            <extensions>
             <gpxtpx:TrackPointExtension>
              <gpxtpx:atemp>17</gpxtpx:atemp>
              <gpxtpx:hr>60</gpxtpx:hr>
             </gpxtpx:TrackPointExtension>
            </extensions>
            '''    
            hrEl = trackPoint.getElementsByTagName("gpxtpx:hr")
            
            if hrEl != None:
                value = hrEl.item(0).childNodes[0].data
                outputStr += ","+value
            else:
                outputStr += ",noHr"
                
            altEl = trackPoint.getElementsByTagName("ele")
            
            if altEl != None:
                altMeters = altEl.item(0).childNodes[0].data
                outputStr += ","+altMeters
            else:
                outputStr += ",noAlt"
            
            
            tempEl = trackPoint.getElementsByTagName("gpxtpx:atemp")
            
            if tempEl != None:
                temp = tempEl.item(0).childNodes[0].data
                outputStr += ","+temp
            outputStr += "\n"
            allOutput.append(outputStr)
            
        return allOutput
