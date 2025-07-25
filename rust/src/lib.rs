use pyo3::prelude::*;
use pyo3::types::{PyDict, PyModule};
use pyo3::wrap_pyfunction;

mod string;

#[pymodule]
fn rust(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    // rust.string
    let string_mod = PyModule::new_bound(py, "string")?;
    string_mod.add_function(wrap_pyfunction!(string::group_anagrams_py, &string_mod)?)?;

    m.add_submodule(&string_mod)?;
    m.add("string", &string_mod)?;

    // enables "from rust.string import"
    let sys = PyModule::import_bound(py, "sys")?;
    let modules: Bound<'_, PyDict> = sys.getattr("modules")?.downcast_into()?;
    modules.set_item("rust.string", &string_mod)?;

    Ok(())
}
