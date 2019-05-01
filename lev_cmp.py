#!/usr/bin/env python

import csv


def get_security_csv_data(fname):
    rows = []
    with open(fname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    rows.sort(key=lambda row: row["Date"])

    return rows


def get_spy_rows():
    return get_security_csv_data("SPY.csv")


def get_upro_rows():
    return get_security_csv_data("UPRO.csv")


import pdb
pdb.set_trace()
