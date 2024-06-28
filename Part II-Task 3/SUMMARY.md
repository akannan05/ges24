# Task III: Synthetic Data Generation

## Approach

- We approached the Synthetic Data Generation portion of this project using a CTGAN (Conditional GAN for Tabular Data). The conditional GAN works like a regular GAN in the sense that it has a generator network to generate synthetic data based on noise, and a discriminator network to differentiate between real and fake data. The idea is the generator gets good enough that the discriminator is very inaccurate. The conditional GAN is a version of this regular GAN but it is conditioned on a certain data format, which allows for more precise, accurate, and strong predictions.

- Due to the conditional nature of the GAN, one must specify the discrete and continuous columns in the dataset. In this case, we only set the label as a discrete variable as discrete variables take more storage (we can round the synthetic data to get discrete features). We also had to only take a sample of 50,000 observations from the data to train the GAN with, as any more data would cause memory issues.

- After the synthetic data was generated we plotted histograms of each variable in the original and synthetic dataframes respectively to assess if there were any distributional differences and to see whether or not the fake data distributions mapped the real data distributions.

  
![image](https://github.com/akannan05/ges24/assets/70667502/9731f80c-1e2f-4e48-929f-2f82092cee03)![Real Histograms](https://github.com/akannan05/ges24/assets/70667502/1e8c7c3d-4479-4b8e-a1ba-a1b9d5ae6e25)

