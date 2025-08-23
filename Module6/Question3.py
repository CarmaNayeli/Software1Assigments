#define function to convert gallons to liters
def gallons_to_liters(gallons):
    return (gallons * 3.785)

# ask user for initial number of gallons, exit if negative
gal = float(input("Enter a volume in American gallons (negative value to quit): "))

# until user inputs a negative number, convert each value and ask for another
while gal >= 0:
    print(f"{gal:.1f} American gallons is {gallons_to_liters(gal):.2f} liters.")
    gal = float(input("Enter a volume in American gallons (negative value to quit): "))

# confirm program end
print("Program finished.")