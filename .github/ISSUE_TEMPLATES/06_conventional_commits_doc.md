---
name: Conventional Commits - Docs
about: Instructions for practising Conventional Commits syntax.
title: "05 Conventional Commits - Docs"
labels: enhancement, help wanted
assignees: ""
---

Use the checklist to tick off the sub-tasks as you complete them. Some of the tasks rely on material that has already
been covered in the lesson so try and use what you have learnt. The commands are provided if required though.

- [ ] Create a branch for undertaking this work it should reflect your username and the issue number (remember to make
      sure `main` is up-to-date before branching).
- [ ] Add text to `README.md`.
- [ ] Stage and commit the changes using the [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)
      syntax. Make sure the following points are addressed.
  - [ ] An appropriate `type` field.
  - [ ] Is there a scope to the commit?
  - [ ] Is the change breaking? If so include the two indicators required.
  - [ ] Describe the change.
- [ ] Push your changes and make a Pull Request.
- [ ] Address Pull Request feedback and once approved merge your changes.

## Create a branch

This work tackles the issues number for the current issue, include it, prefixed with your GitHub username and a slash
(e.g. `ns-rse/`), the issue number then a short description.

```bash
git switch main
git pull
git switch -c ns-rse/8-update-readme
```

## Add text to `README.md`

Add the following text to the `README.md` at line 34, substituting `<repository_owner>` for the GitHub username of the
person who owns the repository.

```markdown
## Issues

If you find problems with this package and the results are inaccurate please create an
[issue](https://github.com/<repository_owner>/issues).
```

## Stage and commit changes

This change is concerned with documentation so we can use the `doc`-type for the commit. There is no particular scope
for the work since it is changing a file at the base of the repository rather than in a sub-directory so we can omit the
option `(<scope>)` component. The change is non-breaking so we do not need to flag it with `!`.

```bash
git add README.md
git commit -m "docs: Update README.md with details of xxx" -m "Closes #8 "
```

## Push Changes and make a PR

```bash
git push
```

## Address feedback and merge Pull Request

Address any feedback on the Pull Request and once complete merge the branch and delete it both on GitHub and from your
local repository.

```bash
git switch -c main
git pull
git branch -d ns-rse/8-udpate-readme
```
