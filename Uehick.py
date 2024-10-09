class vehicle:
    
    def __init__(self, max_speed, mileage, colour):
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour
        
tesla = vehicle(180, 0 , "White")
lambo = vehicle(350, 3 , "Blue")

print("Tesla Max Speed:", tesla.max_speed)
print("Tesla Milrage:", tesla.mileage)
print("Tesla Colour:", tesla.colour)

print()

print("Lambo Max Speed:", lambo.max_speed)
print("TLambo Milrage:", lambo.mileage)
print("Lambo Colour:", lambo.colour)

