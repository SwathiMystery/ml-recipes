from sklearn.datasets import load_iris
iris = load_iris()
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]
for x in xrange(len(iris.target)):
	print "Example %d : label %s, features %s" % (x, iris.target[x], iris.data[x] )