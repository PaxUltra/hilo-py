![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/PaxUltra/hilo-py/ci.yml)

# hilo-py
Python CLI hi-lo game.

## Requirements
- Python 3.6+

## Installation

1. Clone the repository wherever you want it to live
```bash
git clone https://github.com/PaxUltra/hilo-py.git
```
2. Change directory into the `hilo-py` directory
```bash
cd hilo-py
```

## Usage

The script accepts no arguments. The user is prompted for all necessary inputs.

```bash
python hilo.py
```
Output is printed directly to the terminal.

### Testing

To run the provided tests, execute:
```bash
python -m unittest test_hilo.py
```

This project was built for the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) project on roadmap.sh.