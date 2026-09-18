# /fix-issue

Prerequisite: an approved plan must already exist in the session.

Implements the approved fix:

1. Make the smallest safe change that resolves the issue.
2. Add a regression test (fails before the fix, passes after).
3. Run targeted tests for the changed files.
4. Report every changed file and why.
5. No changes outside the approved plan's scope.

After tests pass, update `logs/session-state.md`.
