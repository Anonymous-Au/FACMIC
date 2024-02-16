import os
import shutil
import numpy as np


def count_files(directory):
    count = 0
    for root, _, files in os.walk(directory):
        count += len(files)
    return count


def create_dir_structure(base_dir, N):
    for i in range(N):
        new_dir = os.path.join(base_dir, f"client_{i}")
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        # for root, dirs, _ in os.walk(base_dir):
        #     if root != base_dir:
        #         continue
        #     for dir in dirs:
        #         new_sub_dir = os.path.join(new_dir, dir)
        #         if not os.path.exists(new_sub_dir):
        #             os.makedirs(new_sub_dir)


def dirichlet_distribution(alpha, N):
    return np.random.dirichlet(alpha * np.ones(N))


def distribute_files(base_dir, save_dir, N, total_files):
    # alpha = 0.6
    # dirichlet_samples = dirichlet_distribution(alpha, N)
    # print(dirichlet_samples)
    # dirichlet_samples = [0.51451878, 0.14796481, 0.33138751641]
    dirichlet_samples = [0.8, 0.2]
    # dirichlet_samples = [0.09358517, 0.61603834, 0.29037648]
    # dirichlet_samples = [0.17181574, 0.21687307, 0.61131118]
    # dirichlet_samples = [0.3333333,0.33333333,0.333333333]
    # file_indices = np.arange(total_files)
    # np.random.shuffle(file_indices)
    # print(file_indices, file_indices.shape)
    # print(dirichlet_samples, dirichlet_samples.shape)
    current_index = 0
    # length = [826, 822, 395, 827]
    # length = [1321, 1339, 1595, 1457]
    # length = [4674, 6528, 12800, 11200]
    length = [867, 3323, 239, 4522,12875,2624,253]
    for i in range(N):
        k = 0
        target_dir = os.path.join(save_dir, f"client_{i}/")
        # files_to_copy = int(dirichlet_samples[i] * total_files)
        for root, _, files in os.walk(base_dir):
            current_index = 0
            if root == base_dir:
                continue
            print('Class length is :', len(files))
            file_indices = np.arange(len(files))
            np.random.shuffle(file_indices)
            # print(file_indices, file_indices.shape)
            # dirichlet_samples = dirichlet_distribution(alpha, N)
            files_to_copy = int(dirichlet_samples[i] * length[k])
            k +=1
            print(files_to_copy)
            for _ in range(files_to_copy):
                file_to_copy = files[file_indices[current_index]]
                src_file_path = os.path.join(root, file_to_copy)
                dst_file_path = src_file_path.replace(save_dir, target_dir)
                root_path = root
                base_path = "train"
                root_index = root_path.find(base_path)
                root_path = root_path[root_index:]
                s_d = save_dir
                class_path = root_path.replace(root_path, target_dir)
                c_p = os.path.join(class_path, root_path)
                if not os.path.exists(c_p):
                    os.makedirs(c_p)
                print(root, root_path, c_p, class_path, src_file_path, dst_file_path)
                # dst_file_path = os.path.join(target_dir, )
                shutil.move(src_file_path, c_p)
                current_index += 1


base_dir = "./data/RealSkin/client_1/train"
save_dir = "./data/RealSkin/client_1"
N = 2

total_files = count_files(base_dir)
print(total_files)
create_dir_structure(save_dir, N)
distribute_files(base_dir, save_dir, N, total_files)
