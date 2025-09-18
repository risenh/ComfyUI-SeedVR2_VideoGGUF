"""
Shared constants and utilities for SeedVR2
Only includes constants actually used in the codebase
"""

import os

# Model folder names
SEEDVR2_FOLDER_NAME = "SEEDVR2"  # Physical folder name on disk
# SEEDVR2_MODEL_TYPE = "seedvr2"   # Model type identifier for ComfyUI
SEEDVR2_MODEL_TYPE = "SEEDVR2"   # Model type identifier for ComfyUI


# Supported model file formats
#SUPPORTED_MODEL_EXTENSIONS = {'.safetensors', '.gguf'}
SUPPORTED_MODEL_EXTENSIONS = {'.safetensors'}

def get_script_directory():
    """Get the root script directory path (3 levels up from this file)"""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# def get_base_cache_dir():
#     """Get or create the model cache directory"""
#     try:
#         import folder_paths # only works if comfyui is available
#         cache_dir = os.path.join(folder_paths.models_dir, SEEDVR2_FOLDER_NAME)
#         folder_paths.add_model_folder_path(SEEDVR2_MODEL_TYPE, cache_dir)
#     except:
#         cache_dir = f"./{SEEDVR2_MODEL_TYPE}_models"
#     
#     os.makedirs(cache_dir, exist_ok=True)
#     return cache_dir
    
def get_base_cache_dir():
    """Get or create the model cache directory (优先使用配置路径)"""
    try:
        import folder_paths
        # 尝试从配置中获取路径（此时 SEEDVR2_MODEL_TYPE 已改为 "SEEDVR2"）
        config_paths = folder_paths.get_folder_paths(SEEDVR2_MODEL_TYPE)
        if config_paths:  # 如果配置中有路径，优先使用第一个
            cache_dir = config_paths[0]
        else:  # 配置中没有时，才使用默认路径
            cache_dir = os.path.join(folder_paths.models_dir, SEEDVR2_FOLDER_NAME)
            folder_paths.add_model_folder_path(SEEDVR2_MODEL_TYPE, cache_dir)
    except:
        # 未在 ComfyUI 环境中时的 fallback
        cache_dir = f"./{SEEDVR2_MODEL_TYPE}_models"
    
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir
    
def is_supported_model_file(filename: str) -> bool:
    """Check if a file has a supported model extension"""
    return any(filename.endswith(ext) for ext in SUPPORTED_MODEL_EXTENSIONS)