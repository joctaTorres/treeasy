# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_tree_id3 1'] = '{"node": "outlook", "values": {"Sunny": {"node": "humidity", "values": {"High": {"node": "No"}, "Normal": {"node": "Yes"}}}, "Overcast": {"node": "Yes"}, "Rain": {"node": "wind", "values": {"Weak": {"node": "Yes"}, "Strong": {"node": "No"}}}}}'
