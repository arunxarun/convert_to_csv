'''
Created on Mar 27, 2016

@author: arunjacob
'''

import sys
from tcx_to_csv import TcxToCsv
from gpx_to_csv import GpxToCsv

if __name__ == '__main__':
    
    if len(sys.argv) < 4:
        print("convert_csv [tcx | gpx] [input file] [output csv_file]")
        exit(1)
        
        
    format = sys.argv[1]
    inputFile = sys.argv[2]
    csvFile = sys.argv[3]
    
    if format == "csv":
        converter = TcxToCsv(inputFile)
        
    else: 
        converter = GpxToCsv(inputFile)
        
    
    converter.convert(csvFile)
    
    