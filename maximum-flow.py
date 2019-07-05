from process.process import Maximum

rout = [
    {
        "from": "A",
        "to": "B",
        "value": 10
    },
    {
        "from": "A",
        "to": "C",
        "value": 10
    },
    {
        "from": "B",
        "to": "R",
        "value": 7
    },
    {
        "from": "B",
        "to": "L", 
        "value": 12
    },
    {
        "from": "C",
        "to": "L",
        "value": 6
    },
    {
        "from": "L",
        "to": "C",
        "value": 4
    },
    {
        "from": "C",
        "to": "X",
        "value": 3
    },
    {
        "from": "X",
        "to": "F",
        "value": 4
    },
    {
        "from": "F",
        "to": "L",
        "value": 1
    },
    {
        "from": "L",
        "to": "F",
        "value": 1
    },
    {
        "from": "F",
        "to": "Z",
        "value": 3
    },
    {
        "from": "L",
        "to": "R",
        "value": 5
    },
    {
        "from": "L",
        "to": "Z",
        "value": 6
    },
    {
        "from": "R",
        "to": "P",
        "value": 10
    },
    {
        "from": "Z",
        "to": "P",
        "value": 10
    }
]

if __name__ == "__main__":
    Maximum(rout, "A", "P").resolve()