A subdirectory to compute hollistic walk-throughs of simple IMV calculations. Utilises data found in `.data/titanic/`. Please feel free to make pull requests with the same example in other languages! However, don't expect the results to always be the same: despite setting a seed within each language, the value of the output will change as a function of how the data table is shuffled prior to folding (i.e. different seeds in different languages lead to different instantiation of the Mersenne Twister). Expected results:

* Python: 0.238152 (min), 0.510161 (max), 0.334076 (mean)
* R: 0.172877 (min), 0.6217951 (max), 0.351805 (mean)
* MATLAB: 0.215879 (min), 0.500918 (max), 0.325264 (mean)