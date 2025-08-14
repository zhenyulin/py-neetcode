use pyo3::prelude::*;

mod rotated_sorted_array_min;
mod rotated_sorted_array_search;

#[pymodule]
pub mod array {
    use super::*;

    #[pymodule_export]
    use rotated_sorted_array_min::find_min;
    #[pymodule_export]
    use rotated_sorted_array_search::search;
}
