months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
while True:
	print("\n-----Tell me your birthday-----")
	year = input('Year:')
	month = input('Month(1-12):')
	day = input("Day(1-31):")

	month_0 = months[int(month)-1]
	day_0 = day + endings[int(day)-1]

	print("\n-----This is your birthday-----")
	print(month_0 + " " + day_0 + " " + year)
	quit = input('Quit this program(y/n):')
	if quit == "y":
		break
	

