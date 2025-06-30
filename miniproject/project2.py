import statistics as stat
#height in cm
user_input = input("Enter height separated by commas: ")
height= [float(x.strip()) for x in user_input.split(",")] 
# Calculations
print("List:", height)
print("count:", len(height))
print("mean:", stat.mean(height))
print("median:", stat.median(height))
print("mode:", stat.mode(height))
print("standard deviation:", stat.stdev(height))
print("variance:", stat.variance(height))
print("minimum:", min(height))
print("maximum:", max(height))
print("range:", max(height) - min(height))
##convert height into meter and inches
height_meters = [h / 100 for h in height]
height_inches = [h * 0.393701 for h in height]
print("Height in meters:", height_meters)
print("Height in inches:", height_inches)
#classifying each person into short, average, tall
for h in height:
    if h < 150:
        print(f"{h} cm: Short")
    elif 150 <= h < 170:
        print(f"{h} cm: Average")
    else:
        print(f"{h} cm: Tall")
        