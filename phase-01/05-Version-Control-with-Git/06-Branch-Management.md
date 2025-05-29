# Branch Management in Git

Branches are lightweight, movable pointers to commits. They are essential for
isolating development work, allowing multipiple developers to work on different
features or bug fixes simultaneously without interferinng with each other's
code.

1. **Listing Branches**

The `git branch` command allows you to see exitsing branches.

- `git branch`
    Lists all local branches in the repository. The currently active branch
    will be marked with an asterisk (`*`).
    ```bash session
    git branch
    # Example Output:
    #   feature/new-auth
    # * main
    #   bugfix/login-issue
    ```
    In the example output, `main` is the currently checked-out branch.

- `git branch -r`
    Lists all remote-tracking branches. These are local references to branches
    on the remote repository. (e.g., `origin/main`)
    ```bash session
    git branch -r
    # Example Output:
    #   origin/HEAD -> origin/MAIN
    #   origin/main
    #   origin/feature/new-dashboard
    ```

- `git branch -a`
    Lists both local and remote-tracking branches.

- `git branch -vv`
    Shows more detail, including the upstream branch the local branches are
    tracking (if any) and the last commit on each branch. This is very helpful
    for seeing if the local branch is ahead or behind its remote counterpart.
    ```bash session
    git branch -vv
    # Example Output:
    #   feature/new-auth   8a4b2c1 [origin/feature/new-auth: ahead 3] Add auth logic
    # * main               00d082b [origin/main] announcement added, curriculum.md added
    #   bugfix/login-issue f3e1d09 Update login form
    ```

2. **Creating Branches**

User typically creates a new branch when they start working on a new feature,
bugfix, or experiment.

- `git branch <new-branch-name>`
    Creates a new branch, but does not switch to it. The new branch will point
    to the same commit as the current `HEAD`.
    ```bash session
    git branch my-new-feature
    git branch
    # Example Output:
    #   my-new-feature
    # * main
    ```
    User is still on `main` after this command.

- `git checkout -b my-awesome-feature`
    This is the most common way to create a new branch, as it creates the
    branch and immediately switches to it. It's a convenient shortcut for
    `git branch <new-branch-name>` followed by `git checkout <new-branch-name>.
    ```bash session
    git checkout -b my-awesome-feature
    # Example Output:
    # Switched to a new branch 'my-awesome-feature'
    git branch
    #   main
    # * my-awesome-feature
    ```

- `git checkout -b <new-branch-name> <start-point>`
    User can also create a new branch based on a specific commit, tag, or
    another branch, instead of the current `HEAD`.
    ```bash session
    git checkout -b experimental-branch old-feature-branch
    # Creates a new branch from an existing old-feature-branch
    git checkout -b fix-for-v1.0 v1.0
    # Creates a new branch from the 'v1.0' tag
    git checkout -b hotfix-from-specific-commit 0a1b2c3d
    # Creates a new branch from a specific commit hash
    ```

3. **Switching Branches**

- `git checkout <branch-name>`
    
    Switches the working directory and `HEAD` to the specified branch. Any
    changes the user has in their working directory that are not commited or
    stashed will be carried over to the new branch if Git can apply them
    without conflict.
    ```bash session
    git checkout main
    # Example Output:
    # Switched to branch 'main'
    ```
    **IMPORTANT:**
    If the user has uncommitted changes, Git might prevent them from switching
    branches to prevent overwriting their work. The user needs to commit or
    sttash the changes first.

- `git switch <branch-name>`
    Introduced in Git 2.23 (alongside `git restore`) to provide a clearer
    separation of concerns. `git switch` is only for switching branches, making
    its intent clearer than `git checkout` which had overloaded functionality
    (checkiing out files, branches, commits).

4. **Deleting Branches**

Once a feature branch has been merged into its target branch (e.g., `main` or
`develop`), user will typically delete it to keep their repository clean.

- `git branch -d <branch-name>`
    Deletes local branch only if it has been fully merged into the current
    `HEAD` (or if the user specify a branch it has been merged into). This is
    the safe way to delete a branch, as it prevents the user from losing work
    that hasn't been integrated.
    ```bash session
    git checkout main
    # Switch to main (it's not possible to delete the branch the user is on)
    git branch -d my-awesome-feature
    # Example Output:
    # Deleted branch my-awesome-feature (was 1a2b3c).
    ```

- `git branch -D <branch-name>`
    Force delete the local branch, regardless of its merged status. Use this
    with caution, as you can lose unmerged work. This is typically used for
    discarding experimental branches that will never be merged.
    ```bash session
    git branch -d old-experimental-branch # Use with care
    # Example Output:
    # Deleted branch old-experimental-branch (was 5d6e7f8).
    ```

- **Deleting Remote Branches**
    Deleting a local branch does not delet its counterpart on the remote. To
    delete a remote branch:
    ```bash session
    git push origin --delete my-awesome-feature
    # or
    git push origin :my-awesome-feature
    # Example Output:
    # To https://github.com/jayshozie/paths.git
    #  - [deleted]         my-awesome-feature
    ```
