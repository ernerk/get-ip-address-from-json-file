# Get ip address from json file

Each JSON object appears as a dict or list, and these are separated by commas, usually located within an array ([]) or a dict ({}).

For example:

`[
  {"ip": "192.168.1.1", "other_data": "..."},
  {"ip": "192.168.1.2", "other_data": "..."}
]`

or

`{
  "first": {"ip": "192.168.1.1", "other_data": "..."},
  "second": {"ip": "192.168.1.2", "other_data": "..."}
}`

But sometimes JSON files might be formatted like this, which could lead to the error you're encountering:

`{"ip": "192.168.1.1", "other_data": "..."}
{"ip": "192.168.1.2", "other_data": "..."}`

If your JSON file is formatted like the last case, you could use the following code snippet. This snippet reads the file line by line, treating each line as a separate JSON object.
