from geopy import geocoders # pip install geopy

g = geocoders.GoogleV3()
c = "Bangladesh"
place, (lat, lng) = g.geocode(c)

timezone = g.timezone(g.geocode(c).point)
timezone = timezone.zone

t = type(timezone)

print timezone, t

# print place, lat, lng
# -> (u'Singapore', (1.352083, 103.819836))

