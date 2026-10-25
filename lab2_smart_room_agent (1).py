# Author: Qasim Raza
# Lab 2: Intelligent Room Environment Controller
# A simple rule-based agent that remembers its previous state.

class RoomController:
    def __init__(self):
        self.current_mode = None

    def choose_mode(self, temperature, people_count):
        if people_count == 0:
            return "OFF"
        elif temperature >= 28:
            return "COOLING"
        else:
            return "NORMAL"

    def update_room(self, temperature, people_count):
        new_mode = self.choose_mode(temperature, people_count)
        print(f"Temperature: {temperature}°C | People: {people_count}")
        if new_mode == self.current_mode:
            print(f"No change needed. Room is already in {new_mode} mode.\n")
        else:
            print(f"Command: Switch room to {new_mode} mode.\n")
            self.current_mode = new_mode


if __name__ == "__main__":
    room = RoomController()
    print("Test 1: Hot room with people")
    room.update_room(32, 3)
    print("Test 2: Same condition again")
    room.update_room(31, 2)
    print("Test 3: Comfortable room")
    room.update_room(24, 2)
    print("Test 4: Empty room")
    room.update_room(30, 0)
    print("Test 5: People return")
    room.update_room(26, 1)
