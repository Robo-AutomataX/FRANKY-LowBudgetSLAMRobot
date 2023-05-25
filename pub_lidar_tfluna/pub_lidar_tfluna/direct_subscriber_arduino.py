import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class KeyboardSerial(Node):

    def __init__(self):
        super().__init__('keyboard_serial')
        self.subscription = self.create_subscription(
            String,
            'teclas_presionadas',
            self.callback,
            10
        )
        self.serial_port = serial.Serial('/dev/ttyACM0', 115200)  # Ajusta el puerto serie y la velocidad según tu configuración

    def callback(self, msg):
        key = msg.data
        self.get_logger().info('Tecla presionada: %s' % key)
        self.send_to_arduino(key)

    def send_to_arduino(self, data):
        try:
            self.serial_port.write(data.encode('utf-8'))
        except serial.SerialException:
            self.get_logger().error('Error al enviar datos al Arduino.')

def main(args=None):
    rclpy.init(args=args)
    keyboard_serial = KeyboardSerial()
    rclpy.spin(keyboard_serial)
    keyboard_serial.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

