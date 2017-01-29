# translate python file/object to json type file/object
# json.dumps/json.loads
import json
l = [0, 1, 2, 'x', 'y', {'a': 1, 'b': None}]
# '[0, 1, 2, "x", "y", {"a": 1, "b": null}]'
json.dumps(l)
# redefine separators
# '[0, 1, 2, "x", "y", {"a": 1, "b": null}]'
json.dumps(l, separators=[',', ':'])
# sort keys
# '[0, 1, 2, "x", "y", {"a": 1, "b": null}]'
json.dumps(l, sort_keys=True)
j = '[0, 1, 2, "x", "y", {"a": 1, "b": null}]'
# transfer json to python type
# [0, 1, 2, u'x', u'y', {u'a': 1, u'b': None}]
json.loads('[0, 1, 2, "x", "y", {"a": 1, "b": null}]')
