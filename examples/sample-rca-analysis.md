# Sample RCA Input

Incident: Production login outage  
Date: 2026-04-22  
Duration: 47 minutes  
System: Customer login service  
Customer Impact: Users could not log in during the incident window.

## Timeline

- 9:02 AM: Customer support reported increased login failures.
- 9:10 AM: Engineering began investigation.
- 9:22 AM: Issue traced to expired certificate on authentication proxy.
- 9:37 AM: Certificate renewed.
- 9:49 AM: Login service confirmed stable.

## Root Cause

The authentication proxy certificate expired.

## Resolution

The certificate was renewed and the service returned to normal.

## Corrective Actions

- Add calendar reminder for certificate renewal.
- Review other certificates.
