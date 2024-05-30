from dataclasses import dataclass, field

@dataclass
class Flight:
    flight_number: str
    departure: str
    destination: str
    total_seats: int
    booked_seats: int = field(default=0)

    def check_availability(self):
        return self.total_seats - self.booked_seats

    def book_seat(self, num_seats):
        if num_seats > 0 and num_seats <= self.check_availability():
            self.booked_seats += num_seats
            print(f"{num_seats} seat(s) booked successfully.")
        else:
            print("Not enough available seats.")

    def display_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Departure: {self.departure}")
        print(f"Destination: {self.destination}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Booked Seats: {self.booked_seats}")
        print(f"Available Seats: {self.check_availability()}")

# Create flight instances
flight1 = Flight("F101", "New York", "Los Angeles", total_seats=150)
flight2 = Flight("F102", "Chicago", "Dallas", total_seats=100)

# Display flight options
print("Flight Options:")
print("1. Flight 1 (F101)")
print("2. Flight 2 (F102)")

choice = input("Select a flight to book seats (1 or 2): ")

if choice == '1':
    flight = flight1
elif choice == '2':
    flight = flight2
else:
    print("Invalid choice. Exiting...")
    exit()

# Display selected flight information
print("\nSelected Flight Information:")
flight.display_info()

# Book seats
num_seats = int(input("\nEnter the number of seats to book: "))
flight.book_seat(num_seats)

# Display updated flight information
print("\nUpdated Flight Information:")
flight.display_info()
