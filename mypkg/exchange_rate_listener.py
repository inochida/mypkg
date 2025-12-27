import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class CurrencyListener(Node):
    def __init__(self):
        super().__init__('listener')
        
        self.create_subscription(Float64, 'dollar_rate', lambda msg: self.cb(msg, 'USD'), 10)
        self.create_subscription(Float64, 'euro_rate',   lambda msg: self.cb(msg, 'EUR'), 10)
        self.create_subscription(Float64, 'pound_rate',  lambda msg: self.cb(msg, 'GBP'), 10)

    def cb(self, msg, name):
        self.get_logger().info(f'{name}: {msg.data} JPY')

def main():
    rclpy.init()
    rclpy.spin(CurrencyListener())
    rclpy.shutdown()
