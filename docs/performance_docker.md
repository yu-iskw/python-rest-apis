# Performance Comparison

## Environment

- Docker with VirtualBox on Mac
  - CPUs: 2
  - Memory: 2048MB


## Tornado
The performance looks good.
Even when the number of requests per second is 500, there was no request error.
However, the latency with heavy requests, such as 200 and 500 got worse.
```
vegeta report docs/performance_tests/tornado/connections-10000_rate-10_duration-60s.bin
Requests      [total, rate]            600, 10.02
Duration      [total, attack, wait]    59.906787379s, 59.9043s, 2.487379ms
Latencies     [mean, 50, 95, 99, max]  1.828749ms, 1.632391ms, 2.629051ms, 4.043117ms, 6.89461ms
Bytes In      [total, mean]            35074, 58.46
Bytes Out     [total, mean]            55800, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:600
Error Set:

vegeta report docs/performance_tests/tornado/connections-10000_rate-100_duration-60s.bin
Requests      [total, rate]            6000, 100.01
Duration      [total, attack, wait]    59.994474682s, 59.992756s, 1.718682ms
Latencies     [mean, 50, 95, 99, max]  1.944571ms, 1.679781ms, 3.141051ms, 5.54105ms, 16.418344ms
Bytes In      [total, mean]            350829, 58.47
Bytes Out     [total, mean]            558000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:6000
Error Set:

vegeta report docs/performance_tests/tornado/connections-10000_rate-200_duration-60s.bin
Requests      [total, rate]            12000, 200.01
Duration      [total, attack, wait]    59.999445856s, 59.997849s, 1.596856ms
Latencies     [mean, 50, 95, 99, max]  2.532286ms, 1.813773ms, 4.899022ms, 13.891933ms, 132.293263ms
Bytes In      [total, mean]            701373, 58.45
Bytes Out     [total, mean]            1116000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:12000
Error Set:

vegeta report docs/performance_tests/tornado/connections-10000_rate-500_duration-60s.bin
Requests      [total, rate]            30000, 500.00
Duration      [total, attack, wait]    1m0.034729725s, 1m0.000241s, 34.488725ms
Latencies     [mean, 50, 95, 99, max]  15.124922ms, 2.981665ms, 68.108087ms, 166.009562ms, 418.70105ms
Bytes In      [total, mean]            1755235, 58.51
Bytes Out     [total, mean]            2790000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:30000
Error Set:
```

## uWSGI
- Workers: 2
- Max Requests to restart worker: 1000000
The performance is quite bad, especially when the number of requests is high.
Even when the number of requests per second is 100, there were 21 request error.
Moreover, the success ratio with 500 requests/sec is just 59.92%.
```
vegeta report docs/performance_tests/uwsgi/connections-10000_rate-10_duration-60s.bin
Requests      [total, rate]            600, 10.02
Duration      [total, attack, wait]    59.908318275s, 59.90622s, 2.098275ms
Latencies     [mean, 50, 95, 99, max]  2.59435ms, 2.210323ms, 3.173889ms, 7.229488ms, 101.154957ms
Bytes In      [total, mean]            33907, 56.51
Bytes Out     [total, mean]            55800, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:600
Error Set:

vegeta report docs/performance_tests/uwsgi/connections-10000_rate-100_duration-60s.bin
Requests      [total, rate]            6000, 100.01
Duration      [total, attack, wait]    59.994736705s, 59.992588s, 2.148705ms
Latencies     [mean, 50, 95, 99, max]  3.089328ms, 2.9952ms, 4.249686ms, 8.648625ms, 40.512811ms
Bytes In      [total, mean]            337620, 56.27
Bytes Out     [total, mean]            556047, 92.67
Success       [ratio]                  99.65%
Status Codes  [code:count]             0:21  200:5979
Error Set:

vegeta report docs/performance_tests/uwsgi/connections-10000_rate-200_duration-60s.bin
Requests      [total, rate]            12000, 200.01
Duration      [total, attack, wait]    59.999453143s, 59.997282s, 2.171143ms
Latencies     [mean, 50, 95, 99, max]  3.175319ms, 2.360318ms, 7.224099ms, 18.661882ms, 59.256829ms
Bytes In      [total, mean]            657614, 54.80
Bytes Out     [total, mean]            1083450, 90.29
Success       [ratio]                  97.08%
Status Codes  [code:count]             0:350  200:11650
Error Set:

vegeta report docs/performance_tests/uwsgi/connections-10000_rate-500_duration-60s.bin
Requests      [total, rate]            30000, 500.00
Duration      [total, attack, wait]    1m28.565415184s, 1m0.000059s, 28.565356184s
Latencies     [mean, 50, 95, 99, max]  336.064636ms, 109.484804ms, 1.142374372s, 4.838128038s, 29.577282828s
Bytes In      [total, mean]            1014252, 33.81
Bytes Out     [total, mean]            1671675, 55.72
Success       [ratio]                  59.92%
Status Codes  [code:count]             0:12025  200:17975
Error Set:
```
