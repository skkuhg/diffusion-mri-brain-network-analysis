"""
Diffusion MRI Brain Network Analysis Package

A comprehensive toolkit for analyzing diffusion MRI data and constructing
brain connectivity networks using advanced neuroimaging techniques.

Authors: Your Name
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .preprocessing import preprocess_dmri, create_brain_mask
from .tensor_analysis import fit_tensor_model, compute_diffusion_metrics
from .tractography import perform_tractography, quality_control
from .connectivity import create_connectivity_matrix, build_network_graph
from .analysis import analyze_network_topology, compute_centrality_measures
from .machine_learning import prepare_features, train_classifier
from .visualization import plot_diffusion_metrics, create_interactive_network

__all__ = [
    "preprocess_dmri",
    "create_brain_mask", 
    "fit_tensor_model",
    "compute_diffusion_metrics",
    "perform_tractography",
    "quality_control",
    "create_connectivity_matrix",
    "build_network_graph",
    "analyze_network_topology",
    "compute_centrality_measures",
    "prepare_features",
    "train_classifier",
    "plot_diffusion_metrics",
    "create_interactive_network"
]
