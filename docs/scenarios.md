# Practical scenarios

## File integrity

Calculate the SHA-256 of an authorized sample, store the expected reference independently, and verify the sample later. A matching hash only confirms equality to the reference.

## Log review

Run log-summary on examples/events.jsonl. Compare counts with the source records. Invalid lines are reported separately; severity labels do not establish conclusions about incidents.

## Inventory

Run inventory on a local directory containing synthetic documents. Record the returned names, sizes and UTC timestamps. Review changes against the expected inventory manually.
