use pyo3::prelude::*;

#[pyfunction]
pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
    let (mut total, mut tank, mut start) = (0, 0, 0);

    for (i, (&g, &c)) in gas.iter().zip(cost.iter()).enumerate() {
        let delta = g - c;
        total += delta;
        tank += delta;
        if tank < 0 {
            start = i + 1;
            tank = 0;
        }
    }

    if total >= 0 { start as i32 } else { -1 }
}
