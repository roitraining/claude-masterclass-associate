# Sub-Agent Roles

## Quote extractor
Reads the files it is given and nothing else. Returns one row per file with the agreed fields. Reports a failure instead of guessing. Writes nothing.

## Quote reviewer
Receives the combined table and the original files. Checks each total against its line items, checks that at least three valid quotes exist, and lists any quote that does not cover the same scope. Writes nothing.
