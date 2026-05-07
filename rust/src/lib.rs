use pyo3::prelude::*;
use pyo3::types::{PyDict, PyModule};
use pyo3::wrap_pymodule;

mod array;
mod array_2d;
mod string;

#[pymodule]
fn rust(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pymodule!(array::array))?;
    m.add_wrapped(wrap_pymodule!(array_2d::array_2d))?;
    m.add_wrapped(wrap_pymodule!(string::string))?;

    // enables "from rust.string import"
    let sys = PyModule::import(py, "sys")?;
    let modules: Bound<'_, PyDict> = sys.getattr("modules")?.downcast_into()?;
    let array_mod: Bound<'_, PyModule> = m.getattr("array")?.downcast_into()?;
    let array_2d_mod: Bound<'_, PyModule> = m.getattr("array_2d")?.downcast_into()?;
    let string_mod: Bound<'_, PyModule> = m.getattr("string")?.downcast_into()?;

    modules.set_item("rust.array", &array_mod)?;
    modules.set_item("rust.array_2d", &array_2d_mod)?;
    modules.set_item("rust.string", &string_mod)?;

    Ok(())
}
