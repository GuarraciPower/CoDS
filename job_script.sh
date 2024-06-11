#!/bin/bash
#SBATCH --job-name=bloomfilter_benchmark
#SBATCH --output=benchmark_output.txt
#SBATCH --ntasks=1
#SBATCH --time=01:00:00
#SBATCH --mem=4GB

module load Python/3.7.0-foss-2018b
#mkdir -p "${VSC_DATA}/python_lib/lib/python3.7/site-packages/"
#export PYTHONPATH="${VSC_DATA}/python_lib/lib/python3.7/site-packages/:${PYTHONPATH}"
python benchmark.py
