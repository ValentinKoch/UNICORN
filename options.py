import argparse


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # logging options
        self.parser.add_argument('--config_file', default='/transformer.yaml', type=str, help='path to config file')
        self.parser.add_argument('--save_dir', type=str, help='path to save models, outputs, and folds')
        self.parser.add_argument('--project', type=str, help='wandb project name')
        self.parser.add_argument('--name', type=str, help='costum prefix for logging')
        
        # task definition
        self.parser.add_argument('--task', type=str, help='training task in [binary, multiclass, multilabel]')
        self.parser.add_argument('--target', type=str, help='targets used for training')
        self.parser.add_argument('--cohorts', nargs='+', type=str, help='cohort used for training')
        self.parser.add_argument('--ext_cohorts', nargs='+', type=str, help='cohort used for external validation')
        self.parser.add_argument('--clini_info', type=bool, help='whether to use clinical information during training')
        self.parser.add_argument('--seed', type=int, help='random state for splitting the data')
        
        # model options
        self.parser.add_argument('--model', type=str, help='costum prefix for logging')
        self.parser.add_argument('--norm', type=str, help='type of pre-processing')
        self.parser.add_argument('--feats', type=str, help='type of features ')
        self.parser.add_argument('--num_tiles', type=int, help='number of tiles to sample from all tiles')    
        self.parser.add_argument('--pad_tiles', type=bool, help='whether to pad the tiles up to num_tiles if #tiles is smaller than num_tiles')
        
        # training options
        self.parser.add_argument('--folds', type=int, help='number of folds')
        self.parser.add_argument('--num_epochs', type=int, help='number of epochs')
        self.parser.add_argument('--optimizer', type=str, help='optimizer for model training')
        self.parser.add_argument('--scheduler', type=str, help='scheduler for model training')
        self.parser.add_argument('--lr', type=float, help='learning rate')
        self.parser.add_argument('--wd', type=float, help='weight decay')
        self.parser.add_argument('--bs', type=int, help='batch size during training')
        self.parser.add_argument('--stop_criterion', type=str, help='metric for choosing best model')
        self.parser.add_argument('--resume', type=str, help='path to trained model for evaluation')

        self.parser.add_argument('--debug', type=bool, help='debug flag, turns off login etc.')

    def parse(self):
        self.opt = self.parser.parse_args()
        args = vars(self.opt)

        return self.opt
