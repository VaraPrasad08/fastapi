from fastapi import FastAPI, File, UploadFile

import pandas as pd
import numpy as np

app = FastAPI()


@app.get("/files/")
def create_file():
    f = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
    return {"file_size": f}

@app.get("/files")
def create_file():
    rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
    ts = pd.Series(np.random.randn(len(rng)), rng)
    ts_utc = ts.tz_localize("UTC")
    return {"file_size": ts_utc}


@app.get("/")
def create_file():

    s = pd.Series(["A", "B", "C", "Aaba", "Baca",  "CABA", "dog", "cat"])
    a=s.str.lower()
    return {"file_size": a}

@app.get("/get")
def read():
    df = pd.DataFrame(np.random.randn(10, 4))
    return df


left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
a=pd.merge(left, right, on="key")
print (a)


prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")

ts = pd.Series(np.random.randn(len(prng)), prng)

ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9

print (ts.head())