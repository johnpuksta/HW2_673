# Time-Memory Trade-Off attack
This repo implements the Time-Memory Trade-Off attack described in this paper: https://ee.stanford.edu/~hellman/publications/36.pdf. <br />
<br />
The goal of this assignment is to crack SHA-256, but only the first 24 bits of it. Thus given H(X) = Y, where we are only know Y, find the first 16, 20, and 24 bits of X. <br /> <br />
For this assignment, I decided to create large tables to reduce computation time. This meant that I was sacrificing memory space for reduced time, hence the time-memory trade-off. <br /> <br />
Since SHA-256 outputs in HEX, I generated all possible hex values for the given bits, stored them in a JSON file as an array, then later loaded that JSON file to create my chains of hash values that I could store each starting and ending point into a table. This table would be a JSON file containing a dictionary of key value pairs of these start and end points.  <br />  <br />
Given a random hash, I can now search my table of end points, find the corresponding starting point, and recompute the chain until I find the X value such that H(X) = Y. <br /> <br />
For the 24 bit solution, I realized that VSCode was crashing because my dictionary was too large for the JSON reader to open/write to it. So, I refactored my code to use a SQL database to manage larger memory usage.  <br /> <br />
I purposely left out the JSON and SQL files because they are large. I left in the JSON file for a 8-bit test case to show functionality. However, users have to create these files and initiliaze them with {} for this code to run properly. The SQL database should be created on the first run.
