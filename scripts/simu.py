import os

from experiments.expsimu import Expsimu


def adolescent():
    conv_kernel = [12, 16]
    decomp_kernel = []
    isometric_kernel = []
    seq_len = 672
    # TODO
    for ii in conv_kernel:
        if ii % 2 == 0:  # the kernel of decomposition operation must be odd
            decomp_kernel.append(ii + 1)
            isometric_kernel.append((seq_len + ii) // ii)
        else:
            decomp_kernel.append(ii)
            isometric_kernel.append((seq_len + ii - 1) // ii)

    exp = Expsimu(model='ykw', num_hidden=16, learning_rate=0.01, seq_len=672, classes=7, in_features=1, freq='min', lgf_layers=1,
                  conv_kernel=conv_kernel, decomp_kernel=decomp_kernel, isometric_kernel=isometric_kernel,
                  seed=2024, subject='adolescent', dataset_dir=os.path.join('.', 'datasets', 'TrainSet'))
    exp.train()

def rnn():
    exp = Expsimu(model='rnn', num_hidden=32, learning_rate=0.01, classes=7, in_features=1,
                  seed=2024, subject='adolescent', dataset_dir=os.path.join('.', 'datasets', 'TrainSet'))
    exp.train()
