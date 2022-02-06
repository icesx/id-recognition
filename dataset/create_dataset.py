from dataset.dataset_sample import take_sample
from dataset.image_file import *


class DatasetCreator:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__ds = None

    def load(self, root):
        return self.__create_dataset(root)

    def batch(self, batch):
        return self.__ds.batch(batch)

    def shuffle_and_repeat(self):
        self.__ds = self.__ds.apply(tf.data.experimental.shuffle_and_repeat(buffer_size=1024))
        return self

    def __load_and_preprocess_from_path_label(self, path):
        return image_byte_array(path, self.__height, self.__width)

    def __create_dataset(self, root):
        image_infos = image_labels(root)
        path_ds = tf.data.Dataset.from_tensor_slices([ii.path_str for ii in image_infos])
        image_ds = path_ds.map(self.__load_and_preprocess_from_path_label)
        label_ds = tf.data.Dataset.from_tensor_slices(
            tf.cast([ii.label_vector for ii in image_infos], tf.int64))
        self.__ds = tf.data.Dataset.zip((image_ds, label_ds))
        self.__ds = self.__ds
        return self


if __name__ == '__main__':
    dataset_creator = DatasetCreator().load('/OTHER/dataset/id_card/train')
    # for element in ds:
    #     print(element)
    sample = take_sample(dataset_creator.batch(15), 0.001)
    for element in sample:
        print(element)
