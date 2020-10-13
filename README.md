# PyCurb

Library for working with street parking data using the [CurbLR data standard](https://github.com/sharedstreets/curblr).

## Installation

PyCurb is currently in development and must be installed locally.

## Documentation

PyCurb Key Features:

- Read and write CurbLR JSON data
- Construct new CurbLR Features in code
- Construct valid CurbLR time rules

### Reading CurbLR Data

We can read a CurbLR geojson feature collection from a file with:

```python
import pycurb
features = pycurb.FeatureCollection.from_file("path/to/curblr.json")
```

We can construct objects that extend `pycurb.PyCurbObject` from a Python dict with the `from_dict` method:

```python
import pycurb
time_span_dict = {"timesOfDay": [{"from": "08:00", "to": "18:00"}]}
time_span = pycurb.TimeSpan.from_dict(time_span_dict)
```

### Writing CurbLR Data

We can write a CurbLR geojson feature collection to a json file:

```python
import pycurb
features = pycurb.FeatureCollection()
features.save("./path/to/curblr.json", add_timestamp=True)
```

We can write objects that extends `pycurb.PyCurbObject` to a Python dict with the `to_dict` method:

```python
import pycurb
time_of_day = pycurb.time_rule.TimeOfDay("12", "14")
time_of_day.to_dict()
```

## Developing

Install all dependencies in `requirements-dev.txt`:

If necessary, create an isolated Python development environment with [venv](https://docs.python.org/3/library/venv.html) or [Docker](https://hub.docker.com/_/python).

```shell
pip install -r requirements-dev.txt
```

### Unit Tests and Code Quality

To run the unit test suite and code quality checks:

```shell
./scripts/test
```

These checks are run in CI on the `master` branch and for all pull requests.

`pycurb` uses the following development libraries:

- `unittest` for testing
- `coverage` for code coverage reports
- `flake8` for linting
- `yapf` for auto formatting
