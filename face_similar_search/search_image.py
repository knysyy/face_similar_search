import os
from annoy import AnnoyIndex

from config import DIMENTION, METRIC, INDEX_PATH
from processing import extract_encoding


def search_image(target_file_path: str, number_of_image: int):
    # annoyのindexを読み込む。
    index = AnnoyIndex(DIMENTION, METRIC)
    index.load(INDEX_PATH)

    # 対象の画像の特徴量を取得する。
    face_encoding = extract_encoding(target_file_path)
    if face_encoding is None:
        return None

    # 類似順に5件取得する。
    return index.get_nns_by_vector(face_encoding, number_of_image)


if __name__ == "__main__":
    target_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'query', 'query.jpg'))
    neighbors = search_image(target_file_path, 5)
    # 仮でos.listdirの順番でidを振っているので実際は画像にidを付与しそちらを利用する想定。
    raw_files = os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static/target")))
    # 画像ファイル名を出力する。
    for neighbor in neighbors:
        print(raw_files[neighbor])
