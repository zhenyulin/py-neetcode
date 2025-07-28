from cython import boundscheck, wraparound
from libc.string cimport memset
from cpython.unicode cimport (
    PyUnicode_DATA,
    PyUnicode_GET_LENGTH,
    PyUnicode_KIND,
    PyUnicode_READ,
)
from cpython.bytes cimport PyBytes_FromStringAndSize

@boundscheck(False)
@wraparound(False)
cpdef list group_anagrams(list strs):
    """Group strings that contain only 'a'..'z'."""
    cdef:
        dict groups = {}
        str s
        unsigned char[26] counts # uint8_t = unsigned char (unicode)
        Py_ssize_t n, i # used by cython.unicode
        int kind
        const void* data
        unsigned int unicode
        const char* count_pointer
        bytes key
        list group

    for s in strs:
        memset(&counts[0], 0, 26)

        # avoid the boxing/unboxing of accessing python's object layer
        n, kind, data = PyUnicode_GET_LENGTH(s), PyUnicode_KIND(s), PyUnicode_DATA(s)

        for i in range(n):
            unicode = PyUnicode_READ(kind, data, i)
            counts[unicode - 97] += 1 # 'a' is 97 in unicode

        # Construct a 1-byte-per-char Unicode string from the counts
        count_pointer = <const char*>&counts[0] # convert an unsigned char* to a const char*
        key = PyBytes_FromStringAndSize(count_pointer, 26) # not passing that inline to avoid cython safety flag

        group = groups.get(key)
        if group is None:
            group = []
            groups[key] = group
        group.append(s)

    return list(groups.values())
