# Sample Input: Change Governance Review

Review the following change request for governance completeness and CAB readiness.

## Change Request

**Ticket:** CMCC-1245  
**Title:** Update production API gateway timeout configuration  
**Environment:** Production  
**Change Type:** Standard  
**Requested By:** Platform Engineering  
**Planned Start:** 2026-05-12 9:00 PM PT  
**Planned End:** 2026-05-12 9:30 PM PT  

## Summary

Increase the API gateway timeout value from 30 seconds to 60 seconds to reduce timeout failures during high-volume call processing windows.

## Implementation Plan

1. Confirm no active deployment freeze.
2. Export current gateway timeout settings.
3. Update timeout value in the production gateway configuration.
4. Restart the gateway service during the approved maintenance window.
5. Confirm service is accepting traffic.

## Validation Plan

Engineering will confirm that API calls complete successfully after the configuration update.

## Rollback Plan

Revert timeout value back to 30 seconds and restart gateway service.

## Risk and Impact

Low customer impact expected. Short restart may cause brief connection retries.

## Monitoring Plan

Monitor API latency and error rate in Datadog for one hour after implementation.

## Approvals

Manager approval complete. Security and Compliance not required according to requester.
