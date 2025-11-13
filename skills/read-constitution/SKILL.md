---
name: read-constitution
description: This skill should be used to load the constitution
---

# Read Constitution

Load all coding constitution files into context to inform implementation.

## Purpose

This skill reads the constitution files that establish fundamental principles.

## Instructions

Read each file in the `.constitution` directory using the Read tool:

1. Use Glob tool to find all constitution files:
   ```
   pattern: "**/.constitution/**/*"
   ```
2. Read each constitution file found.
3. After loading the constitution, acknowledge that the content has been read and understood.

If no constitution directory is found, or if there are no files in the constitution directory, stop and reply with "No constitution files found".

**Skill loaded.** Constitution principles are now available to guide implementation.
