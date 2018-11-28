## Environment

- Docker with VirtualBox on Mac
  - CPUs: 2
  - Memory: 2048MB

## Tornado
```
vegeta attack -rate=1 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt  | vegeta report
Requests      [total, rate]            30, 1.03
Duration      [total, attack, wait]    29.004142157s, 29.002108s, 2.034157ms
Latencies     [mean, 50, 95, 99, max]  2.086642ms, 1.927738ms, 3.860109ms, 4.083394ms, 4.083394ms
Bytes In      [total, mean]            1746, 58.20
Bytes Out     [total, mean]            2790, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:30

vegeta attack -rate=10 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt  | vegeta report
Requests      [total, rate]            300, 10.03
Duration      [total, attack, wait]    29.903338851s, 29.901723s, 1.615851ms
Latencies     [mean, 50, 95, 99, max]  1.897443ms, 1.80096ms, 2.614129ms, 3.516101ms, 4.471384ms
Bytes In      [total, mean]            17546, 58.49
Bytes Out     [total, mean]            27900, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:300

vegeta attack -rate=100 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt  | vegeta report
Requests      [total, rate]            3000, 100.02
Duration      [total, attack, wait]    29.994395327s, 29.99273s, 1.665327ms
Latencies     [mean, 50, 95, 99, max]  1.828685ms, 1.734405ms, 2.37063ms, 3.129067ms, 11.410814ms
Bytes In      [total, mean]            175493, 58.50
Bytes Out     [total, mean]            279000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:3000

vegeta attack -rate=200 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt  | vegeta report
Requests      [total, rate]            6000, 200.03
Duration      [total, attack, wait]    29.997880914s, 29.995952s, 1.928914ms
Latencies     [mean, 50, 95, 99, max]  1.807301ms, 1.68855ms, 2.304118ms, 3.952279ms, 13.551514ms
Bytes In      [total, mean]            351050, 58.51
Bytes Out     [total, mean]            558000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:6000

vegeta attack -rate=500 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt  | vegeta report
Requests      [total, rate]            15000, 500.01
Duration      [total, attack, wait]    30.001395992s, 29.999424s, 1.971992ms
Latencies     [mean, 50, 95, 99, max]  4.038657ms, 1.661907ms, 16.909197ms, 41.32897ms, 150.487838ms
Bytes In      [total, mean]            877292, 58.49
Bytes Out     [total, mean]            1395000, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:15000

vegeta attack -rate=1000 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt  | vegeta report
Requests      [total, rate]            30000, 1000.00
Duration      [total, attack, wait]    39.082603025s, 30.000118s, 9.082485025s
Latencies     [mean, 50, 95, 99, max]  2.193429633s, 37.887125ms, 6.178168548s, 27.998390323s, 30.672134273s
Bytes In      [total, mean]            873755, 29.13
Bytes Out     [total, mean]            1391280, 46.38
Success       [ratio]                  49.87%
Status Codes  [code:count]             0:15040  200:14960
```


## uWSGI
```
vegeta attack -rate=1 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt | vegeta report
Requests      [total, rate]            300, 10.03
Duration      [total, attack, wait]    29.907040422s, 29.904713s, 2.327422ms
Latencies     [mean, 50, 95, 99, max]  18.806405ms, 2.490402ms, 3.906145ms, 684.125646ms, 931.440798ms
Bytes In      [total, mean]            16936, 56.45
Bytes Out     [total, mean]            27900, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:300

vegeta attack -rate=10 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt | vegeta report
Requests      [total, rate]            300, 10.03
Duration      [total, attack, wait]    29.909152824s, 29.906657s, 2.495824ms
Latencies     [mean, 50, 95, 99, max]  19.746326ms, 2.489848ms, 4.738031ms, 710.990834ms, 956.71541ms
Bytes In      [total, mean]            16926, 56.42
Bytes Out     [total, mean]            27900, 93.00
Success       [ratio]                  100.00%
Status Codes  [code:count]             200:300

vegeta attack -rate=100 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt | vegeta report
Requests      [total, rate]            3000, 100.03
Duration      [total, attack, wait]    29.993963647s, 29.991128s, 2.835647ms
Latencies     [mean, 50, 95, 99, max]  23.259968ms, 2.474543ms, 9.441168ms, 761.858484ms, 1.006375068s
Bytes In      [total, mean]            167686, 55.90
Bytes Out     [total, mean]            276396, 92.13
Success       [ratio]                  99.07%
Status Codes  [code:count]             0:28  200:2972

vegeta attack -rate=200 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt | vegeta report
Requests      [total, rate]            6000, 200.02
Duration      [total, attack, wait]    29.998467861s, 29.996261s, 2.206861ms
Latencies     [mean, 50, 95, 99, max]  29.328119ms, 2.392093ms, 25.937609ms, 910.62678ms, 1.012839538s
Bytes In      [total, mean]            320315, 53.39
Bytes Out     [total, mean]            527868, 87.98
Success       [ratio]                  94.60%
Status Codes  [code:count]             0:324  200:5676

vegeta attack -rate=500 -duration=30s -body=./resources/test-body.json -targets=./resources/vegeta-target.txt | vegeta report
Requests      [total, rate]            15000, 499.87
Duration      [total, attack, wait]    57.127278866s, 30.007829s, 27.119449866s
Latencies     [mean, 50, 95, 99, max]  646.793683ms, 12.953078ms, 3.057501821s, 7.648019851s, 28.326067866s
Bytes In      [total, mean]            452040, 30.14
Bytes Out     [total, mean]            746604, 49.77
Success       [ratio]                  53.52%
Status Codes  [code:count]             0:6972  200:8028
```
