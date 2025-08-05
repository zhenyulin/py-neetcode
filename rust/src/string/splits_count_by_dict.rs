use pyo3::prelude::*;

// 1 <= s.len() <= 100

#[pyfunction]
pub fn ways_of_decoding(s: &str) -> PyResult<i32> {
    if &s[0..1] == "0" {
        return Ok(0);
    }

    let n = s.len();
    let (mut prev, mut last) = (1, 1);

    for i in 1..n {
        let mut current = 0;

        if &s[i..i + 1] != "0" {
            current += last;
        }

        let two = &s[i - 1..i + 1];
        if ("10"..="26").contains(&two) {
            current += prev;
        }

        (prev, last) = (last, current);
    }

    Ok(last)
}
