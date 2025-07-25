use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
pub fn group_anagrams(strs: Vec<String>) -> PyResult<Vec<Vec<String>>> {
    let mut groups: HashMap<String, Vec<String>> = HashMap::new();
    for s in strs {
        let mut chars: Vec<char> = s.chars().collect();
        chars.sort_unstable();
        let key: String = chars.into_iter().collect();
        groups.entry(key).or_default().push(s);
    }
    Ok(groups.into_values().collect())
}
