# src/module1_input_loader.py
# to run main pipeline:
# (cyvcf2_env) CardioVarClassify-SimPipe % python src/main_pipeline.py

from cyvcf2 import VCF 


def load_vcf_data(vcf_filepath):
    """
    Loads variant data from VCF using cyvcf2

    Args:
        vcf_filepath (str): Path to the VCF file

    Returns:
        List of variant records (cyvcf2 Variant objects)
        Returns None if file cannot be opened
    """
    try:
        vcf_reader = VCF(vcf_filepath)
        print(f"Successfully opened VCF file: {vcf_filepath}")
        # header info
        # print(f"VCF Header Samples: {vcf_reader.samples}")
        
        variants = []
        for record in vcf_reader:
            variants.append(record) 
        
        print(f"Found {len(variants)} variants.")
        return variants
    except FileNotFoundError:
        print(f"Error: VCF file not found at {vcf_filepath}")
        return None
    except Exception as e: #other exceptions can be caught too
        print(f"An error occurred while reading VCF: {e}")
        return None


#THIS IS FOR TESTING 
# if __name__ == '__main__':
#     dummy_vcf_path = "data/input_vcfs/dummy_cardio_variants.vcf" 
    
#     print(f"Attempting to load VCF: {dummy_vcf_path}")
#     loaded_variants = load_vcf_data(dummy_vcf_path)

#     if loaded_variants:
#         print("\nFirst variant details (as an example using cyvcf2):")
#         if len(loaded_variants) > 0:
#             first_variant = loaded_variants[0]
#             print(f"  Chrom: {first_variant.CHROM}")
#             print(f"  Pos: {first_variant.POS}") # POS is 1-based in cyvcf2 output
#             print(f"  Ref: {first_variant.REF}")
#             print(f"  Alt: {first_variant.ALT}") # Returns list ALT alleles
#             print(f"  Info: {dict(first_variant.INFO)}") # Access INFO fields
#         else:
#             print("No variants were loaded to display details.")
#     else:
#         print("VCF loading failed.")