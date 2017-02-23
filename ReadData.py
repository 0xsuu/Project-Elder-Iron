#!/usr/bin/env python3

import numpy as np
import pprint

def handleEndpointsBlock(Endpoint):
    latency = {}
    latency['center'] = Endpoint[0][0]
    latency['cacheServerNum'] = Endpoint[0][1]
    if Endpoint[0][1] != 0:
        for miniLat in Endpoint[1:]:
            print(miniLat[0], miniLat[1])
            latency[miniLat[0]] = miniLat[1]

    return latency

def readfile(filePath):
    file = open(filePath, "r")
    
    data = []
    for line in file.readlines():
        line = line.strip('\n')
        miniLine = line.split()
        data.append(miniLine)
    dataFrame = {}
    dataFrame['videos'] = data[0][0]
    dataFrame['endpoints'] = data[0][1]
    dataFrame['requestDescriptions'] = data[0][2]
    dataFrame['cacheNum'] = data[0][3]
    dataFrame['cacheSize'] = data[0][4]
    dataFrame['videoSizes'] = data[1]
    dataFrame['latency'] = []
    start = 2
    for i in range(int(dataFrame['endpoints'])):
        end = start + int(data[start][1])
        dataFrame['latency'].append(handleEndpointsBlock(data[start:end+1]))
        
        start = end + 1
    
    return dataFrame


data = readfile('me_at_the_zoo.in')
pprint.pprint(data)
