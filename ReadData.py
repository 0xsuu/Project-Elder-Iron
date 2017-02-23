#!/usr/bin/env python3

import sys
import random
import copy

class Cache:
    def __init__(self, num, capcity):
        self.num = num
        self.capcity = capcity
        self.videos = []
    def cache_video(self, video):
        self.videos.append(video)
        self.capcity -= video.size
class Endpoint:
    def __init__(self, latency):
        self.caches = []
        self.latency = latency
    def connect_to(self, cache, latency):
        self.caches.append((cache, latency))
class Video:
    def __init__(self, num, size):
        self.num = num
        self.size = size
class Request:
    def __init__(self, num_video, endpoint, count):
        self.num_video = num_video
        self.endpoint = endpoint
        self.count = count
class Input:
    def __init__(self, endpoints, videos, requests, videos_sizes, caches):
        self.endpoints = endpoints
        self.videos = videos
        self.requests = requests
        self.videos_sizes = videos_sizes
        self.caches = caches

def readfile(filePath):
    fo = open(filePath, "r")
    (num_video, num_endpoint, num_request, num_caches, cache_capcity) = fo.readline().strip('\n').split(" ")
    videos_sizes = fo.readline().strip('\n').split(" ")
    videos = []
    for i in range(int(num_video)):
        videos.append(Video(int(i), int(videos_sizes[i])))
    endpoints = []
    caches = []
    for c in range(int(num_caches, 10)):
        caches.append(Cache(c, int(cache_capcity)))
    for e in range(int(num_endpoint, 10)):
        (latency, num_caches_connected) = fo.readline().strip('\n').split(" ")
        endpoint = Endpoint(latency)
        for c in range(int(num_caches_connected, 10)):
            (num, latency) = fo.readline().strip('\n').split(" ")
            endpoint.connect_to(caches[int(num)], int(latency))
        endpoints.append(endpoint)
    requests = []
    for r in range(int(num_request, 10)):
        (num_video, endpoint, count) = fo.readline().strip('\n').split(" ")
        requests.append(Request(num_video, endpoint, int(count)))
    
    return Input(endpoints, videos, requests, videos_sizes, caches)

def score(data):
    sum_time = 0
    count_request = 0
    for r in data.requests:
        count_request += r.count
        num_endpoint = r.endpoint
        num_video = r.num_video
        endpoint = data.endpoints[int(num_endpoint)]
        least_latency = []
        for i in range(len(data.videos)):
            least_latency.append(int(endpoint.latency))
        for (cache, latency) in endpoint.caches:
            for video in cache.videos:
                tmp = least_latency[video.num]
                if tmp > latency:
                    least_latency[video.num] = latency
        #       print("num_endpoint", num_endpoint, "least_latency", least_latency)
    sum_time += r.count * (int(endpoint.latency) - least_latency[int(num_video)])
    return sum_time/count_request*1000

def search(d):
    videoCount = len(d.videos)
    cacheCount = len(d.caches)
    cacheMax = d.caches[0].capcity
    videos = d.videos
    
    cacheAlloc = []
    for i in range(cacheCount):
        cacheAlloc.append([])
    #vs = {}
    #for i in range(videoCount):
    #vs[i] = dataFrame['videoSizes']
    for video in range(videoCount):
        cacheAllocCopy = copy.deepcopy(d)
        values = []
        for cacheIndex in range(cacheCount):
            if cacheAllocCopy.caches[cacheIndex].capcity == 0:
#            if (isFullLoaded(cacheMax, cacheAllocCopy.caches[cacheIndex], videos)):
                values.append(0)
                continue
                
            cacheAllocCopy.caches[cacheIndex].cache_video(cacheAllocCopy.videos[video])
#            cacheAllocCopy[cacheIndex].append(video)

            values.append(score(cacheAllocCopy))
        maxC = values.index(max(values))
        cacheAlloc[maxC].append(video)
    print(cacheAlloc)

data = readfile('kittens.in')
#pprint.pprint(data)
search(data)


