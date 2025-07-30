use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
pub fn length_of_longest_substring(s: &str) -> PyResult<i32> {
    let mut seen: HashMap<char, usize> = HashMap::new();
    let (mut res, mut i) = (0, 0);

    for (j, c) in s.chars().enumerate() {
        if let Some(&last) = seen.get(&c)
            && last >= i
        {
            i = last + 1;
        } else {
            res = res.max(j - i + 1);
        }
        seen.insert(c, j);
    }
    Ok(res as i32)
}
