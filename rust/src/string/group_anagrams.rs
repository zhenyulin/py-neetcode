use ahash::RandomState;
use hashbrown::HashMap; // uncomment if you add hashbrown + ahash
use pyo3::prelude::*;
use pyo3::types::{PyList, PyString};
// use std::collections::HashMap;

type Key = [u16; 26];

#[pyfunction]
pub fn group_anagrams<'py>(py: Python<'py>, strs: Bound<'py, PyList>) -> PyResult<Py<PyList>> {
    // With std HashMap (SipHash) – slower but no extra deps:
    // let mut groups: HashMap<Key, Vec<Py<PyString>>> = HashMap::with_capacity(strs.len());

    // If you prefer speed:
    let mut groups: HashMap<Key, Vec<Py<PyString>>, RandomState> =
        HashMap::with_hasher(RandomState::new());
    groups.reserve(strs.len());

    let n = strs.len();
    for i in 0..n {
        let any = strs.get_item(i)?;
        let pystr: Bound<'py, PyString> = any.downcast_into()?;
        let s = pystr.to_str()?; // &str, no copy
        let mut key: Key = [0; 26];

        // ASCII lowercase-only fast path
        for &b in s.as_bytes() {
            let idx = b.wrapping_sub(b'a') as usize;
            if idx >= 26 {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    "Only lowercase ASCII a-z supported",
                ));
            }
            key[idx] += 1;
        }

        groups.entry(key).or_default().push(pystr.into_py(py));
    }

    // Build Python list[list[str]]
    let out = PyList::empty_bound(py);
    for vals in groups.into_values() {
        let inner = PyList::new_bound(py, &vals);
        out.append(inner)?;
    }
    Ok(out.into())
}
