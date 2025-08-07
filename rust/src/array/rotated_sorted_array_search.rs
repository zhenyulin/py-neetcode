use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
pub fn search<'py>(_py: Python<'py>, nums: Bound<'py, PyList>, target: i32) -> PyResult<i32> {
    let (mut l, mut r) = (0usize, nums.len() - 1);

    while l <= r {
        let m = (l + r) / 2; // usize division would floor
        let mid = nums.get_item(m)?.extract::<i32>()?;

        if mid == target {
            return Ok(m as i32);
        }

        let left = nums.get_item(l)?.extract::<i32>()?;

        // left part is sorted
        if left <= mid {
            if left <= target && target < mid {
                r = m - 1;
            } else {
                l = m + 1;
            }
        } else {
            // right part is sorted
            let right = nums.get_item(r)?.extract::<i32>()?;
            if mid < target && target <= right {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
    }

    Ok(-1)
}
