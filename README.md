# quickcli

## Installation steps

1. Clone the repository:

```bash
git clone https://github.com/dsirakov/quickdemo.git
```

2. Create virtual environment:

```bash
cd quickdemo

python -m venv .venv

source .venv/bin/activate
```

2. Install quickcli:

```bash
pip install .
```

## Usage

1. Export access tokens:

```bash
export GITHUB_TOKEN=<token-value>
export FRESHDESK_TOKEN=<token-value>
```

2. Run the tool:

```bash
quickcli <github-username> <freshdesk-subdomain>
```

## Run the tests

1. Install the dev dependencies:

```bash
pip install -r requirements-dev.txt
```

2. Run the tests:

```bash
python -m pytest tests -v
```
