.PHONY.: clean
clean :
        @find . -name "*.*~" -delete
        @find . -name "*.pyc" -delete
        @find . -name "*.pyo" -delete
        @rm -rf _site
