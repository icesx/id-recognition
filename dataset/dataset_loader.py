from dataset.image_file import *
from model.model_define import IdModelDefine


class DatasetLoader:

    def __init__(self, md: ModelDefine):
        self.__md = md
        self.__height = md.image_height()
        self.__width = md.image_width()
        self.__ds = None
        self.__base_ds = None

    def base_ds(self):
        return self.__base_ds

    def load(self, root):
        return self.__create_dataset(root)

    def batch(self, batch):
        return self.__ds.batch(batch)

    def shuffle_and_repeat(self):
        self.__ds = self.__ds.apply(tf.data.experimental.shuffle_and_repeat(buffer_size=1024))
        return self

    def __load_and_preprocess_from_path_label(self, path):
        return image_byte_array(path, self.__md)

    def __create_dataset(self, root):
        image_infos = image_labels(root, self.__md)
        path_ds = tf.data.Dataset.from_tensor_slices([ii.path_str for ii in image_infos])
        image_ds = path_ds.map(self.__load_and_preprocess_from_path_label)
        label_ds = tf.data.Dataset.from_tensor_slices(
            tf.cast([ii.label_vector for ii in image_infos], tf.int64))
        self.__ds = tf.data.Dataset.zip((image_ds, label_ds))
        self.__ds = self.__ds
        self.__base_ds = self.__ds
        return self

    def take(self, count=10):
        return self.__ds.take(count)


if __name__ == '__main__':
    dataset_creator = DatasetLoader(IdModelDefine()).load('/OTHER/dataset/id_card/train')
    # for element in dataset_creator.sample():
    #     print("image:" + str(element[0]))
    #     print("label:" + str(element[1]))
    for i in dataset_creator.take(1).as_numpy_iterator():
        print("image:" + str(i[0]))
        print("label:" + str(i[1]))
