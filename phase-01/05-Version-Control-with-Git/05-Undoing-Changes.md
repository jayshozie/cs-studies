# Undoing Changes with Git

There are 3 main commands that are used to "undo" or reverse changes in Git
repositories. They work fundamentally different.

1. `git restore`

    - **Purpose**
        To discard changes in the working directory or staging area. It helps
        the user to "unmodify" or "unstage" files. It was introduced in Git
        2.23 to clarify the behavior previously handled by `git checkout` for
        files.

    - **What does it do?**
        - **Unmodifying files in the working directory**
            Reverts a file to its last committed state (or staged state). This
            means any edits you've made to the file since your last commit or
            `git add` will be lost.
        - **Unstaging files**
            Removes a file from the staging area (`git add`) without affecting
            its content in the working directory.

    - **When to use it?**
        - User made changes to a file but decided they don't want them.
        - User accidenally ran `git add` and staged files they didn't mean to.

    - **Key Points:**
        - **Local Only**
            Affects only the users local working directory and staging area.
            Does not touch the commit history.
        - **Destructive to Unsaved Work**
            Changes are lost if not committed.

    - **Commands:**
        - `git restore <file-name>`
            Discards changes in the working directory of `<file_name>`.
            (Reverts it to its staged state, or if not staged, to its last
            committed state.)
        - `git restore --staged <file_name>`
            Unstages `<file_name>` (Moves it from staging area back to working
            directory, keeping current edits.)
        - `git restore --source=<commit-hash> <file_name>`
            Restores `<file_name>` to its state at a specific `<commit-hash>`.

2. `git revert`

    - **Purpose:** To undo a specific commit by creating a new commit that
        reverses the changes introduced by the original commit.

    - **What does it do?**
        It creates a new commit that is the "opposite" of the commit the user
        is reverting. If the original commit added a line, the revert commit
        removes it. If the original commit removed a line, the revert commit
        adds it back.

    - **When to use it?**
        - User already a pushed a commit to a shared remote repository, and the
        user wants to undo it without rewriting shared history. This is the
        safest way to undo commits that have already been pushed.

        - User wants to undo an old commit in the middle of the history without
        affecting subsequent commits.

    - **Key Points:**
        - **Non-Destructive History**
            It preserves the original commit and its history. This is why it's
            safe for shared branches.
        - **Create a New Commit**
            Git history moves forward, showing both the original commit and the
            revert commit.
        - Can cause merge conflicts if subsequent commits modified the same
        lines.

    - **Command:**
        - `git revert <commit-hash>`
            Creates a new commit that undoes the changes in the specified
            commit. Git will open the editor for the commit message.

3. `git reset`

    - **Purpose:** To move the `HEAD` pointer (and optionally the branch
        pointer) to an older commit, effectively rewriting history from that
        point forward. It allows the user to "undo" commits by making Git
        forget they ever happened in that branch.

    - **What does it do?**
        It moves the `HEAD` pointer to a specified commit. The effect on the
        users working directory and staging area depends on the `mode` they
        choose.

    - **When to use it?**
        - User wants to undo local commits that haven't been pushed to a shared
        remote yet.
        - User wants to clean up local history before pushing.
        - User wants to discard cchanges in the staging area and/or working
        directory.

    - **Key Points:**
        - **Rewrites History**
            Because it moves the branch pointer, it can make commits
            unreachable. This is dangerous if used on commits that have already
            been pushed to a shared remote, as it will cause divergence for
            other team members.

        - **Multiple Modes**
            - `--soft`
                Moves `HEAD` and the branch pointer, but keeps all changes from
                the "reset" commits in the staging area. User can then
                `git commit` them again as a single new commit.
                ```bash session
                git reset --soft HEAD~1
                # Un-commits the last commit, keeps changes staged
                ```
            - `--mixed` (default)
                Moves `HEAD` and the branch pointer, and moves changes from the
                "reset" commits to the working directory (unstaged).
                ```bash session
                git reset --mixed HEAD~1
                # Un-commits the last commit keeps changes in working directory
                git reset HEAD^
                # Same as HEAD~1, default mode is --mixed
                ```
            - `--hard`
                Moves `HEAD` and the branch pointer, and discards all changes
                from the "reset" commits in both the staging area and the
                working directory. This is destructive.
                ```bash session
                git reset --hard HEAD~1
                # Discards the last commit and all its changes
                ```


        - **`HEAD~N` or `HEAD^N`**
            Refers to `N` commits before `HEAD`. `HEAD~1` is the commit before
            the current one.
