## Generate Fake Credit Card Transaction Data
Based on original code by [Josh Plotkin](https://github.com/joshplotkin/data_generation)

The purpose of this code is to generate somewhat real credit card transaction data. The initial framework and (awesome) code around profiles, as well as initial assumptions for variable distributions was made by Josh. My list of modifications are below.

### Modifications:

####v 0.2
* Added unix time stamp for transactions for easier programamtic evaluation.
* Individual profiles modified so that there is more variation in the data.
* Modified random generation of age/gender. Original code did not appear to work correctly?
* Added batch files for windows users

####v 0.1
* Transaction times are now included instead of just dates
* Profile specific spending windows (AM/PM with weighting of transaction times)
* Merchant names (specific to spending categories) are now included (along with code for generation)
* Travel probability is added, with profile specific options
* Travel max distances is added, per profile option
* Merchant location is randomized based on home location and profile travel probabilities
* Simulated transaction numbers via faker MD5 hash (replacing sequential 0..n numbering)
* Includes credit card number via faker
* improved cross-platform file path compatibility
