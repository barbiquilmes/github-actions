# Github Actions

__Continuous integration__ is all about integrating new code or code changes into an existing code base by building that code automatically.
So that changed code by testing it automatically and by then merging it into existing code.

__Continuous delivery__ or deployment is about publishing new versions of your app or package or website automatically after the code has been tested and integrated.

## Recap
### Some terms
Git is a free version control system tool.

GitHub is a company, and it is a company that offers cloud Git repositories and services related to that code which you're managing in the cloud.

commits: code snapshots

HEAD is basically a pointer managed by Git that controls which commit is currently visible
in our project. HEAD points at the commit that's currently loaded.

git log: shows all commits that are older than the current commit

### Undo a commit (revert)

```
git revert <commit-id>
```
Reverts the changes that were made by the commit-id. It doesnt delete the commit, it just creates a new commit that reverts the changes.

### Reset a commit

```
git reset --hard <commit-id>
```

All commits after the commit-id will be deleted. The commit-id will be the new HEAD. History will be deleted.

origin is a local identifier for the remote repository, meaning a pointer to the remote repository.

### Connect a repository

```
git remote add origin <url>: adds a remote repository to the local repository
```

## Triggers

https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows

workflow_dispatch: Manually trigger a workflow run.
pull_request: Triggered when a pull request is assigned, unassigned, labeled, unlabeled, opened, edited, closed, reopened, synchronize, ready_for_review, locked, unlocked or when a pull request review is requested or removed.
push: Triggered when a Git push is performed to a branch or a tag.

## Actions

https://github.com/marketplace/actions/checkout

checkout: Checks-out your repository under $GITHUB_WORKSPACE, so your workflow can access it.

## Runners

https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners

Under Preinstalled software, to see what is already installed.


