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
    
# def get_base_cache_dir():
#     """Get or create the model cache directory (优先使用配置路径)"""
#     try:
#         import folder_paths
#         # 尝试从配置中获取路径（此时 SEEDVR2_MODEL_TYPE 已改为 "SEEDVR2"）
#         config_paths = folder_paths.get_folder_paths(SEEDVR2_MODEL_TYPE)
#         if config_paths:  # 如果配置中有路径，优先使用第一个
#             cache_dir = config_paths[0]
#         else:  # 配置中没有时，才使用默认路径
#             cache_dir = os.path.join(folder_paths.models_dir, SEEDVR2_FOLDER_NAME)
#             folder_paths.add_model_folder_path(SEEDVR2_MODEL_TYPE, cache_dir)
#     except:
#         # 未在 ComfyUI 环境中时的 fallback
#         cache_dir = f"./{SEEDVR2_MODEL_TYPE}_models"
#     
#     os.makedirs(cache_dir, exist_ok=True)
#     return cache_dir
    
def get_base_cache_dir() -> str:
    """Get or create the model cache directory with priority to local models"""
    try:
        import folder_paths  # 导入ComfyUI的路径处理模块
        
        # 1. 优先检查本地models/SEEDVR2路径
        local_model_dir = os.path.join(folder_paths.models_dir, SEEDVR2_FOLDER_NAME)
        
        # 检查路径是否存在且包含模型文件
        if os.path.exists(local_model_dir) and len(os.listdir(local_model_dir)) > 0:
            folder_paths.add_model_folder_path(SEEDVR2_MODEL_TYPE, local_model_dir)
            return local_model_dir
        
        # 2. 本地路径不存在时，尝试读取配置文件
        config_paths = folder_paths.get_folder_paths(SEEDVR2_MODEL_TYPE)
        if config_paths and len(config_paths) > 0:
            # 优先使用配置中的第一个路径
            configured_dir = config_paths[0]
            if os.path.exists(configured_dir):
                return configured_dir
        
        # 3. 所有路径都无效时，创建默认本地路径
        folder_paths.add_model_folder_path(SEEDVR2_MODEL_TYPE, local_model_dir)
        os.makedirs(local_model_dir, exist_ok=True)
        return local_model_dir
        
    except ImportError:
        # 未安装ComfyUI环境时的 fallback
        default_dir = f"./{SEEDVR2_MODEL_TYPE}_models"
        os.makedirs(default_dir, exist_ok=True)
        return default_dir
    except Exception as e:
        print(f"获取模型路径时出错: {str(e)}")
        # 出错时的安全 fallback
        default_dir = os.path.join("models", SEEDVR2_FOLDER_NAME)
        os.makedirs(default_dir, exist_ok=True)
        return default_dir
    
def is_supported_model_file(filename: str) -> bool:
    """Check if a file has a supported model extension"""
    return any(filename.endswith(ext) for ext in SUPPORTED_MODEL_EXTENSIONS)