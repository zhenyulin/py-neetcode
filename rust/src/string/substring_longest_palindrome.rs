//
// 5. Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/
//

use pyo3::prelude::*;

#[pyfunction]
pub fn longest_palindrome(s: &str) -> PyResult<String> {
    let chars: Vec<char> = s.chars().collect(); // convert to Vec<char> for access
    let n = chars.len();

    let mut l = 0usize;
    let mut r = 1usize; // exclusive

    for i in 0..n {
        for &(mut a, mut b) in [(i, i + 1), (i - 1, i + 1)].iter() {
            // a > b when a turned "negative" (out of index)
            while a < b && b < n && chars[a] == chars[b] {
                a -= 1;
                b += 1;
            }

            if b - (a + 1) > r - l {
                l = a + 1;
                r = b;
            }
        }
    }

    Ok(chars[l..r].iter().collect()) // convert &[char] to String
}
