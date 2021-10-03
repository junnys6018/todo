# A simple command line todo lister

Example useage
```
$ python list_todo.py
  [today] buy groceries
  - get bread, tomatoes and new pan
  [today] top up car
  [uni]   math assignment
```

Example todo.json 
```
[
    {
        "title": "buy groceries",
        "message": "get bread, tomatoes and new pan",
        "tag": "[today]",
        "priority": "med"
    },
    {
        "title": "top up car",
        "message": "",
        "tag": "[today]",
        "priority": "low"
    },
    {
        "title": "math assignment",
        "message": "",
        "tag": "[uni]",
        "priority": "high"
    }
]
```