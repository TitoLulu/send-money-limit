Hey, good work getting to this. I noticed a few issues that need to be addressed before merging the PR: 3 functional issues, 1 design issue, and a few test coverage gaps.

## Functional Issues

1. **Off-by-one in limit check** — `limits.py:59` uses `>=` instead of `>`, so `check_daily_limit` blocks amounts that land exactly at the limit.
2. **Timezone inconsistency** — `limits.py:29-30` uses `datetime.utcnow()` whereas `countries.py` uses country-specific timezones.
3. **Inconsistent daily limit computation** — `limits.py:43-52` filters out `FAILED` and `SUSPENDED` transfers, but `schema.py:81` does not.

## Design Issue

The `COUNTRY_INFO` design observation is sharp. However, implementing it as-is makes it painful to scale: it requires touching every user row, leading to full table scans and row-level locks that can make the database unavailable. Worth discussing whether a `countries` or `country_info` table with a foreign key relation to the user table is the right model.

## Test Coverage Gaps

**Critical:**

1. **Conflicting test name and assertion** — `test_transfers.py:31` (`test_can_send_again_after_a_reversal`): reversed transfers should add to the daily send overhead, but the assertion expects an error.
2. No test for sending exactly at the limit.
3. No test to verify that day boundaries use local time.

**Low priority:**

1. `transfers.py:44-45` raises `TransferError` for `amount <= 0` but there is no test exercising this path.
2. No test for the edge case where a user tries to send money to a non-existent recipient.
