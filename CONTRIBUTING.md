# Contributing to Diffusion MRI Brain Network Analysis

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the Diffusion MRI Brain Network Analysis pipeline.

## 🤝 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. **Search existing issues** to avoid duplicates
2. **Create a new issue** using the appropriate template
3. **Provide detailed information**:
   - Clear description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs. actual behavior
   - System information (OS, Python version, package versions)
   - Relevant code snippets or error messages

### Suggesting Enhancements

We welcome suggestions for new features or improvements:

1. **Check the roadmap** in the README to see if it's already planned
2. **Open an issue** with the "enhancement" label
3. **Describe the feature** in detail:
   - Use case and motivation
   - Proposed implementation approach
   - Potential impact on existing functionality
   - Alternative solutions considered

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment manager (venv, conda, etc.)

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork**:
```bash
git clone https://github.com/skkuhg/diffusion-mri-brain-network-analysis.git
cd diffusion-mri-brain-network-analysis
```

3. **Create a virtual environment**:
```bash
python -m venv dev_env
source dev_env/bin/activate  # On Windows: dev_env\Scripts\activate
```

4. **Install development dependencies**:
```bash
pip install -r requirements.txt
pip install -e .[dev]
```

5. **Install pre-commit hooks**:
```bash
pre-commit install
```

## 📝 Code Style and Standards

### Python Code Style

We follow PEP 8 with some modifications:

- **Line length**: 88 characters (Black default)
- **Imports**: Use isort for import sorting
- **Type hints**: Encouraged for new code
- **Docstrings**: NumPy style documentation

### Code Formatting

We use automated tools for consistent formatting:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Check code style with flake8
flake8 .
```

### Documentation Style

- **Docstrings**: Use NumPy style for functions and classes
- **Comments**: Clear and concise explanations
- **Type hints**: Include for function parameters and returns
- **Examples**: Provide usage examples where helpful

Example docstring format:
```python
def example_function(param1: np.ndarray, param2: int = 10) -> Tuple[float, bool]:
    """
    Brief description of the function.
    
    Longer description if needed, explaining the purpose,
    algorithm, or important details.
    
    Parameters
    ----------
    param1 : np.ndarray
        Description of the first parameter
    param2 : int, optional
        Description of the second parameter (default: 10)
        
    Returns
    -------
    result : float
        Description of the first return value
    success : bool
        Description of the second return value
        
    Examples
    --------
    >>> result, success = example_function(data, 5)
    >>> print(f"Result: {result}, Success: {success}")
    """
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=dmri_analysis

# Run specific test file
pytest tests/test_preprocessing.py
```

### Writing Tests

- **Test files**: Place in `tests/` directory
- **Naming**: Use `test_*.py` pattern
- **Coverage**: Aim for >80% code coverage
- **Types**: Include unit tests, integration tests, and doctests

Example test structure:
```python
import pytest
import numpy as np
from dmri_analysis.preprocessing import preprocess_dmri

class TestPreprocessing:
    def test_preprocess_dmri_basic(self):
        """Test basic preprocessing functionality."""
        # Create mock data
        data = np.random.randn(10, 10, 10, 20)
        gtab = create_mock_gtab()
        
        # Run preprocessing
        result, mask = preprocess_dmri(data, gtab)
        
        # Assert expected behavior
        assert result.shape == data.shape
        assert mask.shape == data.shape[:3]
        assert np.all(mask >= 0)
```

## 📋 Pull Request Process

### Before Submitting

1. **Create a feature branch**:
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** following the style guidelines

3. **Add tests** for new functionality

4. **Update documentation** as needed

5. **Run the test suite**:
```bash
pytest
black .
flake8 .
```

6. **Commit your changes**:
```bash
git add .
git commit -m "Add feature: brief description"
```

### Commit Message Format

Use clear, descriptive commit messages:

```
Add feature: brief description

Longer explanation of the change if needed.
Include motivation and context.

- List specific changes
- Include any breaking changes
- Reference relevant issues (#123)
```

### Submitting the Pull Request

1. **Push to your fork**:
```bash
git push origin feature/your-feature-name
```

2. **Create a pull request** on GitHub

3. **Fill out the PR template** with:
   - Description of changes
   - Motivation and context
   - Type of change (bug fix, feature, etc.)
   - Testing information
   - Checklist completion

4. **Wait for review** and address feedback

## 🏷️ Release Process

For maintainers:

1. **Update version** in `__init__.py` and `setup.py`
2. **Update CHANGELOG.md** with new version details
3. **Create a release tag**:
```bash
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin v1.1.0
```
4. **Create GitHub release** with release notes

## 📚 Documentation

### Building Documentation

```bash
cd docs/
make html
```

### Documentation Standards

- **README**: Keep updated with new features
- **API docs**: Auto-generated from docstrings
- **Tutorials**: Step-by-step guides for common tasks
- **Examples**: Working code examples

## 🌟 Recognition

Contributors will be recognized in:

- **AUTHORS.md** file
- **Release notes** for significant contributions
- **README acknowledgments** section

## 📞 Getting Help

If you need help with contributing:

1. **Check the wiki** for detailed guides
2. **Join discussions** on GitHub
3. **Ask questions** in issues with the "question" label
4. **Contact maintainers** directly if needed

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

### Summary

- **Be respectful** and inclusive
- **Welcome newcomers** and help them learn
- **Focus on constructive feedback**
- **Respect different viewpoints** and experiences

Thank you for contributing to the advancement of neuroimaging research! 🧠✨
