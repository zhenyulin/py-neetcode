use pyo3::prelude::*;

#[pyfunction]
pub fn word_break(s: &str, word_dict: Vec<String>) -> bool {
    let n = s.len();
    let mut dp = vec![false; n + 1];
    dp[0] = true;

    for i in 1..=n {
        for w in &word_dict {
            let m = w.len();
            if i >= m && dp[i - m] && &s[i - m..i] == w {
                dp[i] = true;
                break;
            }
        }
    }

    dp[n]
}
