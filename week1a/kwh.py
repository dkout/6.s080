kwh_used=1000
kw=kwh_used
p=0
p+=min(500,kw)*0.43
if kw>500:
	p+=min(1000, kw-500)*0.71
if kw>1500:
	p+=min(1000,kw-1500)*1.15
if kw>2500:
	p+=(kw-2500)*1.81
print (p*1.2)
