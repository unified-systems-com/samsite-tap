"""GRIFT batch assembly for the samsite compliance collector.

Wraps the per-run node/edge envelopes in the one GRIFT document the collector
submits via ``CollectorBase.submit_grift``. Mirrors the boto3 collector's
batch shape (one batch per run, per-run uuid7 batch id, deterministic node/
edge ids inside), under the GRIFT format "1" header core writes for it
(``tap_grid.grift.upgrade.build_header``).
"""

from __future__ import annotations

import uuid
from collections import Counter
from datetime import UTC, datetime
from typing import Any

COLLECTION_FORMAT = "tap.samsite.compliance-v0"


def assemble_batch(
    *,
    source: str,
    manifest_version: str,
    site_base_url: str,
    nodes: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    now: datetime | None = None,
) -> dict[str, Any]:
    """Wrap node/edge envelopes in one GRIFT document for one run.

    The header is core's format "1" header: the spine version and the version of every type the
    batch carries, read off the grid, so this needs the database; the collector calls it in a run.
    """
    from tap_grid.grift.upgrade import build_header

    moment = (now or datetime.now(UTC)).astimezone(UTC)
    now_iso = moment.isoformat().replace("+00:00", "Z")
    label = f"Samsite compliance collection {now_iso}"

    by_entity_type = Counter(env["entity"]["entity_type"] for env in nodes)
    description_data = {
        "schema_version": "v0",
        "manifest_version": manifest_version,
        "site_base_url": site_base_url,
        "counts": {
            "nodes": len(nodes),
            "edges": len(edges),
            "by_entity_type": dict(sorted(by_entity_type.items())),
        },
    }

    batch = {
        "batch_entity": {
            "entity_id": str(uuid.uuid4()),
            "entity_type": "batch",
            "name": label,
            "dimensions": {},
        },
        "batch_node": {
            "source": source,
            "name": label,
            "description": "Samsite signed /.well-known/ compliance artifacts.",
            "description_json": {
                "format": COLLECTION_FORMAT,
                "data": description_data,
            },
        },
        "nodes": nodes,
        "edges": edges,
    }
    document: dict[str, Any] = {"metadata": {}, "_reserved": {}, "batches": [batch]}
    document["metadata"] = build_header(document)
    return document
