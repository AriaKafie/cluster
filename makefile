all:
	g++ -w -std=c++20 *cpp -o cluster
debug:
	g++ -w -std=c++20 *cpp -g -o debug
clean:
	rm *~ cluster debug
