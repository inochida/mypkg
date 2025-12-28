# SPDX-FileCopyrightText: 2025 Sota Ino
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='talker',
            name='talker_node',
            parameters=[{'currencies': ['USD', 'EUR', 'GBP']}],
            output='screen',
        ),
        Node(
            package='mypkg',
            executable='listener',
            name='listener_node',
            output='screen',
        ),
    ])
