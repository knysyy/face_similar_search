import face_recognition


def extract_encoding(target_image_path: str):
    target_image = face_recognition.load_image_file(target_image_path)
    face_encodings = face_recognition.face_encodings(target_image)
    if len(face_encodings) == 0:
        return None
    return face_encodings[0]
