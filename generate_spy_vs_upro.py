#!/usr/bin/env python

import csv


def get_security_csv_data(fname):
    rows = []
    with open(fname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            assert "Date" in row
            assert "Close" in row
            rows.append(row)

    rows.sort(key=lambda row: row["Date"])

    return rows


def get_spy_rows():
    return get_security_csv_data("SPY.csv")


def get_upro_rows():
    return get_security_csv_data("UPRO.csv")


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
cumulative_ideal_upro = 1.0

print ("Date,SPY_pcent_gain,UPRO_pcent_gain,ideal_UPRO_pcent_gain,"
       "SPY_cumulative_gain,UPRO_cumulative_gain,ideal_UPRO_cumulative_gain")

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
        prev_spy_row = spy_rows[spy_rownum - 1]
        prev_upro_row = upro_rows[upro_rownum - 1]
        spy_gain = gain(spy_row["Close"], prev_spy_row["Close"])
        upro_gain = gain(upro_row["Close"], prev_upro_row["Close"])
        spy_pcent = percentage_from_gain(spy_gain)
        upro_pcent = percentage_from_gain(upro_gain)
        ideal_upro_pcent = spy_pcent * 3.0
        ideal_upro_gain = gain_from_percentage(ideal_upro_pcent)
        cumulative_spy *= spy_gain
        cumulative_upro *= upro_gain
        cumulative_ideal_upro *= ideal_upro_gain

        print "%s,%f,%f,%f,%f,%f,%f" % (
            spy_row["Date"], spy_pcent, upro_pcent, ideal_upro_pcent,
            cumulative_spy, cumulative_upro, cumulative_ideal_upro)

    spy_rownum += 1
    upro_rownum += 1
    streams_synced_for += 1

