parcel = 0
total_weight = 0
while True:
    parcel_weight = int(input("Enter the parcel weight, or 0 to finish: "))
    if parcel_weight == 0:
        break
    
    parcel += 1
    total_weight += parcel_weight

print(f"Parcels: {parcel}")
print(f"Total weight: {total_weight}")




    
