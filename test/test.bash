#!/bin/bash
# SPDX-FileCopyrightText: 2025 Sota Ino
# SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build

timeout 30 stdbuf -oL bash -lc \
"source /opt/ros/humble/setup.bash && source install/setup.bash && ros2 launch mypkg rate.launch.py" \
> /tmp/mypkg.log 2> /tmp/mypkg.err

sleep 2

if ! grep -Ei 'USD|EUR|GBP' /tmp/mypkg.log; then
    echo "--- Standard Output (/tmp/mypkg.log) ---"
    cat /tmp/mypkg.log
    echo "--- Standard Error (/tmp/mypkg.err) ---"
    cat /tmp/mypkg.err
    exit 1
fi

! grep -iq 'error' /tmp/mypkg.err

echo "ALL TESTS PASSED"
exit 0

