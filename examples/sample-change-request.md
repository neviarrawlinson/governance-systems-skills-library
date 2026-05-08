# Sample Change Request

Ticket: CHG-1001  
Title: Update production API gateway routing rule  
Environment: Production  
Change Type: Normal  
Planned Start: 2026-05-12 10:00 PM ET  
Planned End: 2026-05-12 11:00 PM ET

## Summary

The Platform team will update the production API gateway routing rule to direct traffic for the billing endpoint to the new backend service.

## Business Reason

The update is required to complete migration from the legacy billing service to the new billing service.

## Implementation Plan

1. Confirm deployment window.
2. Export current gateway configuration.
3. Apply new routing rule.
4. Restart gateway service.
5. Notify application owner.

## Validation Plan

The team will test the billing endpoint after the routing rule is applied.

## Rollback Plan

Restore the prior gateway configuration export and restart the gateway service.

## Risk and Impact

Possible temporary billing endpoint interruption during restart.

## Monitoring Plan

Application logs and API gateway metrics will be monitored after deployment.

## Approvals

Manager approval complete. Security review pending. CAB approval required.
