use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
pub fn can_be_grouped(mut hand: Vec<i32>, group_size: i32) -> bool {
    if group_size <= 0 {
        return false;
    }

    let group_size = group_size as usize;
    if !hand.len().is_multiple_of(group_size) {
        return false;
    }

    if group_size == 1 || hand.is_empty() {
        return true;
    }

    let mut counts = HashMap::with_capacity(hand.len());
    for &n in &hand {
        *counts.entry(n).or_insert(0) += 1;
    }

    hand.sort_unstable();

    for start in hand {
        let needed = match counts.get(&start) {
            Some(&count) if count > 0 => count,
            _ => continue,
        };

        for offset in 0..group_size {
            let n = match start.checked_add(offset as i32) {
                Some(n) => n,
                None => return false,
            };

            match counts.get_mut(&n) {
                Some(count) if *count >= needed => *count -= needed,
                _ => return false,
            }
        }
    }

    true
}
