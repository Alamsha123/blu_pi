# blu_pi
To run the provided Python code, follow these steps:

Install PyBluez:
Before running the script, make sure you have the PyBluez library installed. You can install it using the following command:
pip install pybluez
Run the Python Script:
Save the provided Python code into a file, Open a terminal and navigate to the directory where the script is saved. Then, run the script using the following command:

python accelerometer.py
This will start the script, and it will wait for a Bluetooth connection from the BLE beacon.

Configure BLE Beacon:
Make sure your BLE beacon is powered on and broadcasting accelerometer data. Ensure that the Bluetooth adapter on your laptop is also enabled.

Establish Bluetooth Connection:
The script will print information about waiting for a connection. Ensure that your BLE beacon is discoverable and initiate the connection from the beacon side. Once the connection is established, the script will start receiving and processing accelerometer data.

Monitor Output:
The script will print information about the received accelerometer data, including frame type, battery level, MAC address, and whether the tag is moving or stationary.

Stop the Script:
To stop the script, press Ctrl+C in the terminal. This will close the Bluetooth connection and terminate the script.
