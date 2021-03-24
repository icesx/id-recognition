from dataset.image_file import *


class DatasetCreator:

    def __init__(self, image_x=64, image_y=64):
        self.__image_x = image_x
        self.__image_y = image_y
        self.__ds = None

    def load(self, root, is_val=False):
        return self.__create_dataset(root, is_val)

    def batch(self, batch):
        return self.__ds.batch(batch)

    def shuffle_and_repeat(self):
        self.__ds = self.__ds.apply(tf.data.experimental.shuffle_and_repeat(buffer_size=1024))
        return self

    def augment(self, augment):
        if augment is True:
            pass
            # self.__ds = self.__ds.concatenate(self.__ds.map(flip_up_down))
            # self.__ds = self.__ds.concatenate(self.__ds.map(random_brightness))
            # self.__ds = self.__ds.concatenate(self.__ds.map(flip_left_right))
            # self.__ds = self.__ds.concatenate(self.__ds.map(central_crop))
        return self.__ds

    def __load_and_preprocess_from_path_label(self, path):
        return image_byte_array(path, self.__image_x, self.__image_y)

    def __create_dataset(self, root, is_val):
        image_infos = image_labels(root)
        path_ds = tf.data.Dataset.from_tensor_slices([ii.path_str for ii in image_infos])
        image_ds = path_ds.map(self.__load_and_preprocess_from_path_label)
        label_ds = tf.data.Dataset.from_tensor_slices(
            tf.cast([ii.label_info.label_idx for ii in image_infos], tf.int64))
        self.__ds = tf.data.Dataset.zip((image_ds, label_ds))
        cache_name = "val" if is_val is True else "train"
        self.__ds = self.__ds.cache()
        return self


if __name__ == '__main__':
    dataset_creator = DatasetCreator().load('/WORK/datasset/mnist/train')
    ds = dataset_creator.batch(15)
    # for element in ds:
    #     print(element)
    sample = dataset_creator.take_sample(0.001)
    for element in sample:
        print(element)
    for lable, label_info in ALL_LABELS.items():
        print(lable, label_info.label_idx)
