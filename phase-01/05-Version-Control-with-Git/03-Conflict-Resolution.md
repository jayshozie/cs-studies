# Conflict Resolution

## What is a merge conflict?

A merge conflict occurs when Git is unable to automatically integrate changes
from two different into a single, unified version. This typically hapens when:
- Two branches modify the same lines in the same file.
- One branch deletes a file that the other branch modifies.
- Two branches add a file with the same name in the same location, but with
    different content.

Git is smart, and it can automatically merge changes that don't overlap easily.
But when it encounters conflicting changes, it halts the merge process and asks
the developer to manually intervene and decide which changes to keep.

## What does a conflict look like? (Markers)

When a merge conflict occurs, Git modifies the conflicting files in the working
directory by adding special ***markers*** to indicate the conflicting sections.

- `<<<<<<< HEAD`: This marks the beginning of the conflicting changes from the
    current branch.
- `=======`: This separates the changes from the current branch (`HEAD`) from
    the changes of the branch the developer is trying to merge.
- `>>>>>>> <branch-name>`: This marks the end of tthe conflicting changes from
    the branch the developer is merging.

## Example Conflict

There is a file `file.txt` in the repository.

### Version of `file.txt` in the branch `main`:
```txt
Hello world!
This is the main branch.
```

### Version of `file.txt` in the branch `feature`:
```txt
Hello world!
This is my awesome feature.
```

If the developer tries to merge `feature` into `main`, `file.txt` will look
like this after the process halts:

```txt
Hello world!
<<<<<<< HEAD
This is the main branch.
=======
This is my awesome feature.
>>>>>>> feature
```

The part from `<<<<<<< HEAD` to `=======` shows the content of the current
`main` branch. The part from `=======` to `>>>>>>> feature` shows the content
from the `feature` branch the developer is merging.

## Usual Steps Taken to Resolve the Conflict

### Manual Resolve
1. **Check Status:**
    - Run `git status`. Git will list all conflicting files under an "Unmerged
        paths" seciton.
    - It will typically say "You have unmerged paths. (fix conflicts and run
        "git commit")".
    - `git status` is the developer's best friend during conflict resolution.
2. **Edit the Conflicting File(s):**
    - Open each file listed as "unmerged".
    - Locate the markers.
    - Manually edit the section between these markers to include the desired
        final content. The developer mustt decide which changes to keep,
        combine them, or write entirely new code.
    - Remove the markers.
3. **Add the Resolved File(s):**
    - Once the conflict is resolved and the markers removed, stage the file.
    ```bash session
    git add <conflicted-file-name>
    # e.g., git add file.txt
    ```
    - Repeat this for all conflicting files.
4. **Commit the Merge:**
    - After all connflicting files are staged, Git knows the merge is complete.
    - Now, the developer can commit the merge. Git will usually provide a
        default commit message; the developer can use it or modify it to
        explain how the conflicts were resolved.
    - This merge commit signifies that the conflicting changes have been
        successfully integrated.
5.  **Clean Up:**
    - After resolving and committing, you might want to remove the temporary
        merge branches, if applicable.

### Using a Merge Tool
For complex conflicts, manually editing can be tedious. Git allows you to
configure external merge tools (like VS Code's built-in merge editor, KDiff3,
Meld, Beyond Compare, etc.)

- After Git Reports a Conflict
    ```bash session
    git mergetool
    ```
    - This will open each conflicting file in the configured merge tool,
        providing a more visual and often easier way to resolve the
        differences.
    - Once you save and close the file in the merge tool, it often
        automatically stages the file as resolved.

## Important Things About Conflict Resolution

1. **COMMUNICATE!!!:**
Talk to the other developer(s) involved to understand their changes and intent.
This is the single most important thing.

2. **Resolve Early, Resolve Often:**
The longer you wait to merge or pull, and the more divergent the branches
become, the harder conflicts will be to resolve. Integrate `main` into your
feature branch frequently.

3. **Do NOT Guess:**
If you're unsure about how to resolve a conflict, ask for help. A wrong
resolution can mess up the entire project.

4. **Test After Resolution:**
After resolving conflicts and committing the merge, always run your tests to
ensure that the combined code works as expected and no regressions were
introduced.

## Some Other Conflict Scenarios

1. **Modify/Modify Conflict:**
This is the previously discussed conflict scenario. Both branches modify the
same lines of code within the same file.
    - **Resolution:** Manual editing to combine or choose one version, then
        `git add` and `git commit`.

