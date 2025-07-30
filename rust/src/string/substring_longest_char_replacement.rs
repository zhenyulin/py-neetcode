use pyo3::prelude::*;

#[pyfunction]
pub fn char_replacement(s: &str, k: i32) -> PyResult<i32> {
    let bytes = s.as_bytes();
    let mut count = [0usize; 26];
    let (mut left, mut res, mut max_same) = (0, 0, 0);

    for right in 0..bytes.len() {
        let j = (bytes[right] - b'A') as usize;
        count[j] += 1;

        max_same = max_same.max(count[j]);

        if (right - left + 1) - max_same > k as usize {
            let i = (bytes[left] - b'A') as usize;
            count[i] -= 1;
            left += 1;
        }

        res = res.max(right - left + 1);
    }

    Ok(res as i32)
}
