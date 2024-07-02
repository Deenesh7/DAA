def pClosest(points, K):

	points.sort(key = lambda K: K[0]**2 + K[1]**2)
	return points[:K]
points = [[1,3],[-2,2],[5,8],[0,1]]
K = 2
print(pClosest(points, K))
