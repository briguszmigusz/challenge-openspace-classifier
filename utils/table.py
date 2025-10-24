class Seat:
    """Cretaing two attributes, where free is a boolean value and occupant is a string."""
    def __init__(self) -> None:
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        """Assigns an occupant to the seat if it's free, otherwise indicates it's taken."""
        if self.free:
            self.occupant = name
            self.free = False
            return f"{self.occupant} is sitting here."
        else:
            return "This seat is taken."

    def remove_occupant(self):
        """Frees the seat and returns the name of the previous occupant if occupied."""
        if not self.free:
            name = self.occupant
            self.free = True
            self.occupant = ""
            return f"Previously {name} was sitting here."
        else:
            return None


class Table:
    def __init__(self,capacity):
        """Creating two attributes, where capacity is an integer and seats is a list of Seat objects representing the seats."""
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        """Checking if there are any seats free, returning a boolean value."""
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self,name):
        """Assigning a person to a seat if it is free."""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return (f"{name} was assigned a table", True)
        return ("No seats left", False)

    def left_capacity(self):
        """Showing how much free seats we have left."""
        capacity = 0
        for seat in self.seats:
            if seat.free:
                capacity += 1
        return capacity
