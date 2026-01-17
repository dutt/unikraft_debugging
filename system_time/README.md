# Unikraft Wall Clock Issue

## Problem

`time.time()` returns 946598400 (December 31st, 1999) instead of current time.

## Expected Output
```
time.time() = 1736280000
datetime    = 2025-01-07 18:00:00
monotonic   = 0.001234
```

## Actual Output
```
time.time() = 946598400.1024494
datetime    = 1999-12-31 00:00:00.102449
monotonic   = 0.203227443
```

## Impact

- TLS certificate validation fails ("not yet valid")
- JWT token expiration broken
- Log timestamps wrong

## Reproduce

```bash
kraft run --plat fc --arch x86_64 -M 512Mi
```
