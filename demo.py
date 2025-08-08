#!/usr/bin/env python3
"""
Demo script for Diffusion MRI Brain Network Analysis

This script demonstrates the basic functionality of the dmri_analysis package
by running a simplified version of the analysis pipeline.

Usage:
    python demo.py

Requirements:
    - All dependencies from requirements.txt installed
    - Internet connection for dataset download
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Add the package to path if not installed
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """
    Run the demo analysis pipeline.
    """
    print("🧠 Diffusion MRI Brain Network Analysis - Demo")
    print("=" * 50)
    
    try:
        # Import core functions
        print("📦 Importing libraries...")
        from dipy.data import read_stanford_hardi
        import networkx as nx
        from sklearn.ensemble import RandomForestClassifier
        
        print("✅ All libraries imported successfully!")
        
        # Download and load data
        print("\n📥 Loading Stanford HARDI dataset...")
        img, gtab = read_stanford_hardi()
        data = img.get_fdata()
        print(f"✅ Data loaded: {data.shape}")
        
        # Basic data exploration
        print("\n🔍 Data exploration:")
        print(f"   • Volume dimensions: {data.shape[:3]}")
        print(f"   • Number of volumes: {data.shape[3]}")
        print(f"   • Number of b0 volumes: {np.sum(gtab.bvals == 0)}")
        print(f"   • Number of DWI volumes: {np.sum(gtab.bvals > 0)}")
        print(f"   • Unique b-values: {np.unique(gtab.bvals)}")
        
        # Simple preprocessing
        print("\n🔧 Basic preprocessing...")
        b0_volume = data[:, :, :, 0]
        threshold = np.percentile(b0_volume[b0_volume > 0], 20)
        brain_mask = b0_volume > threshold
        print(f"✅ Brain mask created: {np.sum(brain_mask)} voxels")
        
        # DTI fitting (simplified)
        print("\n🧮 Tensor analysis...")
        from dipy.reconst.dti import TensorModel
        tenmodel = TensorModel(gtab)
        tenfit = tenmodel.fit(data, brain_mask)
        FA = tenfit.fa
        FA[np.isnan(FA)] = 0
        print(f"✅ FA computed: mean = {np.mean(FA[brain_mask]):.3f}")
        
        # Create simple visualization
        print("\n🎨 Creating visualization...")
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        slice_idx = data.shape[2] // 2
        
        # B0 image
        axes[0].imshow(b0_volume[:, :, slice_idx].T, cmap='gray')
        axes[0].set_title('B0 Image')
        axes[0].axis('off')
        
        # Brain mask
        axes[1].imshow(brain_mask[:, :, slice_idx].T, cmap='gray')
        axes[1].set_title('Brain Mask')
        axes[1].axis('off')
        
        # FA map
        im = axes[2].imshow(FA[:, :, slice_idx].T, cmap='gray', vmin=0, vmax=1)
        axes[2].set_title('Fractional Anisotropy')
        axes[2].axis('off')
        plt.colorbar(im, ax=axes[2], fraction=0.046)
        
        plt.tight_layout()
        plt.savefig('demo_output.png', dpi=150, bbox_inches='tight')
        plt.show()
        print("✅ Visualization saved as 'demo_output.png'")
        
        # Simple connectivity demonstration
        print("\n🔗 Network analysis demo...")
        
        # Create a simple demo network
        n_regions = 10
        connectivity = np.random.rand(n_regions, n_regions)
        connectivity = (connectivity + connectivity.T) / 2  # Make symmetric
        np.fill_diagonal(connectivity, 0)  # Remove self-connections
        
        # Create network graph
        G = nx.from_numpy_array(connectivity)
        
        # Compute basic metrics
        degree_centrality = nx.degree_centrality(G)
        clustering = nx.average_clustering(G)
        
        print(f"✅ Demo network created:")
        print(f"   • Number of nodes: {G.number_of_nodes()}")
        print(f"   • Number of edges: {G.number_of_edges()}")
        print(f"   • Average clustering: {clustering:.3f}")
        print(f"   • Network density: {nx.density(G):.3f}")
        
        # Machine learning demo
        print("\n🤖 Machine learning demo...")
        
        # Create synthetic features
        n_samples = 100
        n_features = 20
        X = np.random.randn(n_samples, n_features)
        y = np.random.choice([0, 1], n_samples)
        
        # Train classifier
        clf = RandomForestClassifier(n_estimators=10, random_state=42)
        clf.fit(X, y)
        
        # Evaluate
        accuracy = clf.score(X, y)
        print(f"✅ Random Forest trained:")
        print(f"   • Training accuracy: {accuracy:.3f}")
        print(f"   • Number of features: {n_features}")
        print(f"   • Number of samples: {n_samples}")
        
        print("\n🎉 Demo completed successfully!")
        print("\nNext steps:")
        print("1. Open the Jupyter notebook for the full analysis")
        print("2. Explore the web interface (Diffusion MRI Brain Network Analysis.html)")
        print("3. Customize parameters in config.ini")
        print("4. Try your own data!")
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        return 1
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Please check your installation and try again.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
