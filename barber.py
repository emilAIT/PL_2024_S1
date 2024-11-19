from datetime import datetime

class Master:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.earnings = 0
        self.schedule = []  # List of reserved times

    def add_reservation(self, date_time, client_name):
        self.schedule.append({"datetime": date_time, "client": client_name})
        print(f"Reservation for {client_name} added to Master {self.name} at {date_time}.")

    def remove_reservation(self, date_time, client_name):
        self.schedule = [res for res in self.schedule if not (res["datetime"] == date_time and res["client"] == client_name)]
        print(f"Reservation for {client_name} at {date_time} removed from Master {self.name}.")

    def get_history(self):
        print(f"Getting history for Master {self.name}.")
        return self.schedule

    def add_earnings(self, amount):
        self.earnings += amount
        print(f"Added earnings of {amount} to Master {self.name}. Total earnings: {self.earnings}.")

    def get_earnings(self):
        print(f"Getting earnings for Master {self.name}. Total earnings: {self.earnings}.")
        return self.earnings


class Barbershop:
    def __init__(self):
        self.masters = {}  # Dictionary of Master objects by name
        print("Barbershop initialized.")

    def add_master(self, name, rate, start_time, end_time):
        if name in self.masters:
            print(f"Master {name} already exists.")
            return
        self.masters[name] = Master(name, rate)
        print(f"Master {name} added with rate {rate} and working hours from {start_time} to {end_time}.")

    def remove_master(self, name):
        if name in self.masters:
            del self.masters[name]
            print(f"Master {name} removed.")
        else:
            print(f"Master {name} not found.")

    def get_available_spots(self, name, date):
        if name not in self.masters:
            print(f"Master {name} not found.")
            return []
        # Assuming a fixed working day schedule for simplicity
        working_hours = range(9, 18)  # 9:00 to 17:00
        reserved_hours = [res["datetime"].hour for res in self.masters[name].schedule if res["datetime"].date() == date]
        available_hours = [hour for hour in working_hours if hour not in reserved_hours]
        print(f"Available spots for Master {name} on {date}: {available_hours}")
        return available_hours

    def reserve(self, name, date_time, client_name):
        if name not in self.masters:
            print(f"Master {name} not found.")
            return
        if any(res["datetime"] == date_time for res in self.masters[name].schedule):
            print(f"Slot already reserved for Master {name} at {date_time}.")
            return
        self.masters[name].add_reservation(date_time, client_name)
        self.masters[name].add_earnings(self.masters[name].rate)
        print(f"Reservation added for {client_name} with Master {name} at {date_time}.")

    def cancel_reservation(self, client_name, date_time):
        for master in self.masters.values():
            for res in master.schedule:
                if res["client"] == client_name and res["datetime"] == date_time:
                    master.remove_reservation(date_time, client_name)
                    print(f"Reservation for {client_name} at {date_time} canceled.")
                    return
        print("Reservation not found.")

    def get_history(self, name):
        if name in self.masters:
            history = self.masters[name].get_history()
            print(f"History for Master {name}: {history}")
            return history
        else:
            print(f"Master {name} not found.")
            return []

    def get_earnings(self, name):
        if name in self.masters:
            earnings = self.masters[name].get_earnings()
            print(f"Earnings for Master {name}: {earnings}")
            return earnings
        else:
            print(f"Master {name} not found.")
            return 0

    def get_kassa(self):
        total_earnings = sum(master.get_earnings() for master in self.masters.values())
        print(f"Total earnings in kassa: {total_earnings}")
        return total_earnings

    def print_all_masters(self):
        print("Listing all masters in the barbershop:")
        for name, master in self.masters.items():
            print(f"Master: {name}, Rate: {master.rate}, Earnings: {master.earnings}")


# Driver/Main Example
if __name__ == "__main__":
    barber = Barbershop()
    # Add Master
    barber.add_master("Azam", 500, "9:00", "17:00")
    barber.add_master("Ayaz", 600, "9:00", "17:00")
    barber.add_master("Azat", 700, "9:00", "17:00")
    
    # Remove Master
    barber.remove_master("Ayaz")
    barber.remove_master("nonexistent_master")
    
    # Get Available Spots
    available_spots = barber.get_available_spots("Azam", datetime(2024, 11, 11).date())
    print(f"Available spots for Azam on 11-11-2024: {available_spots}")
    
    # Reserve a slot
    barber.reserve("Azam", datetime(2024, 11, 11, 16, 0), "Emi")
    barber.reserve("Azam", datetime(2024, 11, 11, 15, 0), "Azat")
    barber.reserve("Azam", datetime(2024, 11, 11, 16, 0), "Duplicate")
    
    # Get History
    history = barber.get_history("Azam")
    print(f"History for Azam: {history}")
    
    # Get Kassa
    kassa = barber.get_kassa()
    print(f"Total earnings in kassa: {kassa}")
    
    # Get Earnings for Master
    earnings = barber.get_earnings("Azam")
    print(f"Earnings for Azam: {earnings}")
    
    # Cancel Reservation
    barber.cancel_reservation("Emi", datetime(2024, 11, 11, 16, 0))
    barber.cancel_reservation("nonexistent_client", datetime(2024, 11, 11, 16, 0))
    
    # Print All Masters
    barber.print_all_masters()
    
    # Additional Reservations and History
    barber.reserve("Azat", datetime(2024, 11, 12, 14, 0), "Client1")
    barber.reserve("Azat", datetime(2024, 11, 12, 15, 0), "Client2")
    barber.reserve("Azam", datetime(2024, 11, 12, 13, 0), "Client3")
    barber.reserve("Azam", datetime(2024, 11, 12, 14, 0), "Client4")
    
    history = barber.get_history("Azat")
    print(f"History for Azat: {history}")
    
    # Get Updated Kassa
    kassa = barber.get_kassa()
    print(f"Updated total earnings in kassa: {kassa}")
    
    # Get Earnings for All Masters
    earnings_azam = barber.get_earnings("Azam")
    print(f"Earnings for Azam: {earnings_azam}")
    
    earnings_azat = barber.get_earnings("Azat")
    print(f"Earnings for Azat: {earnings_azat}")
