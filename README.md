### UPRO
`UPRO` is a leveraged ETF that promises 3x daily returns
of `S&P 500`. Details: http://etf.com/UPRO, 
[fund's prospectus](https://www.proshares.com/funds/prospectus.html?ticker=UPRO).

### Non-purpose of this repository
Be of any financial advice. Don't buy `UPRO` if you cannot stomach 100% losses.
It can literally go to zero in a single day - from the fund's prospectus:

```
> For example, because the Fund includes a multiplier of three times
> (3x) the Index, a single day movement in the Index approaching 33%
> at any point in the day could result in the total loss of an
> investor’s investment if that movement is contrary to the investment
> objective of the Fund, even if the Index subsequently moves in
> an opposite direction, eliminating all or a portion of the earlier
> movement. 
```

### Purpose of this repository
See what has really happened to `UPRO` between June 2009
and April 2019 - how well it has been tracking it's target,
what's the deviation from the target and how can one predict
future deviation.

### UPRO's stated target
From the fund's prospectus:
```
> ProShares UltraPro S&P500 (the “Fund”) seeks daily investment
> results, before fees and expenses, that correspond to three times
> (3x) the return of the S&P 500® Index (the “Index”) for a single
> day, not for any other period. A “single day” is measured from the
> time the Fund calculates its net asset value (“NAV”) to the time of
> the Fund’s next NAV calculation.
```

As I understand the NAV is calculated after every trading day. To assess
the performance of `UPRO` I'll compare it to compounded 3x daily `SPY`
price changes, from previous closing price to next closing price.

### Handling of dividends
Dividends need to be included for `UPRO`, but also for `SPY` when constructing
the "ideal" daily 3x SPY benchmark. Otherwise the comparison is unfair,
it makes it look like `UPRO` delivers higher results than the "ideal", cost-free
and interest-rate-free daily 3x SPY benchmark:
#### TODO: insert a PNG with the chart. 
