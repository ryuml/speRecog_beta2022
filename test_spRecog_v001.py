#coding: utf-8

import speech_recognition as sr

def main():
    r = sr.Recognizer()
    recog_texts = []
    encodeed_texts = []
    dec_type = "shift_jis"
    enc_type = "utf-8"
    exit_flag = False
    flag_text = 'n'
    output_file_name = "output.txt"

    with sr.Microphone() as source:
        while (not(exit_flag)):
            r.adjust_for_ambient_noise(source)
            print("=== 何か、話しかけてください ===")
            audio = r.listen(source)
            print("[o] ===> オーディオGET")
            print("=== Google Speech Recognition - 音声解析中 ===")
            try:
                text = r.recognize_google(audio, language='ja-JP')
                print("You said : " + text)
            except Exception:
                print("[-- Error --] Google Speech Recognition Error.")
            recog_texts.append(text + '\n')

            flag_text = input(">>> 終了しますか？ [y / n]:")
            if (flag_text == 'y'):
                exit_flag = True

    for recog_text in recog_texts:
        try:
            recog_text = recog_text.encode(enc_type)
            encodeed_texts.append(recog_text)
        except Exception:
            print("[-- Error --] Text decode-encode Error.")
            quit()

    with open(output_file_name, 'wb') as f_txt:
        f_txt.writelines(encodeed_texts)

if __name__ == "__main__":
    main()

