"""Convenience entry point for training Deformable DETR.

This is a thin wrapper around ``main.py``.  All training/evaluation logic lives
there, so this script only changes the defaults for the small COCO subset that
ships with this repository and for a single 8 GB GPU.

Examples
--------
Train with the defaults (``./data/coco``, 100 epochs, batch size 1)::

    python train_deformable_detr.py

Train for a quick smoke test::

    python train_deformable_detr.py --epochs 1 --output_dir ./output_smoke

Evaluate a checkpoint::

    python main.py --coco_path ./data/coco --resume ./output/checkpoint.pth --eval
"""
import argparse
from pathlib import Path

import torch

from main import get_args_parser as get_main_args_parser
from main import main


def get_args_parser():
    parser = argparse.ArgumentParser(
        'Deformable DETR training script', parents=[get_main_args_parser()])
    parser.set_defaults(
        coco_path='./data/coco',
        epochs=100,
        batch_size=1,
        lr=1e-4,
        num_workers=0,
        output_dir='./output',
    )
    return parser


if __name__ == '__main__':
    args = get_args_parser().parse_args()
    if args.device == 'cuda' and not torch.cuda.is_available():
        print('CUDA is not available, falling back to CPU.')
        args.device = 'cpu'
    if args.output_dir:
        Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    main(args)
