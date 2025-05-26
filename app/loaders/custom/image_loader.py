import os
from typing import List, Dict, Any, Union
from app.loaders.base_loader import BaseLoader, Document, LoaderException
from app.tools.registry import get_tool

tool = get_tool("ImageDownloaderTool")

class ImageLoader(BaseLoader):
    """
    Loader untuk mengunduh gambar dari URL dan mengembalikan dokumen dengan metadata path lokal.
    """

    def __init__(self, save_dir: str = "output/image"):
        self.downloader = tool(save_dir=save_dir)

    def load(self, source: Union[str, os.PathLike], **kwargs) -> List[Document]:
        """
        Mengunduh satu gambar dari URL dan mengembalikan sebagai dokumen.
        Args:
            source (str): URL gambar.
        Returns:
            List[Document]: List berisi satu dokumen dengan path lokal gambar dan metadata.
        """
        try:
            local_path = self.downloader.download(str(source))
            doc: Document = {
                "content": local_path,
                "metadata": {
                    "source_url": str(source),
                    "local_path": local_path
                }
            }
            return [doc]
        except Exception as e:
            raise LoaderException(f"Failed to load image from {source}: {e}")

    def load_all(self, sources: List[Union[str, os.PathLike]], **kwargs) -> List[Document]:
        """
        Mengunduh banyak gambar dari daftar URL.
        Args:
            sources (List[str]): Daftar URL gambar.
        Returns:
            List[Document]: List dokumen untuk semua gambar.
        """
        results = []
        for src in sources:
            try:
                results.extend(self.load(src))
            except Exception as e:
                # Bisa log error di sini jika perlu
                continue
        return results