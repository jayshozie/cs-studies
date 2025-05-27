# Git Workflows Notes

## Intro

### What is the difference between Git commands and a Git workflow?
- Individual Git commands are the individual tools in the Git toolbox. They
    tell Git what specific action to perform.

- A Git workflow is a prescribed set of conventions, strategies, and procedures
    for how a team (or individuals on large projects) use those Git commands to
    manage their codebase and collaborate effectively.

### Common Git Workflows:

1. **Centralized Workflow:**
    - **Concept:** Simplest, most direct workflow, mimicking older version
        control systems like SVN. All development happens on a single `main`
        or `master` branch. Developers pull, commit, and push directly to
        `main`.
    - **Pros:** Very simple for small teams or solo projects.
    - **Cons:** Can quickly lead to conflicts and unstable `main` if not
        managed very carefully. Not ideal for larger teams or projects with
        concurrent features.
    - **Core Principles:**
        - Single Source of Truth
        - Sequential Development

2. **Feature Branch Workflow:**
    - **Concept:** It's built on top of the centralized workflow. For every new
        feature or bug fix, developers create a separate branch off of `main`
        (or any stable branch). All work for that feature happens on this
        branch. Once complete, the feature branch is merged back into `main`,
        and then typically deleted.
    - **Pros:** Isolated the development, keeps `main` stable, encourages code
        review before integration. Very popular.
    - **Cons:** Can lead to many short-lived branches.
    - **Core Principles:**
        - Isolation of Work
        - Stable `main` Branch
        - Collaboration and Review
        - Parallel Development

3. **GitFlow Workflow:**
    - **Concept:** This is a more complex, highly structured workflow
        specifically designed for projects with scheduled releases. It uses
        several long-lived branches in addition to feature branches:
        - `main`: Always contains production-ready code.
        - `develop`: Integration branch for all new features.
        - `feature/*`: For developing new features.
        - `release/*`: For preparing new releases (bug fixes, final tweaks).
        - `hotfix/*`: For quickly patching critical bugs in production.
    - **Pros:** Excellent for managing complex cycles and ensuring a stable
        production branch.
    - **Cons:** Can be overkill and too complex for smaller, rapidly iterating
        teams.
    - **Core Principles:**
        - **Two Primary Long-Lived Branches:**
            1. **`main` (or `master`):** This branch always reflects the
                production-ready state of the project. Every commit on `main`
                should be a release.
            2. **`develop`:** This branch contains the latest integrated
                development changes for the next release. All new features are
                ultimately merged into `develop`.
        - **Supporting Short-Lived Branches:**
            1. **`feature` Branches:** Used for developing new features. They
                branch off `develop` and merge back into `develop`.
                **Format:** `feature/<name>`
            2. **`release` Branches:** Used for preparing new releases. They
                branch off `develop`, allow for last-minute bug fixes and
                preparation, and then merg back into both `main` and `develop`.
                **Format:** `release/<version>`
            3. **`hotfix` Branches:** Used for quickly patching critical bugs
                in the production (`main`) branch. They branch off `main` and
                merge back into both `main` and `develop`.
                **Format:** `hotfix/<name>`

4. **GitHub Flow:**
    - **Concept:** This is a much simpler, lightweight, and continuous
        delivery-oriented workflow, popular with many open-source projects and
        companies using GitHub. It's essentially a streamlined Feature Branch
        Workflow.
        1. Anything in `main` is deployable.
        2. To work on something new, create a descriptively named branch off
            `main`.
        3. Commit often to that branch.
        4. When you need feedack or want to merge, open a PR.
        5. Once reviewed and approved, merge to `main`.
        6. Deploy immediately.
    - **Pros:** Very simple, fast, and promotes continuous integration and
        deployment. Ideal for agile teams.
    - **Cons:** Less structured for complex release management than GitFlow.
    - **Core Principles:**
        - Anything in `main` is deployable
        - Create a descriptively-named branch off `main` to
            work on something new
        - Commit often to that branch
        - Open a PR
        - Merge into `main`
        - Deploy immediately
