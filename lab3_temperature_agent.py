# Lab 3: Smart Temperature Control Agent
# Model-Based Reflex Agent

class TemperatureControlAgent:
    def __init__(self):
        # Remember the current state of each appliance.
        self.fan_running = False
        self.heater_running = False

    def adjust_temperature(self, room_temp):
        print(f"\nRoom temperature: {room_temp}°C")

        # Turn the fan on when the room is hot (above 27°C).
        if room_temp > 27 and not self.fan_running:
            self.fan_running = True
            print("Fan switched ON")
        elif room_temp <= 27 and self.fan_running:
            self.fan_running = False
            print("Fan switched OFF")
        else:
            print("Fan state unchanged")

        # Turn the heater on when the room is cold (below 19°C).
        if room_temp < 19 and not self.heater_running:
            self.heater_running = True
            print("Heater switched ON")
        elif room_temp >= 19 and self.heater_running:
            self.heater_running = False
            print("Heater switched OFF")
        else:
            print("Heater state unchanged")


# Different temperatures used to test the agent.
test_temperatures = [15, 22, 31, 31, 18, 24]

smart_agent = TemperatureControlAgent()

for temperature in test_temperatures:
    smart_agent.adjust_temperature(temperature)
