#!/bin/bash -l
#SBATCH --job-name=bloomfilter_job
#SBATCH --output=output.txt
#SBATCH --account=lp_h_ds_2023_2024
#SBATCH --ntasks=1
#SBATCH --time=02:00:00
#SBATCH --mem=32GB
#SBATCH --cluster=wice
#SBATCH --nodes=1

# Load the correct Python module
module load Python/3.11.3-GCCcore-12.3.0
module load psutil/5.9.8-GCCcore-12.3.0
module load matplotlib/3.7.0-gfbf-2022b

# create directory and set PYTHONPATH
cd /vsc-hard-mounts/leuven-user/363/vsc36335
PYTHON_LIB="/apps/leuven/rocky8/skylake/2023a/software/Python/3.11.3-GCCcore-12.3.0/lib/python3.11/site-packages/"
export PYTHONPATH="${PYTHON_LIB}:${PYTHONPATH}"
export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "PYTHONPATH is set to:"
echo $PYTHONPATH

# Run the benchmark script
python benchmark.py
