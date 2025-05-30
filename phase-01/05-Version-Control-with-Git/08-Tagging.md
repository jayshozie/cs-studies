# Tagging in Git

Tags in Git are essentially permanent, unmoving pointers to specific commits.
Unlike branches, which are designed to move and evolve, tags are typically used
to mark release points (e.g. `v1.0`, `v2.0-beta`), specific milestones, or
important historical moments in your project.

## Two Main Types of Tags:

1. **Lightweight Tags**
    - Think of these as simple, unchangeable pointers to a commit. They are
    just a name and a commit hash.
    - They don't store any extra information like author, date, or message.
    - They are similar to a branch that never moves.
    - Not recommended for public releases, as they lack metadata.
2. **Annotated Tags**
    - These are full Git objects, stored in the Git database.
    - They include a tagger name, email, and date, along with a tagging
    message.
    - They can also be GPG-signed for verification.
    - High recommended for public release because they contain valuable
    metadata and can be verified.

-------------------------------------------------------------------------------

1. **Listing Tags**
    - `git tag`
        Lists all tags in your repository in alphabetical order.
        ```bash session
        git tag
        # Example Output:
        # v1.0
        # v1.1-beta
        # v2.0
        ```

    - `git tag -l`
        Lists tags matching a specific pattern.
        ```bash session
        git tag -l "v1.*"
        # Example Output:
        # v1.0
        # v1.1-beta
        ```

    - `git show <tag-name>`
        Displays the commit information and message associated with a specific
        tag (especially useful for annotated tags).
        ```bash session
        git show v2.0
        # Example Output (for an annotated tag):
        # tag v2.0
        # Tagger: John Doe <john.doe@example.com>
        # Date: Wed May 28 15:02:34 +0000
        #
        # Final release of version 2.0 with all new features
        #
        # commit abcdef1234567890... (HEAD -> main, tag: v2.0)
        # Author: ...
        # Date:   ...
        #
        # Merge branch 'feature/new-design' into main
        # ... (diff for the commit)
        ```

2. **Creating Tags**
    - **Lightweight Tag**
        Created by simply providing a name. It points to your current `HEAD`
        commit by default.
        ```bash session
        git tag v1.2-alpha
        ```

    - **Annotated Tag**
        Created using the `-a` or `--annotate` flag, which prompts for a
        message.
        ```bash session
        git tag -a v2.0 -m "Release version 2.0 with major feature updates."
        ```
        Alternatively, you can create a tag pointing to an older commit (not
        your current `HEAD`) by providing its hash:
        ```bash session
        git tag -a v1.0.1_hotfix 0a1b2c3d
        # Creates an annotated tag at commit 0a1b2c3d
        ```

3. **Pushing Tags to Remote**
    By default, `git push` does not push tags to the remote repository. You
    need to explicitly push them.

    - **Single Tag**
    ```bash session
    git push origin v2.0
    ```

    - **ALl Tags At Once**
    ```bash session
    git push origin --tags
    ```

4. **Deleting Tags**
    `git tag -d <tag-name>`
    - **Delete a Local Tag**
    ```bash session
    git tag -d v1.2-alpha
    # Example Output:
    # Deleted tag `v1.2-alpha1 (was 1a2b3c4)
    ```
    - **Delete a Remote Tag**
    Deleting a local tag does not delete its counterpart on the remote. You
    must explicitly tell the remote to delete it.
    ```bash session
    git push origin --delete v1.2-alpha
    # or
    git push origin :refs/tags/v1.2-alpha
    # Example Output:
    # To https://github.com/jayshozie/paths.git
    #  - [deleted]         v1.2-alpha
    ```
