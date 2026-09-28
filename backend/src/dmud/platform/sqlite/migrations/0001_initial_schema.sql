CREATE TABLE schema_migrations (version INTEGER PRIMARY KEY CHECK(version > 0)) STRICT;
CREATE TABLE operations (
 operation_id TEXT PRIMARY KEY,
 request_id TEXT NOT NULL UNIQUE,
 draft_id TEXT NOT NULL,
 payload_digest TEXT NOT NULL,
 payload TEXT NOT NULL CHECK(json_valid(payload)),
 resource TEXT NOT NULL CHECK(json_valid(resource))
) STRICT;
CREATE UNIQUE INDEX single_draft_mutation ON operations(draft_id) WHERE json_extract(resource, '$.status') IN ('accepted', 'validating');
CREATE TABLE session_zero_drafts (
 draft_id TEXT PRIMARY KEY,
 revision INTEGER NOT NULL CHECK(revision > 0),
 resource TEXT NOT NULL CHECK(json_valid(resource)),
 operation_id TEXT NOT NULL UNIQUE REFERENCES operations(operation_id)
) STRICT;
CREATE TABLE operation_events (
 operation_id TEXT NOT NULL REFERENCES operations(operation_id),
 event_id INTEGER NOT NULL CHECK(event_id > 0),
 resource TEXT NOT NULL CHECK(json_valid(resource)),
 PRIMARY KEY(operation_id, event_id)
) STRICT;
CREATE TABLE request_results (
 request_id TEXT PRIMARY KEY REFERENCES operations(request_id),
 operation_id TEXT NOT NULL UNIQUE REFERENCES operations(operation_id),
 draft_id TEXT NOT NULL REFERENCES session_zero_drafts(draft_id),
 resource TEXT NOT NULL CHECK(json_valid(resource))
) STRICT;
CREATE TABLE draft_commits (
 operation_id TEXT PRIMARY KEY REFERENCES operations(operation_id),
 draft_id TEXT NOT NULL UNIQUE REFERENCES session_zero_drafts(draft_id),
 revision INTEGER NOT NULL CHECK(revision > 0),
 payload_digest TEXT NOT NULL
) STRICT;
CREATE TRIGGER immutable_draft_commit_update BEFORE UPDATE ON draft_commits BEGIN SELECT RAISE(ABORT, 'immutable evidence'); END;
CREATE TRIGGER immutable_draft_commit_delete BEFORE DELETE ON draft_commits BEGIN SELECT RAISE(ABORT, 'immutable evidence'); END;
CREATE TABLE recovery_commands (
 request_id TEXT PRIMARY KEY,
 operation_id TEXT NOT NULL REFERENCES operations(operation_id),
 payload_digest TEXT NOT NULL,
 resource TEXT NOT NULL CHECK(json_valid(resource))
) STRICT;
