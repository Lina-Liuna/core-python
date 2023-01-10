# Simple example presenting how persistent ID can be used to pickle
# external objects by reference.

# "pickling" is the process whereby a Python object hierarchy is converted into a byte stream.
# "unpickling" is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
# pickling is alternatively known as "serizlization", "marshalling" or "flattening"

# The pickle module is not secure.
# Only unpickle data you trust.
# It is possible to construct malicious pickle data which will execute arbitrary code during unpickling
# Never unpickle data that could have come from an untrusted source
# Safer serialization formats such as json may be more appropriate if you are processing untrusted data.
# See Comparison with json.

# pickle VS marshal
# marshal is a more primitive serialization module
# pickle always be a preferred way to serialize python object
# marshal exists primarily to support python's .pyc files

# pickle module keeps track of the objects it has already serialized, so that later references to the same objects
# won't be serialized again.

# marshal cannot be used to serialize user-defined classes and their instances.
# pickle can save and restore class instances transparently

# the marshal serialization format is not guaranteed to be portable across python versions, because
# marshal primary job in life is to support .pyc files
# pickle serialization format is guaraanteed to be backwards compatible across python releases
# provides a compatible pickle protocol.


import pickle
import sqlite3
from collections import namedtuple

# Simple class representing a record in our database.
MemoRecord = namedtuple("MemoRecord", "key, task")

class DBPickler(pickle.Pickler):

    def persistent_id(self, obj):
        # Instead of pickling MemoRecord as a regular class instance, we emit a
        # persistent ID.
        if isinstance(obj, MemoRecord):
            # Here, our persistent ID is simply a tuple, containing a tag and a
            # key, which refers to a specific record in the database.
            return ("MemoRecord", obj.key)
        else:
            # If obj does not have a persistent ID, return None. This means obj
            # needs to be pickled as usual.
            return None


class DBUnpickler(pickle.Unpickler):

    def __init__(self, file, connection):
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):
        # This method is invoked whenever a persistent ID is encountered.
        # Here, pid is the tuple returned by DBPickler.
        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            # Fetch the referenced record from the database and return it.
            cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id),))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("unsupported persistent object")


def main():
    import io
    import pprint

    # Initialize and populate our database.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
    tasks = (
        'give food to fish',
        'prepare group meeting',
        'fight with a zebra',
        )
    for task in tasks:
        cursor.execute("INSERT INTO memos VALUES(NULL, ?)", (task,))

    # Fetch the records to be pickled.
    cursor.execute("SELECT * FROM memos")
    memos = [MemoRecord(key, task) for key, task in cursor]
    # Save the records using our custom DBPickler.
    file = io.BytesIO()
    DBPickler(file).dump(memos)

    print("Pickled records:")
    pprint.pprint(memos)

    # Update a record, just for good measure.
    cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

    # Load the records from the pickle data stream.
    file.seek(0)
    memos = DBUnpickler(file, conn).load()

    print("Unpickled records:")
    pprint.pprint(memos)


if __name__ == '__main__':
    main()