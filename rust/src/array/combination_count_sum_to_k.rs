use pyo3::prelude::*;

#[pyfunction]
pub fn ways_of_change(coins: Vec<i32>, amount: i32) -> i32 {
    let amount = amount as usize;
    let mut dp = vec![0_i32; amount + 1];
    dp[0] = 1;

    for coin in coins {
        let coin = coin as usize;
        for i in coin..=amount {
            dp[i] += dp[i - coin];
        }
    }

    dp[amount]
}
