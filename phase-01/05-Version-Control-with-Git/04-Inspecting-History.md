# Inspecting History of a Git Repository

Understanding the history of a project is crucial for debugging, auditing, code
review, and simply gaining context about how the codebase evolved. While
`git log` by itself showsa a basic list of commits, its real power comes from
its many options for filtering, formatting, and presenting that history.

## Why Iis Inspecting History Important?

- **Debugging:** Find out when a bug was introduced and by who by examining
    changes around the time the bug appeared.
- **Code Review:** Understand the context of channges in a pull request.
- **Auditing:** Trace features, bug fixes, or changes through the project's
    timeline.
- **Understanding Evolution:** See how a particular file or feature has changed
    over time.
- **Collaboration:** Understand what other developers have been working on.

## A Basic `git log` Recap

When `git log` is ran, it gives out a detailed list of commits in reverse
chronological order (newest first). Each entry includes:

- Commit hash (SHA-1)
- Author name and email
- Date and time
- Commit message

## Advanced `git log` Options

1. **Limiting the Output**

- `-n <number>` or `--max-count=<number>`: Show only the last `n` commits.
    ```bash session
    git log -5 # Shows the last 5 commits
    ```
- `--since=<date>` or `--until==<date>`: Filter commits by date. Dates can be
    absolute (`"2025-01-01"`) or relative (`"2 weeks ago"`, `"yesterday"`).
    ```bash session
    git log --since="2024-05-01"
    git log --until="yesterday"
    git log --since="2 weeks ago" --until="1 week ago!
    ```
- `--author="<name>"`: Show commits by a specific author.
    ```bash session
    git log --author="jayshozie"
    ```
- `--grep="<pattern>"`: Filter commits by a pattern in their commit message.
    ```bash session
    git log --grep="fix bug" # Case-sensitive by default
    git log --grep="feature" -i # -i for case-insensitive
    ```
- `--all-match` Use with multiple `--grep` or `--author` to match all criteria.
- `<path>`: Show commits that affected a specific file or directory.
    ```bash session
    git log curriculum.md # Shows commits that changed curriculum.md
    git log phase-1/ # Shows commits that changed anything in 'phase-1/' dir
    ```
- `<branch-name>`: Show commits reachable from a specific branch.
    ```bash session
    git log feature/new-login # Shows commits on the feature/new-login branch
    ```
- `<branch1>..<branch2>`: Shows commits that are on `branch2` but not on
    `branch1`. Useful for seeing what's new in a branch before merging.
    ```bash session
    git log main..feature/new-feature # What's in new-feature that's not in main
    ```
- `<commit-hash>`: Show history starting from a specific commit.
    ```bash session
    git log 00d082b # Shows history from this commit backwards
    ```
2. **Formatting the Output:**

- `--oneline`: Shows eeach commit on a single line, displaying only the short
    hash and the commit message. This is excellent forr a quick overview.
    ```bash sesion
    git log --oneline
    ```
- `--graph`: Draws an ASCII art graph of the branch and merge history. Best
    used with `--oneline` and `--decorate`.
    ```bash session
    git log --oneline --graph --decorate
    ```
- `--decorate`: Shows branch and tag names next to the commits thep point to.
    Often used with `--oneline` and `--graph`.
    ```bash session
    git log --oneline --decorate
    ```
- `--pretty=format:"<format-string>"`: Provides control over the output format
    using placeholders.
    - `%H`: full commit hash
    - `%h`: abbreviated commit hash
    - `%an`: author name
    - `%ad`: author date
    - `%s`: subject (commit message)
    - `%d`: ref names (branches, tags)
    ```bash session
    git log --pretty=format:"%h %an %ad - %s%d" --graph --all
    # Output:
    # * 00d082b jayshozie Tue May 27 11:30:00 2025 +0300 - announcement added, curriculum.md added (HEAD -> master, origin/master)
    # * 3f7cf55 jayshozie Mon May 26 22:00:00 2025 +0300 - Initial commit
    ```
- `--stat`: Shows a short summary of which files were modified and how many
    lines were added/deleted for each commit.
    ```bash session
    git log --stat
    ```
- `-p` or `--path`: Shows the actual diff (patch) introduced by each commit.
    This is incredibly useful for seeing the exact line-by-line changes.
    ```bash session
    git log -p -1 # Show pattch for the last commit only
    git log -p curriculum.md # Show patches for changes to curriculum.md
    ```

3. **Viewing Specific Commits:**

- `git show <commit-hash>`: Displays the commit details (author, date, message)
    and the full patch (diff) for a single specific commit.
    ```bash session
    git show 00d082b # Shows dtails and diff for commit 00d082b
    ```
