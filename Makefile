CXX = g++
CXXFLAGS = -std=c++17 -g -Wall -DNDEBUG -L./smile-librarie -I./smile-librarie -lsmile -lm
DEPS = smile-librarie/smile.h
OBJ = main.o 

%.o: %.cc $(DEPS)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

main: $(OBJ)
	$(CXX) -o $@ $^ $(CXXFLAGS)

.PHONY: clean
clean:
	rm main *.o