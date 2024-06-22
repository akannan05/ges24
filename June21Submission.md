# June 21 Submission for Mercury Codes

We are running into some hardware issues with memory and disk space so we weren't able to fully implement our synthetic data generation model before this first deadline.

Instead, we have put all the notebooks we are using so far in the repo. Below, we also explain our plans in the next week and our approach to the project as a whole.

We hope that this will give the judges a good overview of our implementation for this hackathon, even though we don't have the full thing working yet.

## Data Clean Room

We are planning on using an Intel TDX CPU Technology in a Virtual Machine with Azure to implement the data clean room. We are currently in the process of purchasing this.

However, we did try running the TPM encoding tutorial in a virtual machine using Virtual Box. This worked up to the point of sending the .ak files back to the host, which it couldn't do properly.

Our goal in the final week of the hackathon is to get the Intel TDX technology and implement the Data Clean Room to run with out models. 


## Aggregate Statistics

We have also included a notebook with functions to calculate and plot aggregate statistics to model the demographic distributions of potential customers.

We also plan to create histograms for each variable to check dataset distribution and ensure that the synthetic data generator performs well.


## Synthetic Data Generation    

The main issue that we were stuck on this week that prevented us from fully implementing the generative model was running into memory issues with merging the dataframes.

We believe this is because the dataframes are pretty large in size (3 million entries and 7 million entries). Even with using dask and partitioning the dataframes we were unable to properly merge the dfs.

In this submission we have included the CTGAN prototype to generate synthetic tabular data. We tested this model on a tips dataset and calculated some accuracy metrics to ensure strong performance.

## Predictive Model

We plan to feed the merged dataset into a random forest model in order to solve the binary classification problem of identifying potential customers.

If the random forest model doesn't work well after hyperparameter tuning, we plan to try a gradient boosting algorithm or neural network based approach.
