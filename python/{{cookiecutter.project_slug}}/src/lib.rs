use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn diff_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a - b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn {{cookiecutter.project_slug}}(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(diff_as_string, m)?)?;
    Ok(())
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sum_as_string_test() {
        let result = sum_as_string(1, 2);
        assert!(result.is_ok());
        let result_string = result.unwrap();
        assert_eq!(result_string, "3");
    }

    #[test]
    fn diff_as_string_test() {
        let result = diff_as_string(4, 1);
        assert!(result.is_ok());
        let result_string = result.unwrap();
        assert_eq!(result_string, "3");
    }
}
