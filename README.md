## Overscripted Web: Data Analysis in the Open

The Systems Research Group (SRG) at Mozilla have created and open sourced a data set of publicly available information that was collected by a November 2017 Web crawl. We want to empower the community to explore the unseen or otherwise not obvious series of JavaScript execution events that are triggered once a user visits a webpage, and all the first- and third-party events that are set in motion when people retrieve content.
Some preliminary insights already uncovered from this data are illustrated in this [blog post](https://medium.com/firefox-context-graph/overscripted-digging-into-javascript-execution-at-scale-2ed508f21862). 
Ongoing analyses can be tracked [here](https://github.com/mozilla/overscripted/tree/master/analyses)

### Technical criteria for submitting an analysis:
- Analyses should be performed in Python using the [jupyter scientific notebook](https://jupyter-notebook.readthedocs.io/en/stable/) format and executing in this [environment](https://github.com/mozilla/overscripted/blob/master/analyses/environment.yaml). 
- Analysis can be submitted by filing a [Pull Request](https://help.github.com/articles/using-pull-requests) against __this__[ repository](https://github.com/mozilla/overscripted) with the analysis formatted as an *.ipynb file in the /analyses/ folder. 
  - Environment can be configured locally by calling `conda env create -f  environment.yaml`
- Only *.ipynb format entries submitted via a pull request to the /analyses/ folder will be considered. Notebooks must be well documented and run on the [environment](https://github.com/mozilla/overscripted/blob/master/analyses/environment.yaml) described. Any entries not meeting these criteria will not be considered and no review will be carried out for error-generating code.
- Any additional code submitted will not be considered. The *.ipynb notebook should be a self contained analysis.

### Accessing the Data
Each of the links below links to a bz2 zipped portion of the total dataset. A small sample of the data is available in `safe_dataset.sample.tar.bz2` to get a feel for the content without commiting to the full download.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2)

Unzipped the full parquet data will be approximately 70GB. Each (compressed) chunk dataset is around 9GB. `SHA256SUMS` contains the checksums for all datasets including the sample.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS](https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS)

### New Contributor Tips

- A valid and much appreciated contribution is to write any of your learnings, be it by reading research papers or through your interaction with the community on gitter and submitting a Pull Request to the repository. You can submit the PR to the README on the main page or the analysis folder README.

- This is not a one issue per person repo. All the questions are very open ended and different people may find very different and complementary things when looking at a question.

- Use a reaction emoji to acknowledge a comment rather than writing a comment like "sure" - helps to keep things clean - but the contributor can still let folks know that they saw a comment.

- You can ask for help and discuss your ideas on gitter. Click [here](https://gitter.im/overscripted-discuss/community) to join !

### Glossary

- TLD means Top-level Domain. You can read up more about it [here.](https://en.wikipedia.org/wiki/Top-level_domain) 

### Resources

- Please refer the [reading list](https://github.com/mozilla/overscripted/wiki/Reading-List-(WIP)) for additional references and information.

- [This](https://github.com/brandon-rhodes/pycon-pandas-tutorial) is a great tutorial to learn Pandas.
