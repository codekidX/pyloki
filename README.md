PyLoki
------

A scalable instance associated module for logging and querying(alpha) in Grafana Loki


## Get Started

```bash
pip install pyloki
```

```bash
from pyloki import PyLoki

auth_loki = PyLoki(source='Authentication Service', job='auth.service')
auth_loki.warn('This module is warning me of something')
```

### Configurable Instance Options

- host: Host of your Loki instance `default: localhost`
- port: Port if needed `default: 3100`
- If secured:
	- username
	- password
- protocol: Protocol to follow `default: http`
- src_host: Host from which the logs are being streamed


### Functions

```python
set_tz(zone='Asia/Kolkata')
```

Sets your timezone for the log stream

```python
set_header(key, value)
```

Sets additional http headers to logs


## Contributing

- Create a python3 virtualenv 
```bash
python3 -m venv venv
```

- Install requirements
```bash
pip install -r requirements.txt
```

- **Before submitting** Run the tests. New tests for your PRs are most appreciated.
```bash
python -m pyloki.loki_test
```

## Versions

> ### 0.2.1
- Add `error` method on PyLoki
- Add `custom` method to pass your own label on PyLoki

> ### 0.2.0
- Proper implementation of logger
- Add Testsfor logging
- Add alpha client for querying the logs

> ### 0.1.0
- Alpha with barely working code

### License

MIT