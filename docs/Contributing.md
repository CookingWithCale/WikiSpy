# Contributing Guide

## Submitting Bugs

**1.** Ensure the bug was not already reported by by reading the [Issues](https://github.com/WikiSpy/WikiSpy/issues).

**2.** Open `/docs/BUG_REPORT_TEMPLATE.md` and copy it's contents to the clipboard.

**3.** Create an issue, paste the template into the Issue body and fill it out.

## Feature Requests

**1.** Same as the instructions for submitting a bug report except with using `/docs/FEATURE_REQUEST.md`.

### Completing Issues

**1.** Clone the repo and create a branch for the IssueNuber:

```Console
git clone https://github.com/WikiSpy/WikiSpy.git
cd WikiSpy
git checkout -b Issue123
```

**2.** Complete the issue with passing unit tests and submit the completed issue:

```Console
git add --all
git commit -m "module_id.Add feature XYZ. #123"
git push origin Issue123
```

**3.** Create a Pull Requesting using the `/docs/PULL_REQUEST_TEMPLATE.md`

**4.** Get others to inspect your changes and merge the branch to the master.

**5.** Commit the changes into a branch named after the issue ticket you're mission solves.

```Console
git branch -m Issue123 Issue125
git add --all
git commit "ModuleID.Fix feature ABC. #125"
git push origin Issue125
```
