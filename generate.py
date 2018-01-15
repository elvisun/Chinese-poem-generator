import numpy as np
from main import Generator

def main():
    f = open('./output.txt', 'w', encoding='utf-8')

    input_char = '卢本伟挂逼凉凉送给你'
    model = Generator()
    model.build_model()

    for diversity in np.linspace(0.2, 3.0, num = 10):
        print(diversity)
        output = model.predict(input_char, diversity = diversity)
        f.write('\n')
        #f.write("\n------------Diversity {}--------------\n".format(diversity))
        f.write(output)
        f.flush()

if __name__ == '__main__':
    main()
