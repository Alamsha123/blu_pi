import struct
import bluetooth

def parse_accelerometer_packet(packet):
    data = struct.unpack("<BBHHBBHHH6s", packet)
    frame_type = data[0]
    version_number = data[1]
    battery_level = data[2] / 100  # converting to percentage
    x_axis = data[3] / 256.0  # converting from fixed-point to float
    y_axis = data[4] / 256.0
    z_axis = data[5] / 256.0
    mac_address = ':'.join(f'{byte:02X}' for byte in data[6])
    
    return frame_type, version_number, battery_level, x_axis, y_axis, z_axis, mac_address

def detect_movement(x_axis, y_axis, z_axis, threshold=0.1):
    acceleration = (x_axis**2 + y_axis**2 + z_axis**2)**0.5
    return acceleration > threshold

def main():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    bluetooth.advertise_service(server_sock, "BluetoothServer", service_id=bluetooth.SERIAL_PORT_CLASS, profiles=[bluetooth.SERIAL_PORT_PROFILE])

    print(f"Waiting for connection on RFCOMM channel {port}")

    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    try:
        while True:
            packet = client_sock.recv(40)  # Assuming the maximum packet size is 40 bytes
            if packet:
                frame_type, version_number, battery_level, x_axis, y_axis, z_axis, mac_address = parse_accelerometer_packet(packet)
                is_moving = detect_movement(x_axis, y_axis, z_axis)
                
                print(f"Frame Type: {frame_type}, Battery Level: {battery_level}%, MAC Address: {mac_address}")
                print(f"Acceleration: X={x_axis:.2f}g, Y={y_axis:.2f}g, Z={z_axis:.2f}g")
                print(f"Tag is {'moving' if is_moving else 'stationary'}")

    except KeyboardInterrupt:
        pass

    print("Closing connection...")
    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    main()
