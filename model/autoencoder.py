import torch
import torch.nn as nn


# LSTM() returns tuple of (tensor, (recurrent state))
class extract_tensor(nn.Module):
    def forward(self, x):
        tensor, _ = x
        return tensor


class TimeSeriesAutoencoder(nn.Module):
    def __init__(self, input_size, embed_size, latent_size, time_feature_size):
        super(TimeSeriesAutoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.LSTM(input_size+time_feature_size, embed_size, batch_first=True),
            extract_tensor(),
            nn.Linear(embed_size, latent_size)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_size, embed_size),
            nn.LSTM(embed_size, input_size, batch_first=True)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded, _ = self.decoder(encoded)
        return decoded

