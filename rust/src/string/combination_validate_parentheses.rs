use pyo3::prelude::*;

#[pyfunction]
pub fn validate_parenthesis(s: &str) -> PyResult<bool> {
    let mut left_min: i32 = 0;
    let mut left_max: i32 = 0;

    for ch in s.chars() {
        match ch {
            '(' => {
                left_min += 1;
                left_max += 1;
            }
            ')' => {
                left_min -= 1;
                left_max -= 1;
            }
            '*' => {
                left_min -= 1;
                left_max += 1;
            }
            _ => {}
        }

        if left_max < 0 {
            return Ok(false);
        }
        if left_min < 0 {
            left_min = 0;
        }
    }

    Ok(left_min == 0)
}
