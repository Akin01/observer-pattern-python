# Observer Pattern - Python

This is a simple code to implement observer pattern in python.

## Features

There is a file named `event_emitter.py` that contains several method to perform observer operation.

| Method           | Description                                                      |
|------------------|------------------------------------------------------------------|
| `register_event` | To register an event and with `namespace` and `handler`          |
| `remove_event`   | To unregister an event with `namespace` as an argument           |
| `dispatch_event` | To trigger an event that performing operation to `payload` given |

The class has an optional constructor to define default events to register before assigning several handlers to it.
Note that the class was singleton which give you same object when every class instantiated. You can see the example how to consume the class in `main.py` file.

