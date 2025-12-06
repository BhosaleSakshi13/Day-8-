
# Distance safety function
def safe_distance(d):
	if d < 10:
		return False
	return True


distance = int(input("Enter Distance : "))
print(safe_distance(distance))

