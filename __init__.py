"""
SeedVR2 Video Upscaler - Transition progressive vers architecture modulaire

Ce fichier gère la transition entre:
- Ancien code monolithique (seedvr2.py)
- Nouvelle architecture modulaire (src/)

Migration en cours...
"""

"""
# 在 F:\ComfyUI-aki-v1.3-0\custom_nodes\ComfyUI-SeedVR2_VideoUpscaler\__init__.py 最顶部添加
import sys
from pathlib import Path

# 1. 打印当前节点根目录（确认路径是否正确）
NODE_ROOT = Path(__file__).parent.resolve()
print(f"[SeedVR2 Debug] 节点根目录：{NODE_ROOT}")

# 2. 打印当前 sys.path（确认路径是否已加入）
print(f"[SeedVR2 Debug] sys.path 中是否包含节点根目录：{str(NODE_ROOT) in sys.path}")
print(f"[SeedVR2 Debug] 当前 sys.path 前 5 项：{sys.path[:5]}")

# 3. 手动添加路径（确保在导入 src 前执行）
if str(NODE_ROOT) not in sys.path:
    sys.path.insert(0, str(NODE_ROOT))
    print(f"[SeedVR2 Debug] 已手动添加路径到 sys.path：{str(NODE_ROOT)}")
# 验证路径是否未被删除（在导入 src 前再次检查）
assert str(NODE_ROOT) in sys.path, f"[SeedVR2 Error] 路径 {NODE_ROOT} 被意外移除！"

# 关键：先移除可能已存在的路径（避免重复），再插入到最前面
if str(NODE_ROOT) in sys.path:
    sys.path.remove(str(NODE_ROOT))
sys.path.insert(0, str(NODE_ROOT))  # 强制放在sys.path[0]

# 再次验证路径是否在最前面
print(f"[SeedVR2 Debug] 修正后 sys.path[0]：{sys.path[0]}")  # 应显示你的节点目录

# 4. 尝试单独导入 src（验证是否能找到包）
try:
    import src
    print(f"[SeedVR2 Debug] 成功导入 src 包，src 路径：{src.__path__}")
except Exception as e:
    print(f"[SeedVR2 Debug] 导入 src 失败：{type(e).__name__}: {e}")

# 后续原有代码...
"""   

# 🆕 TENTATIVE: Nouvelle architecture modulaire
from .src.interfaces.comfyui_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
USING_MODULAR = True


# Export pour ComfyUI
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# Métadonnées
__version__ = "1.5.0-transition" if not USING_MODULAR else "2.0.0-modular"
