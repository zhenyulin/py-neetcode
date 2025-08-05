use pyo3::prelude::*;

#[pyfunction]
pub fn num_match_subsequences(s: &str, t: &str) -> PyResult<i32> {
    let (_s, _t) = (s.as_bytes(), t.as_bytes());
    let m: usize = _t.len();

    let mut count = vec![0; m + 1];
    count[0] = 1;

    for &char_s in _s {
        for (j, &char_t) in _t.iter().enumerate().rev() {
            if char_s == char_t {
                count[j + 1] += count[j];
            }
        }
    }

    Ok(count[m])
}
