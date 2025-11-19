import logging
import asyncio
from typing import Any, Dict, Optional, Tuple
from om1.core.input import InputPlugin, InputType

logger = logging.getLogger(__name__)

class DummySensorPlugin(InputPlugin):
    """
    A dummy sensor plugin to demonstrate the integration of new sensors (Closes #365).
    This plugin simulates a simple image capture.
    """
    
    # REQUIRED: Tên plugin
    plugin_name = "dummy_sensor"

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        # Ví dụ: đọc cấu hình từ file .json
        self.interval = config.get("interval", 5)  # Giả lập chụp sau mỗi 5 giây
        logger.info(f"Dummy Sensor initialized with interval: {self.interval}s")

    async def initialize(self) -> None:
        # Code khởi tạo (nếu cần thiết)
        pass

    async def get_input(self) -> Optional[Tuple[InputType, Any]]:
        """
        Main function to periodically check for new sensor data and return it.
        """
        # Giả lập đọc dữ liệu sau mỗi interval
        await asyncio.sleep(self.interval)
        
        # Giả lập trả về một tin nhắn văn bản
        dummy_data = "Dummy sensor reports: Movement detected at the virtual camera."
        logger.info(f"Dummy Sensor captured data: {dummy_data}")

        # Trả về dữ liệu ở định dạng tiêu chuẩn của OM1: (InputType.TEXT, data)
        return InputType.TEXT, dummy_data

    async def shutdown(self) -> None:
        # Code dọn dẹp (nếu cần)
        logger.info("Dummy Sensor shutting down.")
