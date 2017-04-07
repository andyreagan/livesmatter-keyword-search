cd /users/a/r/areagan/fun/twitter/keyword-searches/2015-10-livesmatter
# /gpfs1/arch/x86_64/python2.7.5/bin/python qsub.py
. pyenv/bin/activate
# /gpfs1/arch/x86_64/python2.7.5/bin/python loaduserdata.py
python loaduserdata.py
# grep -l "delete me" keywordScrape.o* | xargs rm
# mv keywordScrape.o* | vacc-output
