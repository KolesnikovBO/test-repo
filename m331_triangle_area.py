def area_triangle (a,b,c):
	p = (a+b+c)/2
	return ((p*(p - a)*(p - b)*(p - c)))**(0.5)



at = area_triangle(3,4,5)
print (at)

