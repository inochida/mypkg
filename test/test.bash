#!/bin/bash
# SPDX-FileCopyrightText: 2025 Sota Ino
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

timeout 30 ros2 launch mypkg rate.launch.py > /tmp/mypkg.log 2> /tmp/mypkg.err

cat /tmp/mypkg.log | grep -Ei 'USD|EUR|GBP'
if [ $? -ne 0 ]; then
    echo "Current Log Content:"
    cat /tmp/mypkg.log
    exit 1
fi

! grep -iq 'error' /tmp/mypkg.err

echo "ALL TESTS PASSED"
exit 0