2. **Delete/Modify Conflict:**
One branch deletes a file, while the other branch modifies the same file.
    - **How Git Shows This:** `git status` will show the file as "deleted
        by us" (if you deleted it) and "modified by them" (if the incoming
        branch modified it), or vice-versa. The file content might not even
        show the standard markers if it's a pure delete/modify.
    - **Resolution:**
        - If you want to keeeep the file and its modifications from the other
            branch, you'd effectively undo your deletion and acccept their
            changes. In a merge tool, you'd choose the "their" version.
            Manually, you'd restore the file, then `git add` it.
        - If you still want to delete the file, and disregard the changes from
            the other branch, you'd confirm the deletion. You might use
            `git rm <file-name>` if the file still exists locally from the
            merge attempt, then `git add` it.
        - You might explicitly tell Git which version to take:
            - To keep your version (delete the file): `git rm <file-name>`
                then `git commit`.
            - To keep their version (restore the file with their changes):
                `git checkout --ours <file-name>` (if their changes are the
                ones on `main` and you're merging `feature` into `main`) or
                `git checkout --theirs <file-name>` (if their changes are from
                the `feature` branch) then `git add <file-name>` then
                `git commit`. This part can be tricky and requires
                understanding `ours` vs `theirs` in the context of the merge
                direction.

3. **Add/Add Conflict (or Rename/Rename Different Content):**
Two different branches add a file with the exact same name in the exact same
directory, but the content of the files is different.
    - **How Git Shows This:** `git status` will show "both added" for that
        filename. The file might contain the markers showing both versions of
        the content.
    - **Resolution:** You must decide whether these are truly supposed to be
        the same file (and merge their content), or if they are intended to be
        two separate files that coincidentally have the same name.
        - If they are one file, resolve the content manually within the markers
            `git add`, `git commit`.
        - If they are two separate files, you'd typically resolve one to the
            intended content and then rename the other file to a unique name
            before staging and committing.

4. **Rename/Rename Conflict (Same File, Different Target Names):**
A file is rename in two different branches, but to different new names. Git
usually handles renames well, but if the new names clash or the content also
changes significantly, it can get confused.
    - **Resoluton:** You'll have to decide which new name to keep, or if you
        need both versions of the file under different names.

5. **Submodule Conflicts:**
If you're using Git submodules, conflicts can arise if the submodule's
committed state (the specific commit it points to) changes on different
branches in a conflicting way.
    - **Resolution:** This is usually about deciding which specific commit of
        the submodule to track. You'd go into the submodule directory, perform
        a `git pull` or `git checkout <commit-hash>` to the desired state, then
        go back to the parent repo, `git add` the submodule change, and
        `git commit`.

## Introduction to Git Merge Tools

Git allows you to configure an external "mergetool" that it will launch
automatically when you encounter a conflict and run `git mergetool`. These
tools provide a graphical interface that often shows you three or four panes:

- Local/Ours: The version of the file from your current branch
    (what you have locally).
- Remote/Theirs: The version of the file from the branch you're merging in.
- Base: The common ancestor version of the file before either conflicting
    change was made.
- Result/Merged: A pane where you combine the changes from the local and
    remote version to create the final, resolved file.

### Some Popular Merge Tools:

1. **VS Code:**
    - **Type:** Integrated Editor Merge Tool
    - **Pros:** If you already use VS Code as your primary editor, its built-in
        merge editor is incredibly intuitive and requires no extra setup. It
        provides a three-way merge view (current, incoming, result) with
        helpful "Accept Incoming", "Accept Current", and "Accept Both" buttons
        for individual conflict blocks.
    - **Setup:** Often auto-detected. If not, you can configure Git to use it.
2. **Meld:**
    - **Type:** Standalone Visual Diff & Merge Tool.
    - **Pros:** Cross-platform (Linux, Windows, macOS), open-source, and
        provides clear three-way comparison. Excellent forr comparing
        directories as well as files.
    - **Cons:** Requires separate installation.
    - **Setup:**
        ```bash session
        git config --global merge.tool meld
        ```
3. **KDiff3:**
    - **Type:** Standalone Visual Diff & Merge Tool.
    - **Pros:** Cross-platform (Linux, Windows, macOS), open-source, and offers
        both two-way and three-way diffs. Good for more complex merges.
    - **Cons:** Interface can look a bit dated to some users; requires separate
        installation.
    - **Setup:**
        ```bash session
        git config --global merge.tool kdiff3
        ```
4. **Beyond Compare:**
    - **Type:** Commercial Visual Diff & Merge Tool.
    - **Pros:** Highly powerful and user-friendly, with excellent features for
        comparing files, directories, and even FTP/cloud resources. Often
        considered a gold standard for professional use.
    - **Cons:** It's a commercial software (paid license required after trial).
    - **Setup:** Git often autodetects it if installed. Otherwise, specific
        configuration commands are available in its documentation.
5. **Sublime Merge:**
    - **Type:** Standalone Git Client with built-in Merge Tool.
    - **Pros:** From the creators of Sublime Text, it's very fast, has a
        beautiful interface, and provides a powerful merge editor. Cann be used
        as a full Git client or just for merging.
    - **Cons:** Commercial software (paid license required after trial).
    - **Setup:** A little bit more complicated, differs from platform to
        platform; check the documentation for more information.

### How to use `git mergetool`:

When Git reports a conflict (after `git merge`, `git pull`, or `git rebase`);

1. Run `git status` to see the unmerged files.
2. Run `git mergetool`.
3. Your configured merge tool will open for the first conflicting file.
4. Resolve the conflict within the merge tool (accepting changes, combining
    lines, etc.).
5. Save and close the file in the merge tool.
6. The merge tool will often automatically stage the file for you (`git add`).
7. If there are more conflicting files, Git will automatically open the next
    one in the merge tool.
8. Once all files are resolved and staged, run `git commit` to finalize the
    merge.
