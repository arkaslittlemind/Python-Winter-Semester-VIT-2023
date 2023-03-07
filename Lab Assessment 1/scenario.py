v1 = 50 #speed of train 1 in km/h
v2 = 70 #speed of train 2 in km/h
vb = 80 #speed of bee in km/h
d = 100 #distance between train
# time taken for trains to collide in hours
t = d / (v1 + v2)
# total distance travelled by bee
db = vb * t
print("Total distance travelled by the bee in time till the collision:", db, "km")
# conversion in minutes
time_in_minutes = t * 60
print("Time taken for the trains to collide in minutes :", time_in_minutes, "minutes")