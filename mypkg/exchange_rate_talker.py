import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import requests

class CurrencyTalker(Node):
    def __init__(self):
        super().__init__('currency_talker')
        
        self.currency_map = {
            'USD': 'dollar_rate',
            'EUR': 'euro_rate',
            'GBP': 'pound_rate'
        }
        
        self.pubs = {}
        for code, topic in self.currency_map.items():
            self.pubs[code] = self.create_publisher(Float64, topic, 10)
        
        self.timer = self.create_timer(15.0, self.timer_callback)
        self.timer_callback()
    def timer_callback(self):
        for code, topic in self.currency_map.items():
            try:
                response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{code}')
                rate = float(response.json()['rates']['JPY'])
                
                msg = Float64()
                msg.data = rate
                self.pubs[code].publish(msg)
                
                self.get_logger().info(f'Sent {code} rate')
            except:
                self.get_logger().error(f'Failed {code}')

def main():
    rclpy.init()
    node = CurrencyTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
