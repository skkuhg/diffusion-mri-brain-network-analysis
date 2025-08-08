# 🧠 Diffusion MRI Brain Network Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![DIPY](https://img.shields.io/badge/DIPY-Neuroimaging-red.svg)](https://dipy.org/)

An automated pipeline for analyzing diffusion MRI data and constructing brain connectivity networks using advanced neuroimaging techniques.

![Brain Network Visualization](https://via.placeholder.com/800x400/667eea/ffffff?text=Interactive+3D+Brain+Network)

## 🚀 Features

- **📥 Automatic Dataset Download**: Stanford HARDI dataset integration
- **🔧 Advanced Preprocessing**: Denoising and brain extraction optimized for laptops
- **🧮 Tensor Analysis**: Fractional Anisotropy (FA) and diffusion metrics computation
- **🧵 Tractography**: White matter pathway reconstruction
- **🔗 Connectivity Analysis**: Structural connectivity matrix construction
- **📊 Graph Theory**: Network topology and centrality analysis
- **🤖 Machine Learning**: Brain state classification using Random Forest
- **🧠 Deep Learning**: Neural networks for advanced connectivity analysis
- **🎨 Interactive Visualization**: 3D brain network exploration with Plotly

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- 4GB+ RAM (8GB+ recommended)
- 2GB free disk space

### Python Dependencies
```
dipy>=1.7.0
nibabel>=4.0.0
nilearn>=0.10.0
networkx>=2.8
scikit-learn>=1.2.0
matplotlib>=3.6.0
seaborn>=0.12.0
plotly>=5.17.0
pandas>=1.5.0
numpy>=1.24.0
scipy>=1.10.0
tensorflow>=2.13.0
```

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/skkuhg/diffusion-mri-brain-network-analysis.git
cd diffusion-mri-brain-network-analysis
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv dmri_env
source dmri_env/bin/activate  # On Windows: dmri_env\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Launch Jupyter Notebook**:
```bash
jupyter notebook
```

5. **Open the analysis notebook**:
Navigate to `Diffusion_MRI_Brain_Network_Analysis.ipynb`

## 📊 Usage

### Quick Start

1. **Run the installation cell** to install all required packages
2. **Execute cells sequentially** - each section builds on the previous one
3. **Explore interactive visualizations** - rotate and zoom the 3D brain networks
4. **Modify parameters** as needed for your specific analysis

### Web Interface

For a quick preview without running the notebook:
1. Open `brain_network_analysis_webapp.html` in your browser
2. Use the interface to explore the analysis pipeline
3. Click "Open in Jupyter" to launch the interactive notebook

### Dataset

The pipeline automatically downloads the **Stanford HARDI dataset**:
- Small size (~20MB) perfect for demonstration
- High-quality diffusion MRI data
- Multiple b-values and gradient directions
- Suitable for educational purposes

## 🔬 Analysis Pipeline

### 1. Data Preprocessing
- **Denoising**: Gaussian smoothing optimized for laptop performance
- **Brain Extraction**: Simple threshold-based masking
- **Quality Control**: SNR assessment and visualization

### 2. Diffusion Tensor Imaging (DTI)
- **Tensor Fitting**: Robust estimation with outlier handling
- **Metric Computation**: FA, MD, AD, RD calculations
- **Color Mapping**: RGB directional encoding

### 3. Tractography
- **Fiber Tracking**: Deterministic streamline generation
- **Pathway Reconstruction**: White matter bundle identification
- **Quality Assessment**: Length and curvature analysis

### 4. Network Construction
- **Parcellation**: Brain region definition
- **Connectivity Matrix**: Structural connection quantification
- **Graph Creation**: NetworkX graph object generation

### 5. Graph Theory Analysis
- **Centrality Measures**: Degree, betweenness, closeness, eigenvector
- **Network Topology**: Clustering, path length, efficiency
- **Hub Identification**: Critical node detection

### 6. Machine Learning
- **Feature Extraction**: Connectivity-based feature vectors
- **Classification**: Random Forest brain state prediction
- **Validation**: Cross-validation and performance metrics

### 7. Deep Learning
- **Neural Networks**: TensorFlow/Keras implementation
- **Architecture**: Multi-layer perceptron with dropout
- **Training**: Early stopping and batch normalization

## 📈 Results and Visualizations

The pipeline generates comprehensive visualizations:

- **📊 Data Quality Plots**: Signal-to-noise ratio, motion assessment
- **🎨 Diffusion Maps**: FA, MD, color-coded directionality
- **🧵 Tractography**: 3D streamline visualization
- **🔗 Connectivity Matrices**: Heatmaps and network graphs
- **📈 Machine Learning**: ROC curves, confusion matrices
- **🌐 Interactive 3D**: Plotly-based brain network exploration

## 🔧 Customization

### Modify Analysis Parameters

```python
# Adjust preprocessing parameters
gaussian_sigma = 0.8  # Smoothing kernel size
fa_threshold = 0.2    # Tractography threshold

# Change network analysis
n_regions = 20        # Number of brain regions
n_streamlines = 1000  # Tractography density

# ML parameters
n_estimators = 100    # Random Forest trees
test_size = 0.3       # Train/test split
```

### Add Custom Brain Atlases

```python
# Use your own parcellation
from nilearn.datasets import fetch_atlas_harvard_oxford
atlas = fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 References

### Software Packages
- **DIPY**: Garyfallidis, E., et al. (2014). Dipy, a library for the analysis of diffusion MRI data. Frontiers in Neuroinformatics, 8, 8.
- **NetworkX**: Hagberg, A., et al. (2008). Exploring network structure, dynamics, and function using NetworkX. Proceedings of the 7th Python in Science Conference.
- **Scikit-learn**: Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.

### Scientific Background
- **Diffusion MRI**: Basser, P. J., & Pierpaoli, C. (1996). Microstructural and physiological features of tissues elucidated by quantitative-diffusion-tensor MRI. Journal of Magnetic Resonance, 111(3), 209-219.
- **Brain Networks**: Sporns, O. (2013). Network attributes for segregation and integration in the human brain. Current Opinion in Neurobiology, 23(2), 162-171.
- **Graph Theory**: Bullmore, E., & Sporns, O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. Nature Reviews Neuroscience, 10(3), 186-198.

## 🆘 Support

If you encounter any issues or have questions:

1. **Check the FAQ** in the wiki
2. **Search existing issues** on GitHub
3. **Create a new issue** with detailed description
4. **Join the discussion** in the community forum

## 🏆 Acknowledgments

- Stanford University for providing the HARDI dataset
- The DIPY development team for the excellent neuroimaging library
- The neuroimaging community for open-source tools and methodologies

## 📞 Contact

- **Author**: Your Name
- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- **Twitter**: [@YourTwitter](https://twitter.com/yourtwitter)

---

⭐ **Star this repository** if you find it helpful for your neuroimaging research!

🔬 **Cite this work** if you use it in your publications:
```bibtex
@software{brain_network_analysis_2025,
  author = {Your Name},
  title = {Diffusion MRI Brain Network Analysis Pipeline},
  url = {https://github.com/yourusername/diffusion-mri-brain-network-analysis},
  year = {2025}
}
```
