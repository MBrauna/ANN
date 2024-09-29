import numpy as np

class OneLayer:
    __ADJUST_POINTS = []
    __ENTRY_DATA = []

    def __init__(self, data) -> None:
        try:
            self.__ENTRY_DATA = data
            self.__ADJUST_POINTS = np.random.rand(len(self.__ENTRY_DATA))
        except:
            raise Exception("[__INIT__] Failed when create entry data")

    def sum_function(self) -> float:
        result = 0.00
        for idx, registry in enumerate(self.__ENTRY_DATA):
            result += ((registry*idx) * (self.__ADJUST_POINTS[idx]*idx))
        return result
    
    def step_function(self, data) -> bool:
        if(data > 0):
            return True
        return False

    def get_points(self) -> list:
        return self.__ADJUST_POINTS



if __name__ == "__main__":
    entry_data = [0, 0, 1, 5, 29, 25]
    ann = OneLayer(entry_data)
    layer = ann.sum_function()
    step = ann.step_function(layer)

    print("============= [FUNÇÃO SOMA] ================")
    print("Pesos: {}".format(ann.get_points()))
    print("Soma: {}".format(layer))
    print("Step: {}".format(step))

