import argparse
import logging as log

import torch

from config import setup_seed
import os

parser = argparse.ArgumentParser(description='[ML] Machine Learning Experiments Template')

# model
parser.add_argument('--dropout', type=float, default=0.05, help='input sequence length')
parser.add_argument('--freq', type=str, default="min", help='freq for time features encoding')
parser.add_argument('--in_features', type=int, default=7, help='input features')
parser.add_argument('--num_embed', type=int, default=512, help='dimension size of model')
parser.add_argument('--univariate', action='store_true', help='use multiple gpus', default=True)

# experiments
parser.add_argument('--adjust_learning_rate', action='store_true', help='optimizer learning rate', default=True)
parser.add_argument('--batch_size', type=int, default=32, help='batch size of train data')
parser.add_argument('--checkpoints', type=str, default=os.path.join('.', 'checkpoints'),
                    help='location of model checkpoints')
parser.add_argument('--early_stop', action='store_true', help='optimizer learning rate', default=True)
parser.add_argument('--dataset_dir', type=str, default=os.path.join('.', 'datasets'), help='datasets root directory')
parser.add_argument('--learning_rate', type=float, default=0.001, help='optimizer learning rate')
parser.add_argument('--patience', type=int, default=3, help='early stopping patience')
parser.add_argument('--seed', type=int, default=2024, help='seed of experiment')
parser.add_argument('--train_epochs', type=int, default=15, help='train epochs')
parser.add_argument('--use_amp', action='store_true', help='use automatic mixed precision training', default=False)

parser.add_argument('--gpu', type=int, default=0, help='gpu device number')
parser.add_argument('--use_multi_gpu', action='store_true', help='use multiple gpus', default=False)
parser.add_argument('--devices', type=str, default='0,1,2,3', help='device ids of multiple gpus')

args = parser.parse_args()

setup_seed(args.seed)

# Check if a GPU is available
device = torch.device("cpu")
if torch.backends.mps.is_available():
    device = torch.device("mps")
    log.info("GPU Available. Using mps GPU.")
elif torch.cuda.is_available():
    device = torch.device(f"cuda:{args.gpu}")
    log.info("GPU Available. Using GPU[%d]: %s", args.gpu, torch.cuda.get_device_name(0))
else:
    log.info("No GPU available. Using CPU.")

if not os.path.exists(args.checkpoints):
    os.makedirs(args.checkpoints)
