use pyo3::prelude::*;
use pyo3::types::PyList;

#[pyfunction]
pub fn range_addition<'py>(
    _py: Python<'py>,
    length: usize,
    operations: Bound<'py, PyList>,
) -> PyResult<Vec<i32>> {
    if length == 0 {
        return Ok(Vec::new());
    };

    let mut res = vec![0; length + 1];

    for op in operations.iter() {
        let [i, j, v]: [i32; 3] = op.extract()?;
        res[i as usize] += v;
        res[j as usize + 1] -= v;
    }

    for i in 1..length {
        res[i] += res[i - 1];
    }

    res.truncate(length);
    Ok(res)
}
