Read each file in the `.constitution` directory.

If the `.constitution` directory does not exist or is empty, query the user if they want to automatically download examples using this command:
```bash
curl -L https://github.com/tordks/claude-workflow/archive/refs/heads/main.tar.gz | tar xz --strip=2 claude-workflow-main/data/.constitution
```

Then read each file in the `.constitution` directory.

After loading the constitution, acknowledge that you have read and understood the content.