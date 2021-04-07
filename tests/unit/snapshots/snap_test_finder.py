# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_get_views_in_file 1"] = set(
    ["codoc_domain_model.view_all", "codoc_domain_model.domain_classes"]
)
