PyLoki
------

A scalable instance associated module for logging in Grafana Loki


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

- `host`: Host of your Loki instance `default: localhost`
- `port`: Port if needed `default: 3100`
- If secured:
	- `username`
	- `password`
- `protocol`: Protocol to follow `default: http`
- `src_host`: Host from which the logs are being streamed


### Functions

```python
set_tz(zone='Asia/Kolkata')
```

Sets your timezone for the log stream

```python
set_header(key, value)
```

Sets additional http headers to logs


### License

MIT