git archive --prefix=source1/ master | tar -xf -
git archive --prefix=source2/ feature | tar -xf -

cd source1 
coverage run --source='.' -m behave; coverage xml
mv coverage.xml ../coverage_source1.xml
cd ..

cd source2
coverage run --source='.' -m behave; coverage xml
mv coverage.xml ../coverage_source2.xml
cd ..

pycobertura diff --source1 source1/ --source2 source2/ coverage_source1.xml coverage_source2.xml -f html -o output.html
#rm -rf source1/ source2/
