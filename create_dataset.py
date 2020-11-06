from generate_data import generate_data

generate_data(n_samples=1,
              n_objects=1,
              backgronds_pattern="data/backgrounds/*",
              objects_pattern="data/objects/*",
              output_dir="data/output",
              show=False)
