from scipy.cluster.vq import kmeans,vq,whiten

#data generation
from numpy import vstack,array
from numpy.random import rand

#data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))

#normalize data (whitening of data)
data = whiten(data)

#computing k-means with k = 3 (2 clusters)
centroids,_ = kmeans(data,3)
print(centroids)

#assign each sample to a cluster
clx,_ = vq(data,centroids)
#check clusters of observation
print(clx)
