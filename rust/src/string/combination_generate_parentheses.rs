use pyo3::prelude::*;

#[pyfunction]
pub fn generate_parentheses(n: i32) -> PyResult<Vec<String>> {
    fn add(left: i32, right: i32, s: &mut String, res: &mut Vec<String>) {
        if left == 0 && right == 0 {
            res.push(s.clone());
            return;
        }
        if left > 0 {
            s.push('(');
            add(left - 1, right, s, res);
            s.pop();
        }
        if right > left {
            s.push(')');
            add(left, right - 1, s, res);
            s.pop();
        }
    }

    let mut res = Vec::new();
    let mut s = String::with_capacity((2 * n) as usize);
    add(n, n, &mut s, &mut res);
    Ok(res)
}
