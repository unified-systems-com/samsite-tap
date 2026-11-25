"""The compliance collector's GRIFT document carries core's format "1" header (tap#1284).

Core 0.5.0 refuses format "0" documents by default, so a collector still writing "0" would stop
importing. The header reads the grid's spine and type versions, hence the database.
"""

from __future__ import annotations

import pytest
from tap_plugin.samsite.collectors.compliance_collector.batch import assemble_batch

from tap_grid.grift.upgrade import build_header


@pytest.mark.django_db
def test_the_document_carries_cores_format_1_header() -> None:
    document = assemble_batch(
        source="test",
        manifest_version="1",
        site_base_url="https://example.invalid",
        nodes=[],
        edges=[],
    )

    assert document["metadata"]["grift_version"] == "1"
    assert document["metadata"] == build_header(document)
