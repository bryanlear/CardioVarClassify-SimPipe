# src/main_pipeline.py
import yaml
import os 
from module1_input_loader import load_vcf_data #module 1 for vcf loading

CONFIG_FILE_PATH = "config/pipeline_config.yaml"

def load_config(config_path):
    """Loads YAML configuration file."""
    try:
        with open(config_path, 'r') as f:
            config_data = yaml.safe_load(f) # good for security
        print(f"Configuration loaded successfully from: {config_path}")
        return config_data
    except FileNotFoundError:
        print(f"ERROR: Configuration file not found at {config_path}")
        return None
    except yaml.YAMLError as e:
        print(f"ERROR: Could not parse YAML configuration file: {e}")
        return None

def ensure_dir(directory_path):
    """Ensures directory exists, create if necessary."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created directory: {directory_path}")

def run_pipeline():
    """
    Main function to orchestrate CardioVarClassify-SimPipe pipeline execution
    """
    print("Starting CardioVarClassify-SimPipe...")

    # 1. Load Configuration
    config = load_config(CONFIG_FILE_PATH)
    if config is None:
        print("Pipeline execution aborted due to configuration error.")
        return

    output_directory = config.get('paths', {}).get('output_dir', 'results/default_output/')
    ensure_dir(output_directory)
    print(f"Output will be saved to: {output_directory}")

    # --- MODULE 1: Input & Data Loading ---
    print("\n=== Module 1: Input & Data Loading ===")
    
    # Get VCF path fromloaded configuration
    # safer way to access nested dictionary keys
    input_vcf_path = config.get('paths', {}).get('input_vcf') 

    if not input_vcf_path:
        print("ERROR: 'input_vcf' path not found in configuration file under 'paths'.")
        return
    
    print(f"Attempting to load VCF from: {input_vcf_path}")
    variants_module1_output = load_vcf_data(input_vcf_path) # Pass the path to your function

    if variants_module1_output:
        print(f"Successfully loaded {len(variants_module1_output)} variants from VCF.")
    else:
        print("Failed to load variants. Exiting pipeline.")
        return
# this then is passed to the next module
    # --- Placeholder Module 2: Variant Pre-processing & QC ---

    print("\nCardioVarClassify-SimPipe finished.")

if __name__ == "__main__":
    run_pipeline()