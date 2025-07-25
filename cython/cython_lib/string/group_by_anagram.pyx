import cython
from cpython.unicode cimport (
    PyUnicode_READ, PyUnicode_KIND, PyUnicode_DATA, PyUnicode_GET_LENGTH
)

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef list group_anagrams_26lower(list strs):
    """Group strings that contain only 'a'..'z'."""
    cdef dict groups = {}
    cdef int[26] counts
    cdef Py_ssize_t i, n
    cdef str s
    cdef int kind
    cdef const void* data
    cdef unsigned int ch
    cdef list lst
    cdef int j
    cdef tuple key

    for s in strs:
        for j in range(26):
            counts[j] = 0

        n = PyUnicode_GET_LENGTH(s)
        kind = PyUnicode_KIND(s)
        data = PyUnicode_DATA(s)

        for i in range(n):
            ch = PyUnicode_READ(kind, data, i)
            ch -= 97  # 'a'
            if ch >= 26:  # also guards negative underflow
                raise ValueError("Only lowercase ASCII a-z supported")
            counts[ch] += 1

        # No generator expressions inside cpdef
        key = (
            counts[0], counts[1], counts[2], counts[3], counts[4], counts[5],
            counts[6], counts[7], counts[8], counts[9], counts[10], counts[11],
            counts[12], counts[13], counts[14], counts[15], counts[16], counts[17],
            counts[18], counts[19], counts[20], counts[21], counts[22], counts[23],
            counts[24], counts[25]
        )

        lst = groups.get(key)
        if lst is None:
            lst = []
            groups[key] = lst
        lst.append(s)

    return list(groups.values())
