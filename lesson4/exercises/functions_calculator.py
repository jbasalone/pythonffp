# Rewrite your pay computation with time-and-a-half for overtime
# and create a function called computepay which takes two parameters ( hours and rate)

try :
	h = raw_input("Enter Hours: ")
	hrs = float(h)
	r = raw_input('Enter Rate: ')
	rRate = float(r)
	m = raw_input('Overtime Multiplier: ')
	multiplier = float(m)
	OTR = raw_input('Different Rate for Overtime? ')
	if OTR is 'y' or OTR is'yes':
		oRate = raw_input('Overtime Rate: ')
		oRate = float(oRate)
	else:
		oRate = rRate
except:
	print "Error, please enter numeric input"
	quit()

def regulartime(rHours, rRate):
	return rHours * rRate

def overtime(oHours, oRate=rRate, multiplier=1.5):
	final_rate = oRate * multiplier
	return oHours * final_rate

if hrs >= 40:
	rHours = 40
	oHours = hrs - 40
else:
	oHours = 0
	rHours = hrs


overtimepay = overtime(oHours, oRate, multiplier)
regularpay = regulartime(rHours, rRate)

print "Your Hours and Rate: "
print 'Overtime: ', overtimepay
print 'Reguar Pay: ', regularpay
print '-' * 5
print overtimepay + regularpay
