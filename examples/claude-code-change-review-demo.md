# Claude Code Demo: Change Review

## Scenario

A production change request is submitted with incomplete governance details.

## Prompt

```text
Use the review-change command to review this production change request.

Title: Production restart for application server
System: Reporting Service
Environment: Production
Change Type: Standard
Planned Start: Friday 9:00 PM
Planned End: Friday 9:30 PM
Implementation Plan: Restart the app server.
Validation Plan: Confirm the application is back online.
Rollback Plan: Not applicable.
Monitoring Plan: None listed.
Approvals: Manager approval pending.
```

## Expected Outcome

The command should identify that the change is not ready or only ready with conditions.
