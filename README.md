# FACMIC
Anonymous

Run main.py to reproduce our results. (You have to divide the data into four sub folders: client_1, client_2, client_3 and client_4.

For convenience, you can use data_split.py to split any dataset into any sub folders as you like.

## Requirements

We suggest you to use the following packages:

clip==1.0

numpy==1.22.0

opencv-python==4.5.4.60

openpyxl==3.0.5

Pillow==9.3.0

scikit-image==0.17.2

scikit-learn==0.23.2

scipy==1.10.0

tqdm==4.62.3

torch==1.13.1+cu117

torchvision=0.14.1+cu117

## How to use

### main.py 

Run main.py to reproduce our results.

For FACMIC and FedCLIP, you have to set arser.add_argument('--aggmode', type=str, default='avg') default as 'att';

For other methods, you have to set arser.add_argument('--aggmode', type=str, default='avg') default as 'avg'.

parser.add_argument('--test_envs', type=int, nargs='+', default=[1]) # default here is to set the global testing set, suppose there are 4 Clients, 1 here means it will treat Client 2 as the global while the rest as training clients.

For optimizer, for FACMIC and FedCLIP, you have to use optimizers = [optim.Adam(params=[{'params': models[idx].fea_attn.parameters()}], lr=args.lr, betas=(args.beta1, args.beta2), eps=args.eps, weight_decay=args.weight_decay) for idx in range(client_num)];

For FedAVG, MOON and FedProx, you have to use optimizers = [optim.Adam(params=[{'params': models[idx].parameters()}], lr=args.lr, betas=(
        args.beta1, args.beta2), eps=args.eps, weight_decay=args.weight_decay) for idx in range(client_num)].

### adaptation.py

adaptation.py is the domain adaptation technique. You have to change the classes in Line 64: self.num_class = 7 (For Real is 7, for BT is 4).

### nets/models.py

models.py is the model backbone file. In Line 46, you have to change attention module if you want to test FedCLIP( just comment Line 47-48, use Line 51-52)

### utils/clip_util.py

clip_util.py is the utils that CLIP will use. For FedAVG, MOON and FedProx, you have to set Line 23 True, For FACMIC and FedCLIP, you have to set it as False.

### utils/prepare_data_dg_clip.py

prepare_data_dg_clip.py is the dataloader CLIP will use. You can define the percentage for training, val and test in Line 97.


### utils/training.py

training.py is the training function for all methods. For SC and BT dataset, you have to use the following statement:

if i == args.n_iter:

    break

This can ensure the funciton will stop in right way. We marked these sentences in Line 32-33, Line 82-83, 124-125, Line 160-161, Line 211-212 and Line 241-242. Besides, you have to change train(args, model, train_test_loaders[client_idx], optimizers[client_idx], device, test_train[0], mmd_loss, server_model_pre, previous_nets[client_idx]) into train(args, model, train_loaders[client_idx], optimizers[client_idx], device, test_train[0], mmd_loss, server_model_pre, previous_nets[client_idx]) in main.py. Only for Real dataset, you have to use train_test_loaders[client_idx], and comment these statements mentioned above (e.g., Line 32-33).

