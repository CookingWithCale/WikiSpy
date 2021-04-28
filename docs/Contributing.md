## Contributing Guide

### Help Wanted

* Reverse contributor psychological profiling.
* Political bias detector - we're building a tool to determine a Wiki contributor's political bias by scanning their Wiki contributions and profile.
* MXNet, Stack AI - we're going to use deep learning for the Political bias detector with some A* stack AI for business model profiling with business model canvas.
* Website design - we're building the GUI with Flask in Python 3.
* Cyber war prevention - we're identifying cyber war threats on Wikipedia and mitigating them.
* Crowd source fact checkers - we need an arm of fact checkers to curate facts.
* Funding - we need to pay for programmers, dedicated servers and cloud GPU time, and essentials for a non-profit organization.

### Submitting Bugs

**1.** Ensure the bug was not already reported by by reading the [Issues](https://github.com/WikiSpy/WikiSpy/issues).

**2.** Open `/docs/BUG_REPORT_TEMPLATE.md` and copy it's contents to the clipboard.

**3.** Create an issue, paste the template into the Issue body and fill it out.

### Feature Requests

**1.** Same as the instructions for submitting a bug report except with using `/docs/FEATURE_REQUEST.md`.

#### Completing Issues

**1.** Clone the repo and create a branch for the IssueNumber:

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

**3.** Create a Pull Requesting using the `/docs/pull_request_template.md`

**4.** Get others to inspect your changes and merge the branch to the master.

**5.** Commit the changes into a branch named after the issue ticket you're mission solves.

```Console
git branch -m Issue123 Issue125
git add --all
git commit "ModuleID.Fix feature ABC. #125"
git push origin Issue125
```

#### Software Engineering Documentation

The software engineering documentation for the project can be found in the [Requirements Analysis Document](./RAD) and [Software Design Document](./SDD). If it's not clear from the documentation what work there is to do, please submit Issue tickets to Request for Clarification.

## License

Copyright © 2021 [Kabuki Starship](https://kabukistarship.com); all rights reserved.
