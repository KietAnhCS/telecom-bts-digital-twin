"""
Pipeline: kiểm tra máy -> dữ liệu -> train -> submission -> báo cáo -> tải về .
Notebook chỉ gọi các hàm ở đây , mọi logic năm trong module .py này 
"""

from pipeline.config import Config
from pipeline.env import check_gpu, free_memory, install_dependencies, mem, show_mem

__all__ = ["config", "check_gpu", "free_memory","install_dependencies","mem","show_mem"]