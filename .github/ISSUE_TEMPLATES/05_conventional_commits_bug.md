---
name: Conventional Commits - Bug
about: Instructions for practising Conventional Commits syntax.
title: "05 Conventional Commits - Bug"
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
