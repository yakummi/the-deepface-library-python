from deepface import DeepFace
import json

def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        with open('result.json', 'w') as f:
            json.dump(result_dict, f, indent=4, ensure_ascii=False)

        # return result_dict

        if result_dict.get('verified'):
            return 'Проверка пройдена. Пропустить.'
        return 'Нарушитель! Задержать!!'

    except Exception as _ex:
        return _ex


def face_recogn():
    try:
        result = DeepFace.find(img_path='<Путь вашей img>', db_path='<Сохранение (куда?)>')
        result = result.values.tolist()

        return result

    except Exception as _ex:
        return _ex


def face_analyze():
    try:
        result_dict = DeepFace.analyze(img_path='<Ваш jpg>', actions=['age', 'gender', 'race', 'emotion'])

        with open('face_analyze.json', 'w') as f:
            json.dump(result_dict, f, indent=4, ensure_ascii=False)

        print(f'[+] Age: {result_dict.get("age")}')
        print(f'[+] Gender: {result_dict.get("gender")}')
        print(f'[+] Race: ')

        for k, v in result_dict.get('race').items():
            print(f'{k} - {round(v, 2)}%')

        print(f'[+] Emotions: ')
        for k, v in result_dict.get('emotion').items():
            print(f'{k} - {round(v, 2)}%')
    except Exception as _ex:
        return _ex

def main():
    # print(face_verify(img_1='dzhejmi-dornan.jpg', img_2='1651716779170925137.jpg'))
    # print(face_recogn())
    face_analyze()
if __name__ == '__main__':
    main()