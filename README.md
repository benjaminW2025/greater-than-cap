# Greater than capability analysis in GPT-2 small

This project is a mechanistic interpretability project aiming to completely reverse engineer the greater than capability of GPT-2 small. My work is based on the original Hanna et al. paper, but none of their methodology or analysis was referenced/used during my own implementation of the experiments. Our workflow will be separated into two main phases:

1) Discovery

Here we will manually inspect attention patterns, residual stream decompositions, etc. for just a handful of inference examples. From our observations and findings we then develop a mechanistic hypothesis for how the model computes this capability. The mechanism for each attention head will be well deocumented, and its behavior across the different inputs will be cross referenced to help create our initial claim.

2) Validation

In the validation phase we will aim to automate some metric calculations across the entirety of the data set.