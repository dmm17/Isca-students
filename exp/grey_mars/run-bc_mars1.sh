#!/bin/bash

#SBATCH --job-name=mars8
#SBATCH --partition=serial
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=6:00:00
#SBATCH --mem=20G

module load build/gcc-7.2.0
module load languages/anaconda2/5.0.1
module load tools/git/2.18.0

echo 'modules loaded'
module list

source activate isca_env

time python mars3.py
