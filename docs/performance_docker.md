## Environment

- Docker with VirtualBox on Mac
  - CPUs: 2
  - Memory: 2048MB

## Tornado
```
vegeta report docs/performance_tests/tornado/connections-10000_rate-100_duration-60s.bin
Requests      [total, rate]            6000, 100.01
Duration      [total, attack, wait]    59.99443003s, 59.992858s, 1.57203ms
Latencies     [mean, 50, 95, 99, max]  1.718028ms, 1.618409ms, 2.227353ms, 3.378229ms, 13.740057ms
Bytes In      [total, mean]            351100, 58.52
Bytes Out     [total, mean]            558000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:6000
Error Set:

vegeta report docs/performance_tests/tornado/connections-10000_rate-200_duration-60s.bin
Requests      [total, rate]            12000, 200.01
Duration      [total, attack, wait]    59.999084905s, 59.997672s, 1.412905ms
Latencies     [mean, 50, 95, 99, max]  1.726478ms, 1.618958ms, 2.198532ms, 4.225907ms, 18.865149ms
Bytes In      [total, mean]            702113, 58.51
Bytes Out     [total, mean]            1116000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:12000
Error Set:

vegeta report docs/performance_tests/tornado/connections-10000_rate-500_duration-60s.bin
Requests      [total, rate]            30000, 500.00
Duration      [total, attack, wait]    1m0.166900633s, 1m0.000193s, 166.707633ms
Latencies     [mean, 50, 95, 99, max]  17.207731ms, 1.507886ms, 124.499757ms, 301.856966ms, 788.331592ms
Bytes In      [total, mean]            1755275, 58.51
Bytes Out     [total, mean]            2790000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:30000
Error Set:
```

## uWSGI
- Workers: 2
- max_requests: 1000000
```
vegeta report docs/performance_tests/uwsgi/connections-10000_rate-100_duration-60s.bin
Requests      [total, rate]            6000, 100.01
Duration      [total, attack, wait]    59.9961612s, 59.994031s, 2.1302ms
Latencies     [mean, 50, 95, 99, max]  2.361062ms, 2.21802ms, 3.072988ms, 5.372874ms, 16.880018ms
Bytes In      [total, mean]            339079, 56.51
Bytes Out     [total, mean]            557907, 92.98
Success       [ratio]                  99.98%
Status Codes  [code:count]             0:1  200:5999
Error Set:

vegeta report docs/performance_tests/uwsgi/connections-10000_rate-200_duration-60s.bin
Requests      [total, rate]            12000, 200.01
Duration      [total, attack, wait]    1m0.012748634s, 59.998083s, 14.665634ms
Latencies     [mean, 50, 95, 99, max]  2.432985ms, 2.165798ms, 3.513377ms, 9.738955ms, 25.075922ms
Bytes In      [total, mean]            670541, 55.88
Bytes Out     [total, mean]            1103631, 91.97
Success       [ratio]                  98.89%
Status Codes  [code:count]             0:133  200:11867
Error Set:
Post http://192.168.99.100:8080/v1/predict: EOF
Post http://192.168.99.100:8080/v1/predict: http: server closed idle connection

vegeta report docs/performance_tests/uwsgi/connections-10000_rate-500_duration-60s.bin
Requests      [total, rate]            30000, 500.00
Duration      [total, attack, wait]    1m0.002331626s, 59.999977s, 2.354626ms
Latencies     [mean, 50, 95, 99, max]  2.775126ms, 2.111957ms, 6.355212ms, 32.287921ms, 67.434734ms
Bytes In      [total, mean]            1203727, 40.12
Bytes Out     [total, mean]            1983225, 66.11
Success       [ratio]                  71.08%
Status Codes  [code:count]             0:8675  200:21325
Error Set:
Post http://192.168.99.100:8080/v1/predict: EOF
Post http://192.168.99.100:8080/v1/predict: http: server closed idle connection
```
