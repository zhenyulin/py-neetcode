use pyo3::prelude::*;

#[pyfunction]
pub fn check_inclusion(s1: &str, s2: &str) -> bool {
    if s1.len() > s2.len() {
        return false;
    }

    let (mut count1, mut count2) = ([0i32; 26], [0i32; 26]);
    let (bytes1, bytes2) = (s1.as_bytes(), s2.as_bytes());

    for i in 0..s1.len() {
        count1[(bytes1[i] - b'a') as usize] += 1;
        count2[(bytes2[i] - b'a') as usize] += 1;
    }

    for j in s1.len()..s2.len() {
        if count1 == count2 {
            return true;
        }

        count2[(bytes2[j] - b'a') as usize] += 1;
        count2[(bytes2[j - s1.len()] - b'a') as usize] -= 1;
    }

    count1 == count2
}
