use ahash::AHashMap;
use pyo3::prelude::*;
use pyo3::types::{PyList, PyString};

type Key = [u8; 26]; // strs[i].length < 255

#[pyfunction]
pub fn group_anagrams<'py>(py: Python<'py>, strs: Bound<'py, PyList>) -> PyResult<Py<PyList>> {
    let mut groups: AHashMap<Key, Vec<Py<PyString>>> = AHashMap::with_capacity(strs.len());

    for py_item in strs.iter() {
        let py_s = py_item.downcast()?;
        let s = py_s.to_str()?; // borrowed view to the string utf8 value in python heap
        let mut key: Key = [0; 26];

        for &b in s.as_bytes() {
            key[(b - b'a') as usize] += 1;
        }

        // convert borrowed &PyString to an owned smart pointer Py<PyString>
        let owned = py_s.into_pyobject(py)?;
        groups.entry(key).or_default().push(owned.into());
    }

    // creating the output list in python heap
    let output = PyList::empty(py);
    for vals in groups.into_values() {
        let py_group = PyList::new(py, &vals)?;
        output.append(py_group)?;
    }
    // convert the borrowed GIL-bound PyList into an owned Py<PyList> and end lifetime
    Ok(output.into())
}
