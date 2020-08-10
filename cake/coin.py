def how_many_ways(coins, value):
	'''
	https://www.interviewcake.com/question/python/coin

	a value = v, and n = largest value coin 
	v = {[(v-1, 1)], [(v - 2, 2)], ..., [(v - n, n)]}
	
	'''
	many_ways = {} 			# dictionary which contains the list of all unique combination
	for x in xrange(0, value): # O(v)
		prev_val = x
		curr_val = x + 1
		many_ways[curr_val] = []
		if curr_val in coins:
			many_ways[curr_val].append([curr_val])

		#print("prev_val %d # curr_val %d" % (prev_val, curr_val))
		#print("many_ways :: %s" % many_ways)
		#print("---------------")
		while prev_val in many_ways : # O(v-1)
			diff = curr_val - prev_val
			#print("diff :: %d" % diff)
			#print("---------------")
			if diff in coins:
				prev_ways = many_ways[prev_val]
				#print("prev_ways :: %s" % prev_ways)
				#print("---------------")
				for prev in prev_ways:
					prev = list(prev)
					prev.append(diff)
					prev = sorted(prev)
					#print("prev :: %s" % prev)
					#print("---------------")
					if prev not in many_ways[curr_val]:
						many_ways[curr_val].append(prev)
					#print("added many_ways :: %s" % many_ways)
					#print("=============")


			prev_val -= 1

	return many_ways
		
if __name__ == '__main__':

	many_ways = how_many_ways([1,2,3], 9)
	for x in many_ways:
		print(many_ways[x])

	print(len(many_ways[9]))