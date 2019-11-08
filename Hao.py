# 作者：hao.ren3
# 时间：2019/11/8 18:28
# IDE：PyCharm
from pandas import read_csv, DataFrame
from numpy import shape

# 获取数据
def get_original_data():
    iris = read_csv('iris.csv', header=None)
    iris.columns = ['sepal_length', 'sepal_width',
                    'petal_length', 'petal_width', 'target_class']
    iris = iris[['sepal_length', 'target_class']]
    return iris


# 獲取各個枚舉值的各個標簽樣本量
def get_nb_target_number_by_value(inside_data):
    list_unique_value = list(set(inside_data['sepal_length'].values))
    list_unique_value = sorted(list_unique_value, reverse=False)
    list_setosa, list_versicolor, list_virginica = [], [], []
    for current_value in list_unique_value:
        temp_data = inside_data[inside_data['sepal_length'] == current_value]
        list_setosa.append(len(temp_data[temp_data['target_class'] == 'Iris-setosa']))
        list_versicolor.append(len(temp_data[temp_data['target_class'] == 'Iris-versicolor']))
        list_virginica.append(len(temp_data[temp_data['target_class'] == 'Iris-virginica']))
    inside_result = DataFrame({
        'value': list_unique_value,
        'setosa': list_setosa,
        'versicolor': list_versicolor,
        'virginica': list_virginica
    })
    return inside_result


def calculate_chi_squared(inside_data):
    print(inside_data)

if __name__ == '__main__':
    data = get_original_data()
    data = get_nb_target_number_by_value(data)



    print(data)