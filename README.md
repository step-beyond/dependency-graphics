# Dependency Graphics

# Run locally

1. Create virtual env:
```commandline
python -m venv venv
```
2. Activate virtual env:
```commandline
source ./venv/bin/activate (Linux, macOS) or ./venv/Scripts/activate (Win)
```
3. Create `.dependency-graphics-rc.yaml` from where you execute main.py
```yaml
directory: <path-to-your-code>
show-graph: True
```
4. Execute `main.py`
```commandline
python3 main.py
```
