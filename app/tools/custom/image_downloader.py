# app/tools/custom/image_downloader.py

import os
import requests
import hashlib
from urllib.parse import urlparse
from app.tools.base_tool import BaseTool

class ImageDownloaderTool(BaseTool):
    """
    Tool untuk mengunduh gambar dari URL dan menyimpannya ke direktori lokal.
    Return: dict berisi path gambar.
    """

    def __init__(self, save_dir: str = "app/static/output/image", **kwargs):
        """
        Inisialisasi dengan direktori penyimpanan default.
        """
        super().__init__(
            name="ImageDownloaderTool",
            host=None,
            save_dir=save_dir,
            **kwargs
        )
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

    def _safe_filename(self, image_url: str) -> str:
        """
        Generate a safe, short filename from the image URL using md5 hash.
        """
        path = urlparse(image_url).path
        ext = os.path.splitext(path)[-1].lower()
        # Only allow image extensions, otherwise default to .png
        allowed_exts = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
        if ext not in allowed_exts:
            ext = ".png"
        hashname = hashlib.md5(image_url.encode()).hexdigest()
        return f"{hashname}{ext}"

    def download(self, image_url: str, filename: str = None) -> str:
        """
        Wrapper untuk memanggil execute dan mengembalikan path file gambar.
        """
        if not filename:
            filename = self._safe_filename(image_url)
        result = self.execute(image_url, filename)
        return result["content"]

    def execute(self, image_url: str, filename: str = None) -> dict:
        """
        Jalankan proses download gambar.
        """
        if not filename:
            filename = self._safe_filename(image_url)

        save_path = os.path.abspath(os.path.join(self.save_dir, filename))
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Pastikan direktori ada

        try:
            response = requests.get(image_url, stream=True, timeout=15)
            response.raise_for_status()

            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            self.logger.info(f"Image downloaded successfully to {save_path}")

            # Convert absolute path to relative path for web access
            rel_path = save_path.replace("\\", "/")
            idx = rel_path.find("/static/")
            if idx != -1:
                rel_path = rel_path[idx:]  # '/static/output/image/xxx.jpg'
            else:
                rel_path = None

            return {"content": rel_path}

        except Exception as e:
            self.logger.error(f"Gagal mengunduh gambar dari {image_url}: {e}", exc_info=True)
            raise Exception(f"Failed to download image: {image_url}\nReason: {e}")