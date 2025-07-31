use pyo3::prelude::*;

// s.len() >= 1, so ranges.len() >= 2
const NULL: usize = usize::MAX;

#[pyfunction]
pub fn num_splits(s: &str) -> PyResult<i32> {
    let (mut first, mut last) = ([NULL; 26], [0; 26]);

    for (index, b) in s.bytes().enumerate() {
        let i = (b - b'a') as usize;
        if first[i] == NULL {
            first[i] = index;
        }
        last[i] = index;
    }

    let mut ranges = Vec::with_capacity(2 * 26);
    for j in 0..26 {
        if first[j] != NULL {
            ranges.push(first[j]);
            ranges.push(last[j]);
        }
    }

    ranges.sort_unstable();
    let mid = ranges.len() / 2;
    Ok((ranges[mid] - ranges[mid - 1]) as i32)
}
