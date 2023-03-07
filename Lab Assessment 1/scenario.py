# distance between trains when bee starts flying
distance = 100

# speed of first train in km/h
speed_train1 = 50

# speed of second train in km/h
speed_train2 = 70

# speed of bee in km/h
speed_bee = 80

# distance travelled by bee in km
distance_bee = 0

# time taken by trains to collide in hours
time_collision = distance / (speed_train1 + speed_train2)

# distance travelled by bee until trains collide
distance_bee = time_collision * speed_bee * 2

# time taken by trains to collide in minutes
time_collision = time_collision * 60

# print results
print("Distance travelled by bee:", distance_bee, "km")
print("Time taken by trains to collide:", time_collision, "minutes")
