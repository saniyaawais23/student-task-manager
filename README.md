A Python console app to manage student tasks

Project status: Testing


# Student Task Manager

A Python console app to manage student tasks.

Project status: Testing

## Features
- Add tasks (empty titles are rejected)
- Display all tasks
- Mark tasks as completed
- Delete tasks by ID (invalid IDs are rejected)

## Setup
```
git clone https://github.com/saniyaawais23/student-task-manager.git
cd student-task-manager
```
Requires Python 3.x. No extra packages are needed.

## Usage
```
python main.py
```
Choose an option from the menu: 1 Add, 2 Show, 3 Complete, 4 Delete, 5 Exit.
See [docs/user-guide.md](docs/user-guide.md) for details.

## Running Tests
```
python -m unittest discover -s tests -v
```
Tests also run automatically on GitHub Actions for pushes and pull requests to `main`.

## License
MIT