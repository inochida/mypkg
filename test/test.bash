#!/bin/bash
# SPDX-FileCopyrightText: 2025 Sota Ino
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

timeout 15 ros2 launch mypkg rate.launch.py > /tmp/mypkg.log 2> /tmp/mypkg.err

cat /tmp/mypkg.log | grep -E 'USD:|EUR:|GBP:'
[ $? -ne 0 ] && exit 1

! grep -iq 'error' /tmp/mypkg.err

echo "ALL TESTS PASSED"
exit 0
