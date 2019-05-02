#!/usr/bin/env python

import csv


def get_security_csv_data(security):
    # Get dividend data
    dividends = dict()
    with open("inputs/%s_dividends.csv" % security) as f:
       reader = csv.DictReader(f)
       for row in reader:
           date = row["Date"]
           div = row["Dividends"]
           dividends[date] = div 

    # Get basic price data, merge with dividends
    rows = []
    with open("inputs/%s.csv" % security) as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row["Date"]
            if date in dividends:
                row["Dividends"] = dividends[date]
            assert "Close" in row
            rows.append(row)

    rows.sort(key=lambda row: row["Date"])

    return rows


def get_spy_rows():
    return get_security_csv_data("SPY")


def get_upro_rows():
    return get_security_csv_data("UPRO")


def gain(current, prev):
    return float(current) / float(prev)


def percentage_from_gain(gain):
    return 100.0 * (gain - 1.0)


def gain_from_percentage(percentage):
    return (percentage / 100.0) + 1.0


spy_rows = get_spy_rows()
upro_rows = get_upro_rows()

spy_rownum = 0
upro_rownum = 0
streams_synced_for = 0
cumulative_spy = 1.0
cumulative_upro = 1.0
cumulative_spy3x = 1.0

print ("Date,SPY_daily_pcent_gain,UPRO_daily_pcent_gain,SPY3X_daily_pcent_gain,"
       "SPY_cumulative_gain,UPRO_cumulative_gain,SPY3X_cumulative_gain,"
       "UPRO_over_SPY3X_cumulative")

while spy_rownum < len(spy_rows) and upro_rownum < len(upro_rows):
    spy_row = spy_rows[spy_rownum]
    upro_row = upro_rows[upro_rownum]

    # Streams are not synced
    if spy_row["Date"] < upro_row["Date"]:
        streams_synced_for = 0
        spy_rownum += 1
        continue
    if spy_row["Date"] > upro_row["Date"]:
        streams_synced_for = 0
        upro_row += 1
        continue

    # Streams are synced.

    if streams_synced_for >= 1:
        prev_spy_price = spy_rows[spy_rownum - 1]["Close"]
        prev_upro_price = upro_rows[upro_rownum - 1]["Close"]
        spy_price = float(spy_row["Close"])
        upro_price = float(upro_row["Close"])

        # Correct for dividends, but only if we've just received it.
        # Further rows will go without dividend as we're only aggregating
        # daily multiplicative changes. This has the effect of always keeping
        # the dividend re-invested.
        if "Dividends" in spy_row:
            spy_price += float(spy_row["Dividends"])
        if "Dividends" in upro_row:
            upro_price += float(upro_row["Dividends"])

        spy_gain = gain(spy_price, prev_spy_price)
        upro_gain = gain(upro_price, prev_upro_price)
        spy_pcent = percentage_from_gain(spy_gain)
        upro_pcent = percentage_from_gain(upro_gain)
        spy3x_pcent = spy_pcent * 3.0
        spy3x_gain = gain_from_percentage(spy3x_pcent)
        cumulative_spy *= spy_gain
        cumulative_upro *= upro_gain
        cumulative_spy3x *= spy3x_gain
        cumulative_upro_vs_spy3x = cumulative_upro / cumulative_spy3x

        print "%s,%f,%f,%f,%f,%f,%f,%f" % (
            spy_row["Date"], spy_pcent, upro_pcent, spy3x_pcent,
            cumulative_spy, cumulative_upro, cumulative_spy3x,
            cumulative_upro_vs_spy3x)

    spy_rownum += 1
    upro_rownum += 1
    streams_synced_for += 1

