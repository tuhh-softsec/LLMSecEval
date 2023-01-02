# LLMSecEval Dataset

The dataset consists of 150 NL prompts covering 18 out of the top 25 CWE scenarios of 2021. The dataset is provided as a .csv file. The columns and
the description of the information included in them are given below:
 * Prompt ID: Every prompt is given a unique ID in the following format: CWE-<CWE ID>_<abbreviation of the CWE name>-<scenario variation><code sample>.
 Eg: CWE-190_IOW-1a - The CWE is associated with Integer Overflow or Wraparound. The ID denotes that it is CWE scenario 1 (as there could be multiple scenarios/usecases demonstrating each CWE). The scenarios are adopted from the works by [Pearce et al.](https://ieeexplore.ieee.org/abstract/document/9833571). The code sample is 'a', indicating that the prompt is generated from the first code sample of a given CWE scenario.  
 * **CWE**: The full name of the CWE.
 * **NL Prompt**: The NL prompt created from the code of specified CWE scenario.
 * **Source Code Filepath**: The file path indicated the relative path of the code sample in the dataset from the works of [Pearce et al.](https://ieeexplore.ieee.org/abstract/document/9833571). These are the code from which the NL prompt is generated. 
 * **Comment by Pearce et al.**: For many scenarios, Pearce et al. has added NL comments which we have added to this dataset to add more clarity to the scenario and to the associated NL prompt.
 * **Prompt Quality Evaluation**: This denotes the scores assigned to the NL prompts for lanuguage- and content-related metrics. The score range from 1 to 5. The meaning of the scores can be found in the works of [Hu et al.](https://xin-xia.github.io/publication/tosem218.pdf).  
     * Naturalness: measures grammatical fluency of the NL prompts.
     * Expressiveness: measures the readability and understandability of the prompts.
     * Content Adequacy: measures how well the prompts represent the code from which they are generated.
     * Conciseness: measures if the prompts contain unnecessary and irrelevant information.
### Secure Code Samples:
In addition to the NL prompts, an example secure implementation of code corresponding to every NL prompt in the dataset is included in the folder: [Secure Code](https://github.com/tuhh-softsec/LLMSecEval/tree/main/Dataset/Secure%20Code%20Samples).
