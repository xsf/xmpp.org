#!/usr/bin/env python3
import ast
import json
import sys
data_raw = "[" + sys.stdin.read() + "]"
data = ast.literal_eval(data_raw)
result = [
    {
        "name": name.strip(),
        "url": url.strip() if url else None,
        "info": [item.strip() for item in info.split("/")],
        "last_renewed": None,
    }
    for name, url, info in data
]
result.sort(key=lambda x: x["name"].casefold())
json.dump(result, sys.stdout, indent=4, sort_keys=True)
