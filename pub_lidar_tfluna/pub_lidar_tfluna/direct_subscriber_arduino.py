
#Este programa se suscribe al topic en el cual se publican las teclas
#que son presionadas por el usuario para después mandar esos datos
#al serial del arduino MEGA (para controlar los motores de las llantas) y al
#del arduino UNO (para controlar el motor del LIDAR)



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
        self.serial_port2= serial.Serial('/dev/ttyACM1', 115200)

    def callback(self, msg):
        key = msg.data
        self.get_logger().info('Tecla presionada: %s' % key)
        if key=="g":
            self.send_to_arduino_uno(key)
        else:
            self.send_to_arduino_mega(key)

    def send_to_arduino_mega(self,data):
        try:
            self.serial_port.write(data.encode('utf-8'))
        except serial.SerialException:
            self.get_logger().error('Error al enviar datos al arduino MEGA')

    def send_to_arduino_uno(self, data):
        try:
            self.serial_port2.write(data.encode('utf-8'))
        except serial.SerialException:
            self.get_logger().error('Error al enviar datos al Arduino UNO.')

def main(args=None):
    rclpy.init(args=args)
    keyboard_serial = KeyboardSerial()
    rclpy.spin(keyboard_serial)
    keyboard_serial.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

