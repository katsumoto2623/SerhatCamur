

months=['March', 'April', 'May','June', 'July', 'August','September', 'October', 'November','December', 'January', 'February']
days_of_months=[31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ,31, 28]

spring = months[0:3]
summer = months[3:6]
fall = months[6:9]
winter = months[9:]

spring_days = days_of_months[0:3]
summer_days = days_of_months[3:6]
fall_days = days_of_months[6:9]
winter_days = days_of_months[9:]


print("The total day of the summer season :", summer_days[0]+summer_days[1]+summer_days[2] )