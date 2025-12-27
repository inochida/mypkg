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
        text = f'{name}: {msg.data} JPY'
        print(text)
        self.get_logger().info(text)

def main():
    rclpy.init()
    node = CurrencyListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
