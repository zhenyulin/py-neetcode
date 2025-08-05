use pyo3::prelude::*;

#[pyfunction]
pub fn longest_common_subsequence(text1: &str, text2: &str) -> PyResult<i32> {
    let mut dp = vec![0; text2.len() + 1];

    let (bytes1, bytes2) = (text1.as_bytes(), text2.as_bytes());

    for &b1 in bytes1 {
        let mut b1_max = 0;
        for (j, &b2) in bytes2.iter().enumerate() {
            let b1_max_next = dp[j + 1];
            if b1 == b2 {
                dp[j + 1] = b1_max + 1;
            } else {
                dp[j + 1] = dp[j + 1].max(dp[j]);
            }
            b1_max = b1_max_next;
        }
    }

    Ok(dp[text2.len()])
}
