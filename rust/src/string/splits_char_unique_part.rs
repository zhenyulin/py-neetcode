use pyo3::prelude::*;

#[pyfunction]
pub fn partition_lengths(s: &str) -> PyResult<Vec<i32>> {
    let mut last = [0usize; 26];

    for (i, b) in s.bytes().enumerate() {
        last[(b - b'a') as usize] = i;
    }

    let mut res = Vec::with_capacity(26);
    let (mut limit, mut length) = (0usize, 0usize);

    for (i, b) in s.bytes().enumerate() {
        limit = limit.max(last[(b - b'a') as usize]);
        length += 1;

        if i == limit {
            res.push(length as i32);
            length = 0;
        }
    }

    Ok(res)
}
