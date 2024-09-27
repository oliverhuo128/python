# PY02.Pandas

The `PY02.Pandas` project is the root project for this module.  Each folder is a unit of the module, and maintained on separate branch, i.e. one branch for each unit. There is also a separate branch for the solutions to each unit's work (which are stored in a subfolder called Solutions.)

There are two additional projects derived from `PY02.Pandasn`:

1. The `PY02.Pandas.AllUnits` project pulls all these units into a single branch, so it can be shared more easily.  

2. The `PY02.Pandas.WithSolutions` also includes all the Solutions branches.

## Target Workflow for Persona 1 (as part of scheduled cohort training)

- Create an empty, single-branch project `PY02.Pandas.DEXXX`
- Fork this project for each consultant
- At the start of each session, push the relevant units to `PY02.Pandas.DEXXX`
- Each's consultant's repository is updated to include that content.
- Each consultant pushes their work to their project. These projects can be pulled by training team for monitoring and feedback.
- Also, for each unit, if/when the trainer wants to share its 'Solutions' branch, this is pushed to `PY02.Pandas.DEXXX` at which point consultants are able to pull this content into their individual projects.

## Workflow for Persona 2 (on-site and bench training)

- Fork the project `PY02.Pandas.AllUnits`, into a project for that consultant.
- The consultant can push work to their project
- This projects can be pulled by training team for monitoring and feedback.
- Solutions can be provided to the consultant either:
  - Unit by unit, i.e. for a given unit, pushing its `Solution` branch to the consultant's project
  - All at once, i.e. forking the project `PY02.Pandas.WithSolutions` into a project for the consultant.
