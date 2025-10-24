import random
from utils.table import Table, Seat

class OpenSpace:
    def __init__(self, number_of_tables, capacity_of_tables):
        """Creating two attributes, where one is an integer and the other one is a list"""
        self.number_of_tables = number_of_tables
        self.tables = [Table(capacity_of_tables) for _ in range(number_of_tables)]

    def organize(self, names):
        """Randomly assigning people from the names list to available seats from all the tables."""
        random.shuffle(names)
        
        for name in names:
            is_assigned = False
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    is_assigned = True
                    break
            if not is_assigned:
                print(f"No more seats left for {name}")

    def display(self):
        """Displaying the tables with the name of the people who are sitting there."""
        for i, table in enumerate(self.tables, start = 1):
            print(f" Table {i}: ")
            for x, seat in enumerate(table.seats, start = 1):
                if seat.free:
                    print(f"Seat {x}: empty")
                else:
                    print(f"Seat {x}: {seat.occupant}")
            print()
             
    def store(self, filename):
        """Storing the repartition of tables and the name of people in an file """
        with open(filename, 'w') as f:
            for i, table in enumerate(self.tables, start = 1):
                f.write(f"Table {i}:\n")
                for x, seat in enumerate(table.seats, start = 1):
                    if seat.free:
                        f.write(f"Seat {x}: empty\n")
                    else:
                        f.write(f"Seat {x}: {seat.occupant}\n")
                f.write("\n")