from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 日経平均を監視するノード
        Node(
            package='my_package',
            executable='market_publisher',
            name='nikkei_pub',
            parameters=[{'symbol': '^N225', 'interval': 60.0}]
        ),
        # ドル円を監視するノード（同じ実行ファイルで別の名前・パラメータで起動）
        Node(
            package='my_package',
            executable='market_publisher',
            name='usd_jpy_pub',
            parameters=[{'symbol': 'USDJPY=X', 'interval': 60.0}]
        ),
        # アラートノード
        Node(
            package='my_package',
            executable='market_alert',
            name='alert_system',
            parameters=[{'threshold': 0.5}] # 0.5%動いたら警告
        )
    ])
