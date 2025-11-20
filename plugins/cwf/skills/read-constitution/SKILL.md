---
name: read-constitution
description: This skill should be used to load the constitution files located in .constitution
---

## Instructions

Read each file in the `.constitution` directory using the Read tool:

1. Use Glob tool to find all constitution files:

   ```yaml
   pattern: "**/.constitution/**/*"
   ```

2a. If no files are found, then we don't need to read any files.
2b. If a .constitution folder exists and there are any files in it, use the Read tool to read each constitution file found.
