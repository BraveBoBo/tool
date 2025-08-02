
import os
import torch

def get_rank():
    return torch.distributed.get_rank() if torch.distributed.is_initialized() else 0

def get_world_size():
    return torch.distributed.get_world_size() if torch.distributed.is_initialized() else 1