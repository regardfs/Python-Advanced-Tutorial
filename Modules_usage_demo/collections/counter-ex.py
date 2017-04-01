#!/usr/bin/env python

from collections import Counter
# Tally occurrences of words in a list
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1


# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)


c = Counter('gallahad')
# Counter({'a': 3, 'd': 1, 'g': 1, 'h': 1, 'l': 2})



