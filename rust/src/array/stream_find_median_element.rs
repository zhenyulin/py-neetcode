use pyo3::prelude::*;
use std::collections::BinaryHeap;

#[pyclass]
pub struct MedianFinder {
    left: BinaryHeap<i32>,
    right: BinaryHeap<i32>,
}

#[pymethods]
impl MedianFinder {
    #[new]
    fn new() -> Self {
        Self {
            left: BinaryHeap::new(),
            right: BinaryHeap::new(),
        }
    }

    #[inline]
    fn add_num(&mut self, num: i32) {
        if self.left.peek().is_none_or(|&x| num <= x) {
            self.left.push(num);
        } else {
            self.right.push(-num);
        }

        if self.left.len() > self.right.len() + 1 {
            self.right.push(-self.left.pop().unwrap());
        } else if self.right.len() > self.left.len() {
            self.left.push(-self.right.pop().unwrap());
        }
    }

    #[inline]
    fn find_median(&self) -> f64 {
        if self.left.len() == self.right.len() {
            (self.left.peek().unwrap() - self.right.peek().unwrap()) as f64 / 2.0
        } else {
            *self.left.peek().unwrap() as f64
        }
    }
}
