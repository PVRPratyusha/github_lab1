# GitHub Lab 1 - Calculator with CI/CD

This project demonstrates a Python calculator application with automated testing using GitHub Actions CI/CD pipeline.

## Project Overview

A simple calculator module that provides basic arithmetic and mathematical operations, with comprehensive unit tests and automated continuous integration.

```
Lab1/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI/CD configuration
├── data/
│   └── init.py
├── src/
│   ├── __init__.py
│   └── calculator.py          # Calculator implementation
├── test/
│   ├── init.py
│   └── test_calculator.py     # Unit tests using pytest
├── .gitignore
├── requirements.txt
└── README.md
```

## Features

The calculator includes the following functions:
- **Basic Arithmetic**: Addition, Subtraction, Multiplication, Division
- **Advanced Operations**: Power, Square Root, Modulo, Absolute Value
- **Error Handling**: Proper validation for division by zero and negative square roots

## Project Structure

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- Git installed on your system
- GitHub account
- SSH key configured for GitHub

### SSH Configuration (Recommended)

Using SSH instead of HTTPS provides a more secure and convenient way to interact with GitHub.

#### Setting Up SSH Keys

**Step 1: Generate SSH key** (if you don't have one)

Run the command: `ssh-keygen -t ed25519 -C "your_email@example.com"`

Press Enter to accept the default location and optionally set a passphrase.

**Step 2: Copy your public key**

Run the command: `cat ~/.ssh/id_ed25519.pub`

This will display your public key. Copy the entire output.

**Step 3: Add SSH key to GitHub**
- Go to GitHub Settings → SSH and GPG keys
- Click "New SSH key"
- Paste your public key and save

**Step 4: Test SSH connection**

Run the command: `ssh -T git@github.com`

You should see a message: "Hi username! You've successfully authenticated, but GitHub does not provide shell access."

#### Why SSH Over HTTPS?

- **No repeated authentication**: No need to enter username/password for every push
- **More secure**: Uses cryptographic keys instead of passwords
- **Better for automation**: Works seamlessly with CI/CD pipelines
- **Industry standard**: Widely used in professional development

### Installation

**Step 1: Clone the repository using SSH**

Run the commands:
- `git clone git@github.com:PVRPratyusha/Github_Lab1.git`
- `cd Github_Lab1/Lab1`

**Step 2: Create and activate virtual environment**

For macOS/Linux, run the commands:
- `python3 -m venv github_lab1_env`
- `source github_lab1_env/bin/activate`

For Windows, run the commands:
- `python -m venv github_lab1_env`
- `github_lab1_env\Scripts\activate`

**Step 3: Install dependencies**

Run the command: `pip install -r requirements.txt`

## Running Tests

Run tests locally using pytest with the command: `pytest test/ -v`

Expected output: All 13 tests should pass.

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration. The workflow automatically:
- Runs on every push to main branch
- Sets up Python 3.9 environment
- Installs dependencies
- Executes all unit tests
- Reports test results

View workflow runs in the "Actions" tab on GitHub.

## Common Issues Encountered

### Issue 1: Invalid Python SDK in PyCharm
**Problem**: PyCharm showed "Invalid Python SDK" error when setting up virtual environment.

**Solution**: 
- Deleted corrupted virtual environment with command: `rm -rf github_lab1_env`
- Created fresh environment using terminal with command: `python3 -m venv github_lab1_env`
- Pointed PyCharm to the new interpreter at `github_lab1_env/bin/python`

### Issue 2: Git Push Rejected - Remote Contains Work
**Problem**: Push failed with "Updates were rejected because the remote contains work that you do not have locally."

**Solution**: 
- Pulled remote changes first with command: `git pull origin main --no-edit`
- Then pushed local changes with command: `git push origin main`
- This merged the workflow file created on GitHub with local changes

### Issue 3: Stuck in Vim Merge Editor
**Problem**: Git opened vim editor during merge, and commands weren't working.

**Solution**: 
- Used `:q!` to quit without saving
- Aborted merge with command: `git merge --abort`
- Configured Git to skip editor with command: `export GIT_EDITOR=true`
- Used `--no-edit` flag with command: `git pull origin main --no-edit`

### Issue 4: GitHub Actions Workflow Not Appearing
**Problem**: Workflow file existed but didn't appear in Actions tab.

**Solution**: 
- Ensured `.github/workflows/tests.yml` was in correct location (inside Lab1 folder)
- Created workflow file directly through GitHub UI
- Made a new commit to trigger the workflow

### Issue 5: Wrong Directory During Git Operations
**Problem**: Git commands behaving unexpectedly.

**Solution**: 
- Verified correct directory with command: `pwd`
- Navigated to Lab1 folder with command: `cd /Users/pvrpratyusha/Workspace/NEU/MLOps/Github_Lab1/Lab1`
- All Git commands must be run from repository root

## Development Workflow

1. Make changes to code
2. Run tests locally with command: `pytest test/ -v`
3. Commit changes with command: `git commit -m "description"`
4. Push to GitHub with command: `git push origin main`
5. GitHub Actions automatically runs tests
6. Check Actions tab for results

## Technologies Used

- **Python 3.9+**: Programming language
- **pytest**: Testing framework
- **GitHub Actions**: CI/CD automation
- **Git/GitHub**: Version control with SSH authentication
- **PyCharm**: IDE for development

## Testing

The project includes comprehensive unit tests covering:
- Normal operation cases
- Edge cases (zero, negative numbers)
- Error conditions (division by zero, negative square root)
- Floating-point precision using `pytest.approx`

Total: 13 tests across all calculator functions

## Author

PVRPratyusha

## License

This project is part of MLOps coursework at Northeastern University.

## Acknowledgments

- MLOps course materials from Northeastern University
- GitHub Actions documentation
- pytest documentation
