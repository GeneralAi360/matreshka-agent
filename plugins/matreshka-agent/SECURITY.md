# Security policy

## Supported version

Security fixes are currently provided for version `0.1.x`.

## What the package does not contain

Matreshka Agent ships instruction skills and two local validation utilities. It does not ship hooks, MCP servers, apps, telemetry, background services, network clients, or dependency installers.

The validation utilities inspect local package files. `doctor.py` may also inspect command availability and Git status. Neither utility changes the inspected repository.

## Reporting a vulnerability

Do not publish credentials, personal data, exploit details, or an unpatched vulnerability in a public issue.

The verified private reporting address has not been selected yet. Before a public release, the maintainer must add a private security contact or enable private vulnerability reporting on the final source repository. Until then, keep the package private and share a report only with the maintainer through an already verified private channel.

Include the affected version, platform, reproduction steps, impact, and any safe supporting evidence. Never include real secrets.
