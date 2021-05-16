# Unit testing and Measuring code coverage

## Testing and Coverage tools
- **pytest** testing tool has been used to create and extend unit tests.
- **Coverage** tool has been utilized in order to measure code coverage

## Overview
Unit tests were created and extended for several packages. The packages were selected based on coverage percentage. List of extended and created unit tests are given below:
- bfs
- dp
- heap
- queues
- search
- sort
- stack
- linkedList

## Result
For the above packages, the coverage percentage increased. For the proccess of analyzing unit test coverage and extending them below proccess were applied:
1. All tests were runned by command **coverage run -m pytest** command, and each subfolder of source folder (/algorithm) were given coverage percentage out of 100.
2. Then **coverage report** command were executed for visualizing each .py file code coverage percentage out of 100.
3. After choosing less covered code snippet, **coverage html** command were executed and for each.py file .html file was generated for finding exact line number those were not covered.
4. In the end some possible extension were added to test cases, in some cases new test class was created because of unimported .py files.

## Acknowledgment
Each test case that newly added or extended were discusses by all team members and new build workflow that was created in another task was executed in each pull request for alarming any bugs that was introduced with newly added test. 
