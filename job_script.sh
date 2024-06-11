#!/bin/bash
#SBATCH --job-name=bloomfilter_benchmark
#SBATCH --output=benchmark_output.txt
#SBATCH --ntasks=1
#SBATCH --time=01:00:00
#SBATCH --mem=4GB

current_date_time=$(date)
echo "Starting benchmark at: $current_date_time"

# Module load commands:
module load Python/3.7.0-foss-2018b
module load psutil/5.9.5-GCCcore-12.2.0
#mkdir -p "${VSC_DATA}/python_lib/lib/python3.7/site-packages/"
#export PYTHONPATH="${VSC_DATA}/python_lib/lib/python3.7/site-packages/:${PYTHONPATH}"
python benchmark.py
