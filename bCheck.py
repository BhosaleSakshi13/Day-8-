# Battery check function
def check_battery(battery):
	if battery < 20:
		return "Low"
	return "ok"


print(check_battery(15))
print(check_battery(30))
