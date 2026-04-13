# Merge Strategy: Prioritize Local Changes

This document outlines how to resolve merge conflicts with Overleaf by prioritizing local changes.

## Quick Resolution Commands

If you encounter merge conflicts when syncing with Overleaf:

### Option 1: Force Local Changes (Recommended)
```bash
# Pull with strategy to prefer local changes
git pull origin main --strategy-option=ours

# Or if conflicts occur, resolve by keeping local versions:
git checkout --ours <file>
git add <file>
git commit -m "Resolve merge conflict: keep local version"
```

### Option 2: Reset to Local State
```bash
# If you want to completely overwrite remote with local:
git push origin main --force
# WARNING: This will overwrite any changes on Overleaf
```

### Option 3: Manual Conflict Resolution
```bash
# When conflicts occur, edit files to keep local content
# Then:
git add .
git commit -m "Resolve merge conflicts: prioritize local changes"
```

## Git Configuration (Run locally)

To automatically prefer local changes during merges:

```bash
git config merge.ours.driver true
```

Or create/edit `.gitattributes`:
```
* merge=ours
```

## Overleaf Sync Notes

- Overleaf syncs with the GitHub repository
- Local changes should be pushed to GitHub first
- If Overleaf has conflicting changes, use the strategies above
- Always backup your work before force pushing
