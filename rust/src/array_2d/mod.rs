use pyo3::prelude::*;

mod sorted_matrix_search;

#[pymodule]
pub mod array_2d {
    use super::*;

    #[pymodule_export]
    use sorted_matrix_search::search;
}
