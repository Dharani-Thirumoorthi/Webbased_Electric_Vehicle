
import serial

# Set up the serial port (replace with the correct port for your setup)
ser = serial.Serial('COM3', 115200)  # Example for Windows (COM3), for Linux it might be '/dev/ttyUSB0'

# Wait for the serial data to be available
ser.flush()

# Read the incoming data
data = []

while True:
    line = ser.readline().decode('utf-8').strip()  # Read the line, decode to string, and remove extra spaces
    print(line)  # Print the line for debugging
    
    # Process data and extract relevant information
    if "Voltage" in line:  # Check if the line contains relevant information
        data.append(line)  # Store the data in a list

    if len(data) >= 10:  # If we have enough data, stop
        break

ser.close()  # Close the serial connection when done

import pandas as pd

# Example data (from serial monitor, you will parse this)
data = [
    "Voltage: 220.0 V, Current (Average): 5.0 Amps RMS, Power: 1100.0 Watts, Energy: 0.5 Wh, Cost: Rs 2.4, Total Time Used: 1.2 hours",
    "Voltage: 221.5 V, Current (Average): 5.1 Amps RMS, Power: 1120.0 Watts, Energy: 0.52 Wh, Cost: Rs 2.5, Total Time Used: 1.3 hours",
    # More data entries
]

# Parse the data into structured format
parsed_data = []
for line in data:
    # Example of splitting each line into the desired parameters
    voltage = float(line.split("Voltage: ")[1].split(" V")[0])
    current = float(line.split("Current (Average): ")[1].split(" Amps")[0])
    power = float(line.split("Power: ")[1].split(" Watts")[0])
    energy = float(line.split("Energy: ")[1].split(" Wh")[0])
    cost = float(line.split("Cost: Rs ")[1].split(",")[0])
    total_time = float(line.split("Total Time Used: ")[1].split(" hours")[0])
    
    parsed_data.append({
        'Voltage (V)': voltage,
        'Current (A)': current,
        'Power (W)': power,
        'Energy (Wh)': energy,
        'Cost (Rs)': cost,
        'Total Time Used (hrs)': total_time
    })

# Create a DataFrame
df = pd.DataFrame(parsed_data)

# Print the DataFrame
print(df)

# Save the data to an Excel file
df.to_excel('energy_data.xlsx', index=False)

print("Data has been saved to energy_data.xlsx")

import serial
import pandas as pd

# Set up the serial port (replace with the correct port for your setup)
ser = serial.Serial('COM3', 115200)  # Replace 'COM3' with the actual port

# Wait for the serial data to be available
ser.flush()

# Example to store the data
data = []

# Read incoming data for a few seconds
for _ in range(10):  # Change the range for more data
    line = ser.readline().decode('utf-8').strip()
    print(line)  # Print the line for debugging
    
    # Process data and extract relevant information
    if "Voltage" in line:
        voltage = float(line.split("Voltage: ")[1].split(" V")[0])
        current = float(line.split("Current (Average): ")[1].split(" Amps")[0])
        power = float(line.split("Power: ")[1].split(" Watts")[0])
        energy = float(line.split("Energy: ")[1].split(" Wh")[0])
        cost = float(line.split("Cost: Rs ")[1].split(",")[0])
        total_time = float(line.split("Total Time Used: ")[1].split(" hours")[0])

        data.append({
            'Voltage (V)': voltage,
            'Current (A)': current,
            'Power (W)': power,
            'Energy (Wh)': energy,
            'Cost (Rs)': cost,
            'Total Time Used (hrs)': total_time
        })

ser.close()  # Close the serial connection when done

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save the data to an Excel file
df.to_excel('energy_data.xlsx', index=False)

print("Data has been saved to energy_data.xlsx")
