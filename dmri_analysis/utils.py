"""
Utility functions for diffusion MRI analysis.
"""

import numpy as np
import os
import configparser
from typing import Tuple, Optional


def load_config(config_path: str = "config.ini") -> configparser.ConfigParser:
    """
    Load configuration parameters from file.
    
    Parameters
    ----------
    config_path : str
        Path to configuration file
        
    Returns
    -------
    config : configparser.ConfigParser
        Configuration object
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def ensure_directory(directory: str) -> None:
    """
    Create directory if it doesn't exist.
    
    Parameters
    ----------
    directory : str
        Directory path to create
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def validate_data_shape(data: np.ndarray, expected_dims: int = 4) -> bool:
    """
    Validate that data has expected number of dimensions.
    
    Parameters
    ----------
    data : np.ndarray
        Input data array
    expected_dims : int
        Expected number of dimensions
        
    Returns
    -------
    bool
        True if data shape is valid
    """
    return data.ndim == expected_dims


def compute_snr(signal: np.ndarray, noise: Optional[np.ndarray] = None) -> float:
    """
    Compute signal-to-noise ratio.
    
    Parameters
    ----------
    signal : np.ndarray
        Signal data
    noise : np.ndarray, optional
        Noise data. If None, uses std of signal
        
    Returns
    -------
    float
        Signal-to-noise ratio
    """
    if noise is None:
        noise_level = np.std(signal)
    else:
        noise_level = np.std(noise)
    
    if noise_level == 0:
        return float('inf')
    
    return np.mean(signal) / noise_level


def safe_divide(numerator: np.ndarray, denominator: np.ndarray, 
                default_value: float = 0.0) -> np.ndarray:
    """
    Safe division avoiding division by zero.
    
    Parameters
    ----------
    numerator : np.ndarray
        Numerator array
    denominator : np.ndarray
        Denominator array
    default_value : float
        Value to use when denominator is zero
        
    Returns
    -------
    np.ndarray
        Result of safe division
    """
    result = np.full_like(numerator, default_value, dtype=float)
    mask = denominator != 0
    result[mask] = numerator[mask] / denominator[mask]
    return result


def normalize_data(data: np.ndarray, method: str = "minmax") -> np.ndarray:
    """
    Normalize data using specified method.
    
    Parameters
    ----------
    data : np.ndarray
        Input data
    method : str
        Normalization method: "minmax", "zscore", or "robust"
        
    Returns
    -------
    np.ndarray
        Normalized data
    """
    if method == "minmax":
        data_min = np.min(data)
        data_max = np.max(data)
        if data_max == data_min:
            return np.zeros_like(data)
        return (data - data_min) / (data_max - data_min)
    
    elif method == "zscore":
        mean = np.mean(data)
        std = np.std(data)
        if std == 0:
            return np.zeros_like(data)
        return (data - mean) / std
    
    elif method == "robust":
        median = np.median(data)
        mad = np.median(np.abs(data - median))
        if mad == 0:
            return np.zeros_like(data)
        return (data - median) / (1.4826 * mad)
    
    else:
        raise ValueError(f"Unknown normalization method: {method}")


def progress_bar(current: int, total: int, width: int = 50) -> str:
    """
    Create a simple text progress bar.
    
    Parameters
    ----------
    current : int
        Current progress
    total : int
        Total items
    width : int
        Width of progress bar
        
    Returns
    -------
    str
        Progress bar string
    """
    percentage = current / total
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {percentage:.1%} ({current}/{total})"


def memory_usage() -> str:
    """
    Get current memory usage information.
    
    Returns
    -------
    str
        Memory usage description
    """
    try:
        import psutil
        process = psutil.Process()
        memory_info = process.memory_info()
        memory_mb = memory_info.rss / 1024 / 1024
        return f"Memory usage: {memory_mb:.1f} MB"
    except ImportError:
        return "Memory monitoring unavailable (install psutil)"


def timing_decorator(func):
    """
    Decorator to time function execution.
    """
    import time
    import functools
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} completed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper
