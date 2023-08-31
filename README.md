# Github Actions

__Continuous integration__ is all about integrating new code or code changes into an existing code base by building that code automatically.
So that changed code by testing it automatically and by then merging it into existing code.

__Continuous delivery__ or deployment is about publishing new versions of your app or package or website automatically after the code has been tested and integrated.

Git is a free version control system tool.

GitHub is a company, and it is a company that offers cloud Git repositories and services related to that code which you're managing in the cloud.

commits: code snapshots


HEAD is basically a pointer managed by Git that controls which commit is currently visible
in our project. HEAD points at the commit that's currently loaded.

git log: shows all commits that are older than the current commit

## Undo a commit (revert)

```
git revert <commit-id>
```
Reverts the changes that were made by the commit-id. It doesnt delete the commit, it just creates a new commit that reverts the changes.

## Reset a commit

```
git reset --hard <commit-id>
```

All commits after the commit-id will be deleted. The commit-id will be the new HEAD. History will be deleted.

