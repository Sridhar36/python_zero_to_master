from translate import Translator

translator = Translator(to_lang='ja')

file_path = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\zero_to_master_complete_python_2022\\11_file_i_o\\test_file'
file_path2 = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\zero_to_master_complete_python_2022\\11_file_i_o\\test_file2'

try:
    with open(file_path, 'r') as file:
        text = file.read()
        translation = translator.translate(text)
        with open(file_path2, mode='w') as file2:
            file2.write(translation)
except Exception as err:
    print(err)
