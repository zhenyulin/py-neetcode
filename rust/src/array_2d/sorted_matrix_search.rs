use pyo3::prelude::*;

#[pyfunction]
pub fn search(matrix: Vec<Vec<i32>>, target: i32) -> PyResult<bool> {
    if matrix.is_empty() || matrix[0].is_empty() {
        return Ok(false);
    }

    let rows = matrix.len();
    let cols = matrix[0].len();

    let (mut top, mut bot) = (0usize, rows - 1);
    while top <= bot {
        let row = (top + bot) / 2;

        if target > *matrix[row].last().unwrap() {
            top = row + 1;
        } else if target < matrix[row][0] {
            if row == 0 {
                return Ok(false);
            }
            bot = row - 1;
        } else {
            let (mut l, mut r) = (0usize, cols - 1);
            while l <= r {
                let m = (l + r) / 2;

                if target > matrix[row][m] {
                    l = m + 1;
                } else if target < matrix[row][m] {
                    if m == 0 {
                        break;
                    }
                    r = m - 1;
                } else {
                    return Ok(true);
                }
            }

            return Ok(false);
        }
    }

    Ok(false)
}
