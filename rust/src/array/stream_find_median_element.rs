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

    fn add_num(&mut self, num: i32) {
        self.right.push(-num);
        self.left.push(-self.right.pop().unwrap());

        if self.left.len() > self.right.len() {
            self.right.push(-self.left.pop().unwrap());
        }
    }

    fn find_median(&self) -> f64 {
        if self.left.len() == self.right.len() {
            (self.left.peek().unwrap() - self.right.peek().unwrap()) as f64 / 2.0
        } else {
            -self.right.peek().unwrap() as f64
        }
    }
}
