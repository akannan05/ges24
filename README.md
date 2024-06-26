# User Engagement Forecasting

<table align="center"> 
  <tr>
    <td style="padding: 0 35px;">
      <img src="assets/image1.png" alt="Animesh" style="width: 100%;">
      <p align="center">Animesh</p>
    </td>
    <td style="padding: 0 35px;">
      <img src="assets/image4.png" alt="Anirudh" style="width: 100%;">
      <p align="center">Anirudh</p>
    </td>
    <td style="padding: 0 35px;">
        <img src="assets/image2.png" alt="Brandon" style="width: 100%;">
      <p align="center">Brandon</p>
    </td>
    <td style="padding: 0 35px;">
      <img src="assets/image3.png" alt="Eli" style="width: 100%;">
      <p align="center">Eli</p>
    </td>
  </tr>
</table>

# Our General Approach 

## Data Clean Room

The full source code and summary is here: [Data Clean Room Task](https://github.com/akannan05/ges24/blob/main/Part%20I%20-%20DCR/SUMMARY.md)

We simply followed the instructions given in the prompt release as well as the TPM coding handout. 

We chose to use the Intel SGX (Software Guard Extensions), which prove hardware-level protection against privacy risks. While we were considering using some software solutions, such as Docker, we came to the conclusion that hardware protections would suffice. 

Our general structure was to use a Azure Virtual Machine with the Intel SGX capability. Then we have a separate resource called a Key Vault to save the public key's AK (Attestation Key). 

## Aggregate Statistics

The full visualizations and data analysis report is here: [Aggregate Statistics Task](https://github.com/akannan05/ges24/blob/main/Part%20II-Task%201/SUMMARY.md)

After merging and preprocessing the data, we used Pandas and Plotly to visualize the distributions and make statistical inferences. In addition to the given prompts, we also analyzed:
- User Likes and Dislikes
- Progress In Article

From the statistical analysis, our conclusion was that the most important attribute that differentiates Potential Customers vs. Non Potential Customers is how far they get through the article that the ad is shown on. That is, users who spend more time scrolling through the article are more likely to click on the ad, and users who spend less time scrolling through the article are less likely to click on the ad.

## Predictive Model

The full source code and summary is here: [Predictive Modelling Task](https://github.com/akannan05/ges24/blob/main/Part%20II-Task%202/SUMMARY.md)

The predictive model we used was a random forest model with a hundred decision trees. The model achieved accuracy, precision, recall, and AUC scores of 1.0 (meaning 100% accuracy). The most important feature was found to be the progress through the article (as seen during aggregate statistics task!)

## Generative Model

The full source code and summary is here: [Generative Modelling Task](https://github.com/akannan05/ges24/blob/main/Part%20II-Task%203/SUMMARY.md)

The generative model we used was a CTGAN which works like a regular GAN but is conditioned to receive and return outputs of a certain format. The CTGAN seemed to generate data which mimicked the distributions of real world data. Columns with privacy risks such as user id and log id were removed and not generated by the CTGAN to ensure trustworthy AI!

# Sources Used Throughout Development

[TPM Coding Tutorial](https://gist.github.com/kenplusplus/f025d04047bc044e139d105b4c708d78)

[Remote Attestation Tutorial](https://tpm2-software.github.io/2020/06/12/Remote-Attestation-With-tpm2-tools.html#service-request-part-1-platform-anonymous-identity-validation)

[Prompt Release Slides](https://docs.google.com/presentation/d/1Pf6I7JC-Pce-BruFViCTFrmgZMRAsNFiHk6ZvPUH4Yw/edit#slide=id.g2e02acbdd07_0_5)

[CTGan Documentation](https://github.com/sdv-dev/CTGAN)
