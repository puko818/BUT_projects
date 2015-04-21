# prekladac + linker
CXX=gcc -std=c++98 -Wall

main: mainframe.o gui.o main.o
	$(CXX) `wx-config --libs` mainframe.o gui.o main.o -o main


mainframe.o: mainframe.cpp
	$(CXX) `wx-config --cflags` -c mainframe.cpp

gui.o: gui.cpp
	$(CXX) `wx-config --cflags` -c gui.cpp

main.o: main.cpp gui.cpp mainframe.cpp
	$(CXX) `wx-config --cflags` -c main.cpp



clean:
	rm -f *.o main

