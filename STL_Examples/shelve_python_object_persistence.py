# A shelf is a persistent, dictionary-like object.
# The difference with dbm databases is that the values in a shelf can be essentially arbitrary python objects
# anything that the pickle module can handle.
# the keys are ordinary strings

# Note and warnings and restrictions

# Don't rely on the shelf being closed automatically, always call close() explicitly
# or use shelve.open() as a context manager with shelve.open() as db:

# because the shelve module is backed by pickle, it is insecure to loadd a shelf from an untrusted source.
# Like with pickle, loading a shelf can execute arbitrary code.
# Persistent dictionary recipe(https://code.activestate.com/recipes/576642/)
# persistent dictionary recipe with widely supported storage formats and having the speed of native dictionaries

# The choice of which database package will be used (as dbm.ndbm or dbm.gnu) depend on which interface is available
# Therefore it is not safe to open the database directly using dbm.
# The database is also (unfortunately) subject to the limitations of dbm, if it is used —
# this means that (the pickled representation of) the objects stored in the database should be fairly small,
# and in rare cases key collisions may cause the database to refuse updates.

# The shelve module does not support concurrent read/write access to shelved objects. lock/unlock


