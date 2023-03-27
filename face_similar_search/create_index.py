import os
from annoy import AnnoyIndex

from config import DIMENTION, METRIC, N_TREES, INDEX_PATH
from processing import extract_encoding


def create_index(target_path: str):
    index = AnnoyIndex(DIMENTION, METRIC)
    
    # target_pathにある画像を読み込んで特徴量をannoyのindexとして保存する。
    target_files = os.listdir(target_path)
    for i, target_file in enumerate(target_files):
        target_file_path = os.path.join(target_path, target_file)
        face_encoding = extract_encoding(target_file_path)
        if face_encoding is not None:
            index.add_item(i, face_encoding)

    # 最適化
    index.build(N_TREES)

    # 保存
    index.save(INDEX_PATH)


if __name__ == "__main__":
    target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static/target"))
    create_index(target_path)
