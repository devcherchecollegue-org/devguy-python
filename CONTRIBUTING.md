# Rules to contribute

Thanks for your help to devguy. To contribute, please:

- attribute your self to the issue you wish to solve
- fork the project (or create a branch if you have access)
- solve the issue
- test your solution
- format it with `black`
- make a clean and readable commit (see #format-commit)
- open your pull request !

PS: You should always work from a venv :)

## Format commit

Though we do not force a commit format we enforce that:

- title should synthesis work done (ex: refactor: Secure distinction between People and Bot in user /// fix: User updating_date not set)
- commit should describe the reason for work done (example: Refactored module user to allow distinction between bot users and normal user through a similar interface. /// User contains a bug when updating data: updated_at field was not set in code.)
- a commit message should describe the solution proposed (example: Creation of an abstract User class to enforce common methods. Creation of Person class implementing user for humans. Creation of Bot class ...)
- commit title and line should not exeed 80 chars

We would prefer a commit title following https://buzut.net/cours/versioning-avec-git/bien-nommer-ses-commits convetion but it 
is not mandatory.
